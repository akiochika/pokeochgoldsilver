import json
import os
import random
import discord
from discord.ext import commands
import asyncio
from datetime import timedelta
import base64
import requests
from skilllist import get_skill_damage
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

channel_data = {}
data_file = 'caught_pokemons.json'
player_data_file = 'player_data.json'
field_data_file = 'field_data.json'
caught_pokemons = {}
player_data = {}

# データの読み込み
if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        caught_pokemons = json.load(file)

if os.path.exists(player_data_file):
    with open(player_data_file, 'r') as file:
        player_data = json.load(file)

if os.path.exists(field_data_file):
    with open(field_data_file, 'r') as file:
        channel_data = json.load(file)

# Convert user_ids from list to set if needed
for channel_id, channel_info in channel_data.items():
    if isinstance(channel_info.get("user_ids"), list):
        channel_info["user_ids"] = set(channel_info["user_ids"])

# レベル100を超えるポケモンの修正
def fix_pokemon_level():
    for user_id, data in player_data.items():
        for pokemon in data["team"]:
            if pokemon["level"] > 100:
                pokemon["level"] = 100
                pokemon["exp"] = 0
                pokemon.update(calculate_pokemon_level(pokemon["base_stats"], 100))
                pokemon["max_hp"] = pokemon["hp"]
        for pokemon in data["box"]:
            if pokemon["level"] > 100:
                pokemon["level"] = 100
                pokemon["exp"] = 0
                pokemon.update(calculate_pokemon_level(pokemon["base_stats"], 100))
                pokemon["max_hp"] = pokemon["hp"]

# メッセージカウントの初期値
spawn_threshold = 10

rarity_to_timeout = {
    1: 60,
    2: 50,
    3: 30,
    4: 20,
    5: 7,
    6: 15
}

rarity_level_min = {
    1: 1,
    2: 15,
    3: 30,
    4: 70,
    5: 1,
    6: 90
}

def calculate_pokemon_level(base_stats, level):
    hp = base_stats['HP'] * 2 * level // 100 + level + 10
    attack = base_stats['攻撃'] * 2 * level // 100 + 5
    defense = base_stats['防御'] * 2 * level // 100 + 5
    special_attack = base_stats['特攻'] * 2 * level // 100 + 5
    special_defense = base_stats['特防'] * 2 * level // 100 + 5
    speed = base_stats['素早さ'] * 2 * level // 100 + 5
    return {'hp': hp, 'attack': attack, 'defense': defense, 'special_attack': special_attack, 'special_defense': special_defense, 'speed': speed}

fix_pokemon_level()

def calculate_capture_chance(pokemon, current_hp):
    base_chance = 100
    hp_factor = (current_hp / pokemon["max_hp"]) * 100
    rarity_penalty = pokemon["rarity"] * 10
    capture_chance = base_chance - hp_factor - rarity_penalty
    return max(capture_chance, 1)

def create_hp_bar(current_hp, max_hp, length=10):
    filled_length = int(length * current_hp // max_hp)
    bar = '█' * filled_length + '-' * (length - filled_length)
    return f"[{bar}] {current_hp}/{max_hp}"

def get_average_player_team_level(user_ids):
    player_levels = []
    for user_id in user_ids:
        if user_id in player_data:
            team_levels = [pokemon["level"] for pokemon in player_data[user_id]["team"]]
            if team_levels:
                player_levels.append(sum(team_levels) // len(team_levels))
    return sum(player_levels) // len(player_levels) if player_levels else 1

def calculate_spawn_rates(player_level):
    min_rates = [90, 9, 0.9, 0.09, 0.009, 0.001]
    max_rates = [40, 30, 20, 9, 0.1, 0.9]
    spawn_rates = []

    for min_rate, max_rate in zip(min_rates, max_rates):
        rate = min_rate - (min_rate - max_rate) * (player_level / 100)
        spawn_rates.append(rate)

    total = sum(spawn_rates)
    normalized_rates = [rate / total for rate in spawn_rates]

    return normalized_rates

def choose_pokemon_by_rarity(spawn_rates):
    cumulative_rates = [sum(spawn_rates[:i+1]) for i in range(len(spawn_rates))]
    roll = random.random()

    for rarity, rate in enumerate(cumulative_rates):
        if roll < rate:
            return rarity + 1

def determine_shiny():
    return random.randint(1, 4096) == 1

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    bot.loop.create_task(check_all_hp_zero())
    load_field_data()

@bot.event
async def on_message(message):
    try:
        if message.author == bot.user:
            return

        channel_id = str(message.channel.id)
        user_id = str(message.author.id)

        if channel_id not in channel_data:
            channel_data[channel_id] = {"message_count": 0, "current_pokemon": None, "wild_pokemon_escape_task": None, "user_ids": set(), "field_pokemons": {}}

        channel_info = channel_data[channel_id]
        channel_info["user_ids"].add(user_id)

        if channel_info["current_pokemon"] is None:
            channel_info["message_count"] += 1

            if channel_info["message_count"] >= spawn_threshold:
                await spawn_pokemon(message.channel, channel_info["user_ids"])
                channel_info["message_count"] = 0

        await bot.process_commands(message)
    except Exception as e:
        logging.error(f"Error in on_message: {e}", exc_info=True)

async def spawn_pokemon(channel, user_ids):
    channel_id = str(channel.id)
    channel_info = channel_data[channel_id]

    if channel_info["current_pokemon"] is not None:
        return

    player_level = get_average_player_team_level(user_ids)
    spawn_rates = calculate_spawn_rates(player_level)
    chosen_rarity = choose_pokemon_by_rarity(spawn_rates)

    shiny = determine_shiny()

    candidates = [pokemon for pokemon in pokemon_list if pokemon["rarity"] == chosen_rarity and (pokemon["shiny"] == shiny or not pokemon["shiny"]) and pokemon["appear"] == 0]
    if not candidates:
        candidates = [pokemon for pokemon in pokemon_list if pokemon["rarity"] == 1 and (pokemon["shiny"] == shiny or not pokemon["shiny"]) and pokemon["appear"] == 0]

    if not candidates:
        return

    channel_info["current_pokemon"] = random.choice(candidates)
    channel_info["current_pokemon"]["shiny"] = shiny

    if all(user_id not in player_data for user_id in user_ids):
        min_level, max_level = 1, 5
    else:
        min_level = rarity_level_min[channel_info["current_pokemon"]["rarity"]]
        max_level = min(player_level, 100)

    if min_level > max_level:
        channel_info["current_pokemon"] = random.choice([pokemon for pokemon in pokemon_list if pokemon["rarity"] == 1 and pokemon["appear"] == 0])
        channel_info["current_pokemon"]["level"] = random.randint(1, 5)
    else:
        channel_info["current_pokemon"]["level"] = random.randint(min_level, max_level)

    stats = calculate_pokemon_level(channel_info["current_pokemon"]["base_stats"], channel_info["current_pokemon"]["level"])
    channel_info["current_pokemon"].update(stats)
    channel_info["current_pokemon"]["max_hp"] = channel_info["current_pokemon"]["hp"]

    wild_pokemon_timeout = rarity_to_timeout[channel_info["current_pokemon"]["rarity"]]

    hp_bar = create_hp_bar(channel_info["current_pokemon"]["hp"], channel_info["current_pokemon"]["max_hp"])
    embed = discord.Embed(title=f"野生の{'色違い ' if channel_info['current_pokemon']['shiny'] else ''}{channel_info['current_pokemon']['name']}が現れた！ レベル: {channel_info['current_pokemon']['level']}")
    embed.set_image(url=channel_info["current_pokemon"]["image"])
    embed.add_field(name="HP", value=hp_bar, inline=False)
    channel_info["current_pokemon"]["message"] = await channel.send(embed=embed)

    if channel_info["wild_pokemon_escape_task"] and not channel_info["wild_pokemon_escape_task"].done():
        channel_info["wild_pokemon_escape_task"].cancel()

    channel_info["wild_pokemon_escape_task"] = bot.loop.create_task(wild_pokemon_escape(channel))
    channel_info["wild_pokemon_attack_task"] = bot.loop.create_task(wild_pokemon_attack(channel))
    save_field_data()  # Save data when a wild Pokémon spawns

async def wild_pokemon_escape(channel):
    channel_id = str(channel.id)
    channel_info = channel_data[channel_id]

    try:
        await asyncio.sleep(rarity_to_timeout[channel_info["current_pokemon"]["rarity"]])
        if channel_info["current_pokemon"]:
            await channel_info["current_pokemon"]["message"].delete()
            await channel.send(f"{channel_info['current_pokemon']['name']} は逃げてしまった！")
            channel_info["current_pokemon"] = None
            for user_id in channel_info["user_ids"]:
                channel_info["field_pokemons"][user_id] = []
            save_player_data()
            save_field_data()
    except asyncio.CancelledError:
        pass

rarity_to_attack_interval = {
    1: 10,
    2: 9,
    3: 8,
    4: 7,
    5: 5,
    6: 6
}

async def wild_pokemon_attack(channel):
    channel_id = str(channel.id)
    channel_info = channel_data[channel_id]

    try:
        while channel_info["current_pokemon"]:
            attack_interval = rarity_to_attack_interval.get(channel_info["current_pokemon"]["rarity"], 5)
            await asyncio.sleep(attack_interval)
            if not channel_info["current_pokemon"]:
                return
            if not channel_info["field_pokemons"]:
                return
            attacker = channel_info["current_pokemon"]
            move = random.choice(attacker["moves"])
            target_user_id = random.choice(list(channel_info["field_pokemons"].keys()))
            if not channel_info["field_pokemons"][target_user_id]:
                continue
            target_pokemon = random.choice(channel_info["field_pokemons"][target_user_id])
            damage = get_skill_damage(move, attacker, target_pokemon)
            target_pokemon["hp"] = max(0, target_pokemon["hp"] - damage)
            hp_bar = create_hp_bar(target_pokemon["hp"], target_pokemon["max_hp"])
            skills = ', '.join(target_pokemon.get("moves", ["なし"]))

            if "message" in target_pokemon and target_pokemon["message"]:
                try:
                    await target_pokemon["message"].delete()
                except discord.errors.NotFound:
                    pass

            embed = discord.Embed(title=f"{attacker['name']} は {target_pokemon['name']} に {move} を使った！")
            embed.set_image(url=target_pokemon["image"])
            embed.add_field(name="ダメージ", value=f"{damage}", inline=False)
            embed.add_field(name="HP", value=hp_bar, inline=False)
            embed.add_field(name="技", value=skills, inline=False)
            target_pokemon["message"] = await channel.send(embed=embed)
            save_field_data()  # Save data when a Pokémon attacks

            if target_pokemon["hp"] == 0:
                await channel.send(f"{target_pokemon['name']} は倒れた！ {target_pokemon['name']} は自動的に手持ちに戻ります。")
                channel_info["field_pokemons"][target_user_id].remove(target_pokemon)
                player_data[target_user_id]["team"].append(target_pokemon)
                save_player_data()
                save_field_data()  # Save data when a Pokémon faints
    except Exception as e:
        logging.error(f"Error in wild_pokemon_attack: {e}", exc_info=True)

@bot.command()
async def start(ctx):
    try:
        user_id = str(ctx.author.id)
        if user_id not in player_data:
            player_data[user_id] = {"level": 1, "exp": 0, "team": [], "box": [], "field": []}
            save_player_data()
            await ctx.send(f'{ctx.author.mention} の冒険が始まった！ ポケモンを選んでください: p!choose チコリータ, p!choose ヒノアラシ, p!choose ワニノコ')
        else:
            await ctx.send(f'{ctx.author.mention} は既に冒険を始めています。')
    except Exception as e:
        logging.error(f"Error in start command: {e}", exc_info=True)

@bot.command()
async def choose(ctx, pokemon_name: str):
    try:
        user_id = str(ctx.author.id)
        starter_options = ["チコリータ", "ヒノアラシ", "ワニノコ"]

        if user_id in player_data and len(player_data[user_id]["team"]) == 0:
            if pokemon_name in starter_options:
                starter_pokemon = next((pokemon for pokemon in pokemon_list if pokemon["name"] == pokemon_name), None)
                if starter_pokemon:
                    starter_pokemon = starter_pokemon.copy()
                    starter_pokemon["level"] = 5
                    starter_pokemon["exp"] = 0
                    starter_pokemon.update(calculate_pokemon_level(starter_pokemon["base_stats"], starter_pokemon["level"]))
                    starter_pokemon["max_hp"] = starter_pokemon["hp"]
                    starter_pokemon["moves"] = ["たいあたり"]
                    player_data[user_id]["team"].append(starter_pokemon)
                    save_player_data()
                    await ctx.send(f'{ctx.author.mention} は {pokemon_name} を選びました！')
                else:
                    await ctx.send(f'{pokemon_name} は選べません。')
            else:
                await ctx.send(f'{pokemon_name} は選べるポケモンに含まれていません。')
        else:
            await ctx.send(f'{ctx.author.mention} は既にポケモンを持っています。')
    except Exception as e:
        logging.error(f"Error in choose command: {e}", exc_info=True)

def github_write_file(content, file_path, message):
    try:
        url = f'https://api.github.com/repos/{REPO_NAME}/contents/{file_path}'
        headers = {
            'Authorization': f'token {GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            sha = response.json()['sha']
        else:
            sha = None

        content = base64.b64encode(content.encode()).decode()

        data = {
            'message': message,
            'content': content,
            'branch': GITHUB_BRANCH
        }

        if sha:
            data['sha'] = sha

        response = requests.put(url, headers=headers, json=data)
        if response.status_code in [200, 201]:
            print('File successfully updated.')
        else:
            print('Failed to update file:', response.json())
    except Exception as e:
        logging.error(f"Error in github_write_file: {e}", exc_info=True)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "akiochika/pokeochgoldsilver"
PLAYER_DATA_FILE_PATH = "player_data.json"
CAUGHT_POKEMONS_FILE_PATH = "caught_pokemons.json"
FIELD_DATA_FILE_PATH = "field_data.json"

def get_file_sha(file_path):
    try:
        url = f"https://api.github.com/repos/{REPO_NAME}/contents/{file_path}"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()["sha"]
        return None
    except Exception as e:
        logging.error(f"Error in get_file_sha: {e}", exc_info=True)
        return None

def update_github_file(file_path, content):
    try:
        url = f"https://api.github.com/repos/{REPO_NAME}/contents/{file_path}"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        file_sha = get_file_sha(file_path)
        data = {
            "message": f"Update {file_path}",
            "content": base64.b64encode(content.encode()).decode(),
            "sha": file_sha
        }
        response = requests.put(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"Successfully updated {file_path} on GitHub")
        else:
            print(f"Failed to update {file_path} on GitHub: {response.content}")
    except Exception as e:
        logging.error(f"Error in update_github_file: {e}", exc_info=True)

def save_player_data():
    try:
        for user_id in player_data:
            for pokemon in player_data[user_id]["team"]:
                if "message" in pokemon:
                    del pokemon["message"]
            for pokemon in player_data[user_id]["box"]:
                if "message" in pokemon:
                    del pokemon["message"]
            for pokemon in player_data[user_id]["field"]:
                if "message" in pokemon:
                    del pokemon["message"]

        player_data_json = json.dumps(player_data, ensure_ascii=False, indent=4)
        with open(player_data_file, 'w') as file:
            file.write(player_data_json)
        
        update_github_file(PLAYER_DATA_FILE_PATH, player_data_json)
    except Exception as e:
        logging.error(f"Error in save_player_data: {e}", exc_info=True)

def save_caught_pokemons():
    try:
        caught_pokemons_json = json.dumps(caught_pokemons, ensure_ascii=False, indent=4)
        with open(data_file, 'w') as file:
            file.write(caught_pokemons_json)
        
        update_github_file(CAUGHT_POKEMONS_FILE_PATH, caught_pokemons_json)
    except Exception as e:
        logging.error(f"Error in save_caught_pokemons: {e}", exc_info=True)

def clean_channel_data(data):
    cleaned_data = {}
    for channel_id, channel_info in data.items():
        cleaned_channel_info = channel_info.copy()
        cleaned_channel_info["user_ids"] = list(cleaned_channel_info["user_ids"])  # Convert set to list
        cleaned_channel_info["current_pokemon"] = cleaned_channel_info["current_pokemon"].copy()
        if "message" in cleaned_channel_info["current_pokemon"]:
            del cleaned_channel_info["current_pokemon"]["message"]
        if "wild_pokemon_escape_task" in cleaned_channel_info:
            del cleaned_channel_info["wild_pokemon_escape_task"]
        if "wild_pokemon_attack_task" in cleaned_channel_info:
            del cleaned_channel_info["wild_pokemon_attack_task"]

        field_pokemons = {}
        for user_id, pokemons in channel_info["field_pokemons"].items():
            field_pokemons[user_id] = []
            for pokemon in pokemons:
                cleaned_pokemon = pokemon.copy()
                if "message" in cleaned_pokemon:
                    del cleaned_pokemon["message"]
                field_pokemons[user_id].append(cleaned_pokemon)
        cleaned_channel_info["field_pokemons"] = field_pokemons

        cleaned_data[channel_id] = cleaned_channel_info
    return cleaned_data

def save_field_data():
    try:
        cleaned_data = clean_channel_data(channel_data)
        field_data_json = json.dumps(cleaned_data, ensure_ascii=False, indent=4)
        with open(field_data_file, 'w') as file:
            file.write(field_data_json)

        update_github_file(FIELD_DATA_FILE_PATH, field_data_json)
    except Exception as e:
        logging.error(f"Error in save_field_data: {e}", exc_info=True)

@bot.command()
async def deposit(ctx, pokemon_name: str):
    try:
        user_id = str(ctx.author.id)
        if user_id not in player_data:
            await ctx.send(f"{ctx.author.mention} あなたのデータが見つかりません。")
            return

        if len(player_data[user_id]["team"]) + len(player_data[user_id]["field"]) <= 1:
            await ctx.send(f"{ctx.author.mention} 手持ちと場にいるポケモンが少なすぎます。")
            return

        for i, pokemon in enumerate(player_data[user_id]["team"]):
            if pokemon["name"].lower() == pokemon_name.lower():
                player_data[user_id]["box"].append(pokemon)
                del player_data[user_id]["team"][i]
                save_player_data()
                await ctx.send(f"{ctx.author.mention} {pokemon_name} をボックスに預けました。")
                await heal_pokemon_in_box(user_id, pokemon)
                return

        await ctx.send(f"{ctx.author.mention} {pokemon_name} は手持ちにいません。")
    except Exception as e:
        logging.error(f"Error in deposit command: {e}", exc_info=True)


@bot.command()
async def withdraw(ctx, pokemon_name: str):
    try:
        user_id = str(ctx.author.id)
        if user_id not in player_data:
            await ctx.send(f"{ctx.author.mention} あなたのデータが見つかりません。")
            return

        if len(player_data[user_id]["team"]) + len(player_data[user_id]["field"]) >= 3:
            await ctx.send(f"{ctx.author.mention} 手持ちと場にいるポケモンが多すぎます。")
            return

        possible_pokemons = [p for p in player_data[user_id]["box"] if p["name"].lower() == pokemon_name.lower()]
        if not possible_pokemons:
            await ctx.send(f"{ctx.author.mention} {pokemon_name} はボックスにいません。")
            return

        if len(possible_pokemons) > 1:
            await ctx.send(f"{ctx.author.mention} 同じ名前のポケモンが複数います。番号を指定してください。")
            for idx, pokemon in enumerate(possible_pokemons, start=1):
                await ctx.send(f"{idx}: {pokemon['name']} (Lv: {pokemon['level']})")
            msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
            try:
                choice = int(msg.content) - 1
                if 0 <= choice < len(possible_pokemons):
                    selected_pokemon = possible_pokemons[choice]
                else:
                    await ctx.send(f"{ctx.author.mention} 番号が無効です。")
                    return
            except ValueError:
                await ctx.send(f"{ctx.author.mention} 番号が無効です。")
                return
        else:
            selected_pokemon = possible_pokemons[0]

        if len(player_data[user_id]["team"]) < 3:
            player_data[user_id]["team"].append(selected_pokemon)
        else:
            player_data[user_id]["field"].append(selected_pokemon)

        player_data[user_id]["box"].remove(selected_pokemon)
        save_player_data()
        await ctx.send(f"{ctx.author.mention} {pokemon_name} をボックスから引き出しました。")
    except Exception as e:
        logging.error(f"Error in withdraw command: {e}", exc_info=True)

async def heal_pokemon_in_box(user_id, pokemon):
    try:
        await asyncio.sleep(600)
        pokemon["hp"] = pokemon["max_hp"]
        save_player_data()
    except Exception as e:
        logging.error(f"Error in heal_pokemon_in_box: {e}", exc_info=True)

async def auto_return_to_hand(user_id, channel_id, pokemon_name, delay):
    try:
        await asyncio.sleep(delay)
        if user_id in player_data and channel_id in channel_data:
            field = channel_data[channel_id]["field_pokemons"].get(user_id, [])
            pokemon = next((p for p in field if p["name"].lower() == pokemon_name.lower()), None)
            if pokemon and not any(channel_info.get("current_pokemon") for channel_info in channel_data.values()):
                field.remove(pokemon)
                save_player_data()
                member = bot.get_user(int(user_id))
                if member:
                    await member.send(f'{pokemon_name} がフィールドに出続けたので自動的に手持ちに戻りました。')
    except Exception as e:
        logging.error(f"Error in auto_return_to_hand: {e}", exc_info=True)

@bot.command()
async def go(ctx, pokemon_name: str):
    try:
        user_id = str(ctx.author.id)
        channel_id = str(ctx.channel.id)

        if user_id in player_data:
            team = player_data[user_id]["team"]
            field = channel_data[channel_id]["field_pokemons"].get(user_id, [])

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
                channel_data[channel_id]["field_pokemons"][user_id] = field
                skills = ', '.join(pokemon.get("moves", ["なし"]))
                hp_bar = create_hp_bar(pokemon["hp"], pokemon["max_hp"])
                embed = discord.Embed(title=f"{ctx.author.name} の {pokemon['name']} (Lv: {pokemon['level']})")
                embed.set_image(url=pokemon["image"])
                embed.add_field(name="HP", value=hp_bar, inline=False)
                embed.add_field(name="技", value=skills, inline=False)
                msg = await ctx.send(embed=embed)
                await msg.delete(delay=300)
                bot.loop.create_task(auto_return_to_hand(user_id, channel_id, pokemon_name, 100))
            else:
                await ctx.send(f"{pokemon_name} は手持ちにいません。")
    except Exception as e:
        logging.error(f"Error in go command: {e}", exc_info=True)

async def restore_hp(user_id):
    try:
        if user_id in player_data:
            for pokemon in player_data[user_id]["team"]:
                pokemon["hp"] = pokemon["max_hp"]
            save_player_data()
    except Exception as e:
        logging.error(f"Error in restore_hp: {e}", exc_info=True)

async def check_all_hp_zero():
    try:
        while True:
            await asyncio.sleep(60)
            for user_id in player_data:
                if all(pokemon["hp"] == 0 for pokemon in player_data[user_id]["team"]):
                    await asyncio.sleep(300)
                    if all(pokemon["hp"] == 0 for pokemon in player_data[user_id]["team"]):
                        await restore_hp(user_id)
                        member = bot.get_user(int(user_id))
                        if member:
                            await member.send("手持ちのポケモンのHPが全回復しました。")
    except Exception as e:
        logging.error(f"Error in check_all_hp_zero: {e}", exc_info=True)

@bot.command()
async def return_pokemon(ctx, pokemon_name: str):
    try:
        user_id = str(ctx.author.id)
        channel_id = str(ctx.channel.id)

        if user_id in player_data and channel_id in channel_data:
            field = channel_data[channel_id]["field_pokemons"].get(user_id, [])
            pokemon = next((p for p in field if p["name"].lower() == pokemon_name.lower()), None)
            if pokemon:
                field.remove(pokemon)
                await ctx.send(f"{pokemon['name']} を手持ちに戻しました。")
                save_field_data()
    except Exception as e:
        logging.error(f"Error in return_pokemon command: {e}", exc_info=True)

@bot.command()
async def rename(ctx, old_name: str, new_name: str):
    try:
        user_id = str(ctx.author.id)
        if user_id in player_data:
            team = player_data[user_id]["team"]
            pokemon = next((p for p in team if p["name"].lower() == old_name.lower()), None)
            if pokemon:
                pokemon["name"] = new_name
                await ctx.send(f"{old_name} の名前を {new_name} に変更しました。")
                save_field_data()
    except Exception as e:
        logging.error(f"Error in rename command: {e}", exc_info=True)

@bot.command()
async def skill(ctx, skill_name: str, target_name: str = None):
    try:
        if not target_name:
            await ctx.send("効果対象のポケモンを入力してください。")
            return

        channel_id = str(ctx.channel.id)
        channel_info = channel_data[channel_id]

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
                if channel_info["current_pokemon"]["message"]:
                    try:
                        await channel_info["current_pokemon"]["message"].delete()
                    except discord.errors.NotFound:
                        pass
                await ctx.send(f"{channel_info['current_pokemon']['name']} は倒れた！")
                await give_exp_on_defeat(ctx, channel_info["current_pokemon"]["level"])
                channel_info["current_pokemon"] = None

                for user_id in channel_info["user_ids"]:
                    channel_info["field_pokemons"][user_id] = []
                save_player_data()
                save_field_data()
            else:
                if channel_info["current_pokemon"]["message"]:
                    try:
                        await channel_info["current_pokemon"]["message"].delete()
                    except discord.errors.NotFound:
                        pass
                embed = discord.Embed(title=f"野生の{channel_info['current_pokemon']['name']}")
                embed.set_image(url=channel_info["current_pokemon"]["image"])
                embed.add_field(name="HP", value=hp_bar, inline=False)
                channel_info["current_pokemon"]["message"] = await ctx.send(embed=embed)
                save_field_data()
        else:
            await ctx.send(f"{target_name} はフィールドにいません。")
    except Exception as e:
        logging.error(f"Error in skill command: {e}", exc_info=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def all_data_reset(ctx):
    try:
        global caught_pokemons, player_data

        caught_pokemons = {}
        player_data = {}

        with open(data_file, 'w') as file:
            json.dump(caught_pokemons, file, ensure_ascii=False, indent=4)

        with open(player_data_file, 'w') as file:
            json.dump(player_data, file, ensure_ascii=False, indent=4)

        await ctx.send("全プレイヤーのデータを初期化しました。")
    except Exception as e:
        logging.error(f"Error in all_data_reset command: {e}", exc_info=True)

def calculate_exp(level, rarity):
    base_exp = 10 * (level ** 1.5)
    rarity_multiplier = 1 + 0.2 * (rarity - 1)
    return int(base_exp * rarity_multiplier)

async def give_exp(user_id, exp):
    try:
        if user_id in player_data:
            player_data[user_id]["exp"] += exp
            await check_level_up(user_id)
            save_player_data()
    except Exception as e:
        logging.error(f"Error in give_exp: {e}", exc_info=True)

async def check_level_up(user_id):
    try:
        while player_data[user_id]["exp"] >= calculate_exp(player_data[user_id]["level"], 1):
            player_data[user_id]["exp"] -= calculate_exp(player_data[user_id]["level"], 1)
            player_data[user_id]["level"] += 1
            if player_data[user_id]["level"] > 100:
                player_data[user_id]["level"] = 100
                player_data[user_id]["exp"] = 0

            for pokemon in player_data[user_id]["team"]:
                while pokemon["exp"] >= calculate_exp(pokemon["level"], pokemon["rarity"]):
                    pokemon["exp"] -= calculate_exp(pokemon["level"], pokemon["rarity"])
                    pokemon["level"] += 1
                    if pokemon["level"] > 100:
                        pokemon["level"] = 100
                        pokemon["exp"] = 0
                    pokemon.update(calculate_pokemon_level(pokemon["base_stats"], pokemon["level"]))
                    pokemon["max_hp"] = pokemon["hp"]
                    await check_evolution(user_id, pokemon)
    except Exception as e:
        logging.error(f"Error in check_level_up: {e}", exc_info=True)

async def give_exp_on_catch(ctx, pokemon_level):
    try:
        exp = calculate_exp(pokemon_level, 1)
        for user_id in channel_data[str(ctx.channel.id)]["user_ids"]:
            if channel_data[str(ctx.channel.id)]["field_pokemons"].get(user_id, []):
                await give_exp(user_id, exp)
                member = ctx.guild.get_member(int(user_id))
                if member:
                    await ctx.send(f'{member.mention} が {exp} の経験値を獲得しました！')
    except Exception as e:
        logging.error(f"Error in give_exp_on_catch: {e}", exc_info=True)

async def give_exp_on_defeat(ctx, pokemon_level):
    try:
        exp = calculate_exp(pokemon_level, 1)
        channel_id = str(ctx.channel.id)
        if channel_id in channel_data:
            for user_id in channel_data[channel_id]["user_ids"]:
                if channel_data[channel_id]["field_pokemons"].get(user_id, []):
                    for pokemon in channel_data[channel_id]["field_pokemons"][user_id]:
                        pokemon["exp"] += exp
                        while pokemon["exp"] >= calculate_exp(pokemon["level"], pokemon["rarity"]):
                            pokemon["exp"] -= calculate_exp(pokemon["level"], pokemon["rarity"])
                            pokemon["level"] += 1
                            if pokemon["level"] > 100:
                                pokemon["level"] = 100
                                pokemon["exp"] = 0
                            pokemon.update(calculate_pokemon_level(pokemon["base_stats"], pokemon["level"]))
                            pokemon["max_hp"] = pokemon["hp"]
                            await check_evolution(ctx, user_id, pokemon)
                    member = ctx.guild.get_member(int(user_id))
                    if member:
                        await ctx.send(f'{member.mention} のポケモンが {exp} の経験値を獲得しました！')
            save_player_data()
    except Exception as e:
        logging.error(f"Error in give_exp_on_defeat: {e}", exc_info=True)

async def check_evolution(ctx, user_id, pokemon):
    try:
        if pokemon["evolve_level"] is not None and pokemon["level"] >= pokemon["evolve_level"] and "evolves_to" in pokemon:
            evolves_to = next((p for p in pokemon_list if p["name"] == pokemon["evolves_to"] and p["shiny"] == pokemon["shiny"]), None)
            if evolves_to:
                original_name = pokemon["name"]
                shiny = pokemon["shiny"]
                pokemon.update(evolves_to)
                pokemon.update(calculate_pokemon_level(pokemon["base_stats"], pokemon["level"]))
                pokemon["max_hp"] = pokemon["hp"]
                pokemon["shiny"] = shiny
                await ctx.send(f'{ctx.author.mention} の {original_name} が {pokemon["name"]} に進化しました！')
                save_player_data()
    except Exception as e:
        logging.error(f"Error in check_evolution: {e}", exc_info=True)

@bot.command()
async def catch(ctx, pokemon_name: str):
    try:
        user_id = str(ctx.author.id)
        channel_id = str(ctx.channel.id)
        channel_info = channel_data[channel_id]

        if channel_info["current_pokemon"] and pokemon_name.lower() == channel_info["current_pokemon"]['name'].lower():
            capture_chance = calculate_capture_chance(channel_info["current_pokemon"], channel_info["current_pokemon"]["hp"])
            if random.randint(1, 100) <= capture_chance:
                if user_id not in caught_pokemons:
                    caught_pokemons[user_id] = []
                if user_id not in player_data:
                    player_data[user_id] = {"level": 1, "exp": 0, "team": [], "box": [], "field": []}
                current_pokemon_copy = channel_info["current_pokemon"].copy()
                current_pokemon_copy["exp"] = 0
                current_pokemon_copy["shiny"] = channel_info["current_pokemon"]["shiny"]
                if len(player_data[user_id]["team"]) < 3:
                    player_data[user_id]["team"].append(current_pokemon_copy)
                else:
                    player_data[user_id]["box"].append(current_pokemon_copy)
                caught_pokemons[user_id].append(current_pokemon_copy)

                for pokemon in caught_pokemons[user_id]:
                    if "message" in pokemon:
                        del pokemon["message"]
                for pokemon in player_data[user_id]["team"]:
                    if "message" in pokemon:
                        del pokemon["message"]
                for pokemon in player_data[user_id]["box"]:
                    if "message" in pokemon:
                        del pokemon["message"]

                with open(data_file, 'w') as file:
                    json.dump(caught_pokemons, file, ensure_ascii=False, indent=4)
                with open(player_data_file, 'w') as file:
                    json.dump(player_data, file, ensure_ascii=False, indent=4)

                await channel_info["current_pokemon"]["message"].delete()
                await ctx.send(f'{ctx.author.mention} が {"色違い " if channel_info["current_pokemon"]["shiny"] else ""}{channel_info["current_pokemon"]["name"]} を捕まえた！')
                await give_exp_on_catch(ctx, channel_info["current_pokemon"]["level"])
                channel_info["current_pokemon"] = None
                if channel_info["wild_pokemon_escape_task"] and not channel_info["wild_pokemon_escape_task"].done():
                    channel_info["wild_pokemon_escape_task"].cancel()

                for user_id in channel_info["user_ids"]:
                    channel_info["field_pokemons"][user_id] = []
                save_player_data()
                save_field_data()
            else:
                msg = await ctx.send(f'{ctx.author.mention} が {channel_info["current_pokemon"]["name"]} を捕まえ損ねた！')
                await msg.delete(delay=5)
        else:
            await ctx.send(f'{pokemon_name} はここにいない！')
    except Exception as e:
        logging.error(f"Error in catch command: {e}", exc_info=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def reset(ctx, member: discord.Member):
    try:
        user_id = str(member.id)
        if user_id in caught_pokemons:
            del caught_pokemons[user_id]

            with open(data_file, 'w') as file:
                json.dump(caught_pokemons, file, ensure_ascii=False, indent=4)

            await ctx.send(f'{member.mention} の所持ポケモンをリセットしました。')
        else:
            await ctx.send(f'{member.mention} はまだポケモンを捕まえていません。')
    except Exception as e:
        logging.error(f"Error in reset command: {e}", exc_info=True)

@reset.error
async def reset_error(ctx, error):
    try:
        if isinstance(error, commands.CheckFailure):
            await ctx.send("このコマンドを使用するには管理者権限が必要です。")
    except Exception as e:
        logging.error(f"Error in reset_error: {e}", exc_info=True)
        
@bot.command()
@commands.has_permissions(administrator=True)
async def spawn(ctx):
    try:
        await spawn_pokemon(ctx.channel, [str(ctx.author.id)])
    except Exception as e:
        logging.error(f"Error in spawn command: {e}", exc_info=True)

@spawn.error
async def spawn_error(ctx, error):
    try:
        if isinstance(error, commands.CheckFailure):
            await ctx.send("このコマンドを使用するには管理者権限が必要です。")
    except Exception as e:
        logging.error(f"Error in spawn_error: {e}", exc_info=True)

@bot.command()
async def inventory(ctx):
    try:
        user_id = str(ctx.author.id)
        if user_id in caught_pokemons and caught_pokemons[user_id]:
            pokemons = ', '.join([p["name"] for p in caught_pokemons[user_id]])
            await ctx.send(f'{ctx.author.mention} が捕まえたポケモン: {pokemons}')
        else:
            await ctx.send(f'{ctx.author.mention} はまだポケモンを捕まえていません。')
    except Exception as e:
        logging.error(f"Error in inventory command: {e}", exc_info=True)

@bot.command()
async def player_data_command(ctx):
    try:
        user_id = str(ctx.author.id)
        if user_id in player_data:
            data = player_data[user_id]
            team_pokemons = ', '.join([f"{p['name']} (Lv: {p['level']})" for p in data["team"]])
            box_count = len(data["box"])
            await ctx.send(f'{ctx.author.mention} のデータ: レベル: {data["level"]}, 経験値: {data["exp"]}, 手持ち: {team_pokemons}, ボックスにいるポケモンの数: {box_count}')
        else:
            await ctx.send(f'{ctx.author.mention} のデータは見つかりませんでした。')
    except Exception as e:
        logging.error(f"Error in player_data_command: {e}", exc_info=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def reset_player(ctx, member: discord.Member):
    try:
        user_id = str(member.id)
        if user_id in player_data:
            del player_data[user_id]
            save_player_data()
            await ctx.send(f'{member.mention} のプレイヤーデータをリセットしました。')
        else:
            await ctx.send(f'{member.mention} のプレイヤーデータは見つかりませんでした。')
    except Exception as e:
        logging.error(f"Error in reset_player command: {e}", exc_info=True)

@reset_player.error
async def reset_player_error(ctx, error):
    try:
        if isinstance(error, commands.CheckFailure):
            await ctx.send("このコマンドを使用するには管理者権限が必要です。")
    except Exception as e:
        logging.error(f"Error in reset_player_error: {e}", exc_info=True)

@bot.event
async def on_command_error(ctx, error):
    try:
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("有効なコマンドを入力してください。")
        else:
            print(f'Unhandled error: {error}')
            await ctx.send("エラーが発生しました。管理者に連絡してください。")
    except Exception as e:
        logging.error(f"Error in on_command_error: {e}", exc_info=True)

# 定期的にフィールドデータを保存するタスクを起動
async def periodic_save_field_data():
    try:
        while True:
            await asyncio.sleep(600)  # 10分ごとに保存
            save_field_data()
    except Exception as e:
        logging.error(f"Error in periodic_save_field_data: {e}", exc_info=True)

async def main():
    async with bot:
        Thread(target=run_flask).start()
        bot.loop.create_task(periodic_save_field_data())
        await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    asyncio.run(main())
