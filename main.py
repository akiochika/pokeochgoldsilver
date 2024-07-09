import json
import os
import random
import discord
from discord.ext import commands
import asyncio
from threading import Thread
from flask import Flask
import logging

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='p!', intents=intents)

from pokemonlist import pokemon_list

data_files = {
    "caught_pokemons": "caught_pokemons.json",
    "player_data": "player_data.json",
    "field_data": "field_data.json"
}
data = {key: (json.load(open(file)) if os.path.exists(file) else {}) for key, file in data_files.items()}

def save_data():
    for key, file in data_files.items():
        with open(file, 'w') as f:
            json.dump(data[key], f, ensure_ascii=False, indent=4)

def calculate_pokemon_level(base_stats, level):
    return {k.lower(): v * 2 * level // 100 + level + 10 for k, v in base_stats.items()}

def fix_pokemon_level():
    for user_data in data["player_data"].values():
        for pokemon in user_data["team"] + user_data["box"]:
            if pokemon["level"] > 100:
                pokemon.update(calculate_pokemon_level(pokemon["base_stats"], 100))
                pokemon["level"], pokemon["exp"], pokemon["max_hp"] = 100, 0, pokemon["hp"]

fix_pokemon_level()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    bot.loop.create_task(periodic_save_data())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    channel_id = str(message.channel.id)
    user_id = str(message.author.id)
    channel_info = data["field_data"].setdefault(channel_id, {"message_count": 0, "current_pokemon": None, "user_ids": []})

    if user_id not in channel_info["user_ids"]:
        channel_info["user_ids"].append(user_id)

    if not channel_info["current_pokemon"]:
        channel_info["message_count"] += 1
        if channel_info["message_count"] >= 10:
            await spawn_pokemon(message.channel, channel_info["user_ids"])
            channel_info["message_count"] = 0

    await bot.process_commands(message)

async def spawn_pokemon(channel, user_ids):
    channel_id = str(channel.id)
    channel_info = data["field_data"][channel_id]

    if channel_info["current_pokemon"]:
        return

    player_level = sum([data["player_data"][uid]["level"] for uid in user_ids if uid in data["player_data"]]) // len(user_ids)
    chosen_rarity = random.choices(range(1, 7), [90, 9, 0.9, 0.09, 0.009, 0.001])[0]
    shiny = random.randint(1, 4096) == 1
    candidates = [p for p in pokemon_list if p["rarity"] == chosen_rarity and (p["shiny"] == shiny or not p["shiny"])]
    if not candidates:
        candidates = [p for p in pokemon_list if p["rarity"] == 1 and (p["shiny"] == shiny or not p["shiny"])]

    channel_info["current_pokemon"] = random.choice(candidates)
    channel_info["current_pokemon"]["level"] = random.randint(1, min(player_level, 100))
    stats = calculate_pokemon_level(channel_info["current_pokemon"]["base_stats"], channel_info["current_pokemon"]["level"])
    channel_info["current_pokemon"].update(stats)
    channel_info["current_pokemon"]["max_hp"] = channel_info["current_pokemon"]["hp"]

    embed = discord.Embed(title=f"野生の{'色違い ' if shiny else ''}{channel_info['current_pokemon']['name']}が現れた！ レベル: {channel_info['current_pokemon']['level']}")
    embed.set_image(url=channel_info["current_pokemon"]["image"])
    channel_info["current_pokemon"]["message"] = await channel.send(embed=embed)

@bot.command()
async def start(ctx):
    user_id = str(ctx.author.id)
    if user_id not in data["player_data"]:
        data["player_data"][user_id] = {"level": 1, "exp": 0, "team": [], "box": [], "field": []}
        save_data()
        await ctx.send(f'{ctx.author.mention} の冒険が始まった！ ポケモンを選んでください: p!choose チコリータ, p!choose ヒノアラシ, p!choose ワニノコ')
    else:
        await ctx.send(f'{ctx.author.mention} は既に冒険を始めています。')

@bot.command()
async def choose(ctx, pokemon_name: str):
    user_id = str(ctx.author.id)
    if user_id in data["player_data"] and not data["player_data"][user_id]["team"]:
        starter_options = ["チコリータ", "ヒノアラシ", "ワニノコ"]
        if pokemon_name in starter_options:
            starter_pokemon = next((p for p in pokemon_list if p["name"] == pokemon_name), None)
            if starter_pokemon:
                starter_pokemon = starter_pokemon.copy()
                starter_pokemon.update({"level": 5, "exp": 0, "moves": ["たいあたり"]})
                starter_pokemon.update(calculate_pokemon_level(starter_pokemon["base_stats"], 5))
                data["player_data"][user_id]["team"].append(starter_pokemon)
                save_data()
                await ctx.send(f'{ctx.author.mention} は {pokemon_name} を選びました！')
            else:
                await ctx.send(f'{pokemon_name} は選べません。')
        else:
            await ctx.send(f'{pokemon_name} は選べるポケモンに含まれていません。')
    else:
        await ctx.send(f'{ctx.author.mention} は既にポケモンを持っています。')

@bot.command()
async def catch(ctx, pokemon_name: str):
    user_id = str(ctx.author.id)
    channel_id = str(ctx.channel.id)
    channel_info = data["field_data"][channel_id]

    if channel_info["current_pokemon"] and pokemon_name.lower() == channel_info["current_pokemon"]['name'].lower():
        capture_chance = max(1, 100 - (channel_info["current_pokemon"]["hp"] / channel_info["current_pokemon"]["max_hp"]) * 100 - channel_info["current_pokemon"]["rarity"] * 10)
        if random.randint(1, 100) <= capture_chance:
            current_pokemon_copy = channel_info["current_pokemon"].copy()
            current_pokemon_copy["exp"] = 0
            if user_id not in data["player_data"]:
                data["player_data"][user_id] = {"level": 1, "exp": 0, "team": [], "box": []}
            if len(data["player_data"][user_id]["team"]) < 3:
                data["player_data"][user_id]["team"].append(current_pokemon_copy)
            else:
                data["player_data"][user_id]["box"].append(current_pokemon_copy)
            await channel_info["current_pokemon"]["message"].delete()
            await ctx.send(f'{ctx.author.mention} が {"色違い " if channel_info["current_pokemon"]["shiny"] else ""}{channel_info["current_pokemon"]["name"]} を捕まえた！')
            channel_info["current_pokemon"] = None
            save_data()
        else:
            await ctx.send(f'{ctx.author.mention} が {channel_info["current_pokemon"]["name"]} を捕まえ損ねた！')
    else:
        await ctx.send(f'{pokemon_name} はここにいない！')

@bot.command()
async def inventory(ctx):
    user_id = str(ctx.author.id)
    if user_id in data["player_data"]:
        pokemons = ', '.join([p["name"] for p in data["player_data"][user_id]["team"] + data["player_data"][user_id]["box"]])
        await ctx.send(f'{ctx.author.mention} のポケモン: {pokemons}')
    else:
        await ctx.send(f'{ctx.author.mention} はまだポケモンを持っていません。')

@bot.command()
async def player_data_command(ctx):
    user_id = str(ctx.author.id)
    if user_id in data["player_data"]:
        pdata = data["player_data"][user_id]
        team_pokemons = ', '.join([f"{p['name']} (Lv: {p['level']})" for p in pdata["team"]])
        box_count = len(pdata["box"])
        await ctx.send(f'{ctx.author.mention} のデータ: レベル: {pdata["level"]}, 経験値: {pdata["exp"]}, 手持ち: {team_pokemons}, ボックスにいるポケモンの数: {box_count}')
    else:
        await ctx.send(f'{ctx.author.mention} のデータは見つかりませんでした。')

@bot.command()
@commands.has_permissions(administrator=True)
async def reset_player(ctx, member: discord.Member):
    user_id = str(member.id)
    if user_id in data["player_data"]:
        del data["player_data"][user_id]
        save_data()
        await ctx.send(f'{member.mention} のプレイヤーデータをリセットしました。')
    else:
        await ctx.send(f'{member.mention} のプレイヤーデータは見つかりませんでした。')

@bot.command()
@commands.has_permissions(administrator=True)
async def spawn(ctx):
    await spawn_pokemon(ctx.channel, [str(ctx.author.id)])

@bot.command()
async def go(ctx, pokemon_name: str):
    user_id = str(ctx.author.id)
    channel_id = str(ctx.channel.id)
    if user_id in data["player_data"]:
        team = data["player_data"][user_id]["team"]
        field = data["field_data"][channel_id].setdefault("field_pokemons", {}).setdefault(user_id, [])
        if any(p["name"].lower() == pokemon_name.lower() for p in field):
            await ctx.send(f"{ctx.author.mention} は既に {pokemon_name} を出しています。")
            return
        if len(field) >= 1:
            await ctx.send(f"{ctx.author.mention} は既に他のポケモンを出しています。")
            return
        pokemon = next((p for p in team if p["name"].lower() == pokemon_name.lower()), None)
        if pokemon:
            if pokemon["hp"] == 0:
                await ctx.send(f"{pokemon_name} は HP0 なのでフィールドに出せません。")
                return
            field.append(pokemon)
            skills = ', '.join(pokemon.get("moves", ["なし"]))
            hp_bar = create_hp_bar(pokemon["hp"], pokemon["max_hp"])
            embed = discord.Embed(title=f"{ctx.author.name} の {pokemon['name']} (Lv: {pokemon['level']})")
            embed.set_image(url=pokemon["image"])
            embed.add_field(name="HP", value=hp_bar, inline=False)
            embed.add_field(name="技", value=skills, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{pokemon_name} は手持ちにいません。")

@bot.command()
async def return_pokemon(ctx, pokemon_name: str):
    user_id = str(ctx.author.id)
    channel_id = str(ctx.channel.id)
    if user_id in data["player_data"] and channel_id in data["field_data"]:
        field = data["field_data"][channel_id].setdefault("field_pokemons", {}).get(user_id, [])
        pokemon = next((p for p in field if p["name"].lower() == pokemon_name.lower()), None)
        if pokemon:
            field.remove(pokemon)
            save_data()
            await ctx.send(f"{pokemon['name']} を手持ちに戻しました。")

@bot.command()
async def rename(ctx, old_name: str, new_name: str):
    user_id = str(ctx.author.id)
    if user_id in data["player_data"]:
        team = data["player_data"][user_id]["team"]
        pokemon = next((p for p in team if p["name"].lower() == old_name.lower()), None)
        if pokemon:
            pokemon["name"] = new_name
            save_data()
            await ctx.send(f"{old_name} の名前を {new_name} に変更しました。")

@bot.command()
async def skill(ctx, skill_name: str, target_name: str = None):
    if not target_name:
        await ctx.send("効果対象のポケモンを入力してください。")
        return

    channel_id = str(ctx.channel.id)
    channel_info = data["field_data"][channel_id]

    user_id = str(ctx.author.id)
    attacker = next((p for p in channel_info["field_pokemons"].get(user_id, []) if skill_name in p["moves"]), None)

    if not attacker:
        await ctx.send(f"{skill_name} を持つポケモンがフィールドにいません。")
        return

    if channel_info["current_pokemon"] and target_name.lower() == channel_info["current_pokemon"]['name'].lower():
        damage = get_skill_damage(skill_name, attacker, channel_info["current_pokemon"])
        channel_info["current_pokemon"]["hp"] = max(0, channel_info["current_pokemon"]["hp"] - damage)
        hp_bar = create_hp_bar(channel_info["current_pokemon"]["hp"], channel_info["current_pokemon"]["max_hp"])

        if channel_info["current_pokemon"]["hp"] == 0:
            await ctx.send(f"{channel_info['current_pokemon']['name']} は倒れた！")
            channel_info["current_pokemon"] = None
        else:
            embed = discord.Embed(title=f"野生の{channel_info['current_pokemon']['name']}")
            embed.set_image(url=channel_info["current_pokemon"]["image"])
            embed.add_field(name="HP", value=hp_bar, inline=False)
            await ctx.send(embed=embed)
        save_data()
    else:
        await ctx.send(f"{target_name} はフィールドにいません。")

@bot.command()
@commands.has_permissions(administrator=True)
async def all_data_reset(ctx):
    for key in data_files:
        data[key] = {}
    save_data()
    await ctx.send("全プレイヤーのデータを初期化しました。")

@bot.command()
@commands.has_permissions(administrator=True)
async def reset(ctx, member: discord.Member):
    user_id = str(member.id)
    if user_id in data["player_data"]:
        del data["player_data"][user_id]
        save_data()
        await ctx.send(f'{member.mention} のプレイヤーデータをリセットしました。')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("有効なコマンドを入力してください。")
    else:
        await ctx.send("エラーが発生しました。管理者に連絡してください。")

async def periodic_save_data():
    while True:
        await asyncio.sleep(600)
        save_data()

async def main():
    async with bot:
        Thread(target=run_flask).start()
        await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    asyncio.run(main())
