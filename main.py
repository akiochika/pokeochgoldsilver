import json
import os
import random
import discord
from discord.ext import commands
import asyncio
from datetime import timedelta
from discord.ext.commands import has_permissions, CheckFailure
import time

from skilllist import get_skill_damage  # 追加

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target=run)
t.start()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='p!', intents=intents)

# pokemonlist.pyからpokemon_listをインポート
from pokemonlist import pokemon_list

channel_data = {}
data_file = 'caught_pokemons.json'
player_data_file = 'player_data.json'
caught_pokemons = {}
player_data = {}

# データの読み込み
if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        caught_pokemons = json.load(file)

if os.path.exists(player_data_file):
    with open(player_data_file, 'r') as file:
        player_data = json.load(file)

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
spawn_threshold = 10  # ポケモンが出現するメッセージ数のしきい値

# 逃げる時間をレアリティに基づいて設定
rarity_to_timeout = {
    1: 60,
    2: 50,
    3: 30,
    4: 20,
    5: 7,
    6: 15
}

# ランクごとのレベル下限
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

# Call the fix_pokemon_level function after defining calculate_pokemon_level
fix_pokemon_level()

def calculate_capture_chance(pokemon, current_hp):
    base_chance = 100
    hp_factor = (current_hp / pokemon["max_hp"]) * 100
    rarity_penalty = pokemon["rarity"] * 10  # レアリティが高いほど捕まえにくい
    capture_chance = base_chance - hp_factor - rarity_penalty
    return max(capture_chance, 1)  # 確率は最低でも1%

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
            return rarity + 1  # Rarity is 1-indexed

def determine_shiny():
    return random.randint(1, 4096) == 1

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
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

        if channel_info["message_count"] >= spawn_threshold:  # しきい値を超えたらポケモンを出現
            await spawn_pokemon(message.channel, channel_info["user_ids"])
            channel_info["message_count"] = 0

    await bot.process_commands(message)

async def spawn_pokemon(channel, user_ids):
    channel_id = str(channel.id)
    channel_info = channel_data[channel_id]

    if channel_info["current_pokemon"] is not None:  # 既にポケモンが出現している場合は新たに出現させない
        return

    player_level = get_average_player_team_level(user_ids)
    spawn_rates = calculate_spawn_rates(player_level)
    chosen_rarity = choose_pokemon_by_rarity(spawn_rates)

    # 色違い判定
    shiny = determine_shiny()

    # 候補ポケモンを選定
    candidates = [pokemon for pokemon in pokemon_list if pokemon["rarity"] == chosen_rarity and (pokemon["shiny"] == shiny or not pokemon["shiny"]) and pokemon["appear"] == 0]
    if not candidates:
        candidates = [pokemon for pokemon in pokemon_list if pokemon["rarity"] == 1 and (pokemon["shiny"] == shiny or not pokemon["shiny"]) and pokemon["appear"] == 0]

    if not candidates:
        return

    channel_info["current_pokemon"] = random.choice(candidates)
    channel_info["current_pokemon"]["shiny"] = shiny  # Ensure shiny attribute is set correctly

    # プレイヤーがゲームを始めていない場合、レベル5以下のポケモンを出現させる
    if all(user_id not in player_data for user_id in user_ids):
        min_level, max_level = 1, 5
    else:
        min_level = rarity_level_min[channel_info["current_pokemon"]["rarity"]]
        max_level = min(player_level, 100)  # プレイヤーの平均レベル以下のポケモンを出現させる

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
    embed = discord.Embed(title=f"野生の{'' if channel_info['current_pokemon']['shiny'] else ''}{channel_info['current_pokemon']['name']}が現れた！ レベル: {channel_info['current_pokemon']['level']}")
    embed.set_image(url=channel_info["current_pokemon"]["image"])
    embed.add_field(name="HP", value=hp_bar, inline=False)
    channel_info["current_pokemon"]["message"] = await channel.send(embed=embed)

    # 既存のタスクがある場合はキャンセル
    if channel_info["wild_pokemon_escape_task"] and not channel_info["wild_pokemon_escape_task"].done():
        channel_info["wild_pokemon_escape_task"].cancel()

    # 新しい逃げるタスクを設定
    channel_info["wild_pokemon_escape_task"] = bot.loop.create_task(wild_pokemon_escape(channel))

async def wild_pokemon_escape(channel):
    channel_id = str(channel.id)
    channel_info = channel_data[channel_id]

    await asyncio.sleep(rarity_to_timeout[channel_info["current_pokemon"]["rarity"]])
    if channel_info["current_pokemon"]:
        await channel_info["current_pokemon"]["message"].delete()
        await channel.send(f"{channel_info['current_pokemon']['name']} は逃げてしまった！")
        channel_info["current_pokemon"] = None

        # 場にいるポケモンを手持ちに戻す
        for user_id in channel_info["user_ids"]:
            channel_info["field_pokemons"][user_id] = []
        save_player_data()

@bot.command()
async def start(ctx):
    user_id = str(ctx.author.id)
    if user_id not in player_data:
        player_data[user_id] = {"level": 1, "exp": 0, "team": [], "box": [], "field": []}
        save_player_data()
        await ctx.send(f'{ctx.author.mention} の冒険が始まった！ ポケモンを選んでください: !choose チコリータ, !choose ヒノアラシ, !choose ワニノコ')
    else:
        await ctx.send(f'{ctx.author.mention} は既に冒険を始めています。')

@bot.command()
async def choose(ctx, pokemon_name: str):
    user_id = str(ctx.author.id)
    if user_id in player_data and len(player_data[user_id]["team"]) == 0:
        # チコリータ、ヒノアラシ、ワニノコの選択肢を追加
        starter_pokemon = next((pokemon for pokemon in pokemon_list if pokemon["name"] == pokemon_name and not pokemon.get("shiny") and pokemon_name in ["チコリータ", "ヒノアラシ", "ワニノコ"]), None)
        if starter_pokemon:
            starter_pokemon = starter_pokemon.copy()
            starter_pokemon["level"] = 5
            starter_pokemon["exp"] = 0
            starter_pokemon.update(calculate_pokemon_level(starter_pokemon["base_stats"], starter_pokemon["level"]))
            starter_pokemon["max_hp"] = starter_pokemon["hp"]
            starter_pokemon["moves"] = ["たいあたり"]  # 初期技として「たいあたり」を追加
            player_data[user_id]["team"].append(starter_pokemon)
            save_player_data()
            await ctx.send(f'{ctx.author.mention} は {pokemon_name} を選びました！')
        else:
            await ctx.send(f'{pokemon_name} は選べません。')
    else:
        await ctx.send(f'{ctx.author.mention} は既にポケモンを持っています。')

def save_player_data():
    # `Message` オブジェクトを削除
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

    with open(player_data_file, 'w') as file:
        json.dump(player_data, file, ensure_ascii=False, indent=4)

# ポケモンリストの表示
# ページ情報を保持するための辞書
pages = {}

def create_embeds(pokemon_list):
    embeds = []
    for i in range(0, len(pokemon_list), 10): #1ページに10項目
        current_embed = discord.Embed(title="ポケモンリスト")
        for pokemon in pokemon_list[i:i+10]:
            current_embed.add_field(name=pokemon["name"], value=f"レアリティ: {pokemon['rarity']}, 進化レベル: {pokemon['evolve_level']}", inline=False)
        embeds.append(current_embed)
    return embeds

@bot.command()
async def show_pokemon(ctx):
    user_id = str(ctx.author.id)
    embeds = create_embeds(pokemon_list)
    if user_id not in pages:
        pages[user_id] = {"embeds": embeds, "current_page": 0}

    await ctx.send(embed=embeds[0])

@bot.command()
async def next_page(ctx):
    user_id = str(ctx.author.id)
    if user_id in pages and pages[user_id]["embeds"]:
        pages[user_id]["current_page"] += 1
        if pages[user_id]["current_page"] >= len(pages[user_id]["embeds"]):
            pages[user_id]["current_page"] = 0  # ループバックする
        await ctx.send(embed=pages[user_id]["embeds"][pages[user_id]["current_page"]])

@bot.command()
async def previous_page(ctx):
    user_id = str(ctx.author.id)
    if user_id in pages:
        pages[user_id]["current_page"] -= 1
        if pages[user_id]["current_page"] < 0:
            pages[user_id]["current_page"] = len(pages[user_id]["embeds"]) - 1  # ループバックする
        await ctx.send(embed=pages[user_id]["embeds"][pages[user_id]["current_page"]])

@bot.command()
async def box(ctx):
    user_id = str(ctx.author.id)
    if user_id in player_data and player_data[user_id]["box"]:
        box_pokemons = player_data[user_id]["box"]
        embeds = create_embeds(box_pokemons)
        if user_id not in pages:
            pages[user_id] = {"embeds": embeds, "current_page": 0}

        await ctx.send(embed=embeds[0])
    else:
        await ctx.send(f'{ctx.author.mention} のボックスにはポケモンがいません。')

@bot.command()
async def box_next(ctx):
    user_id = str(ctx.author.id)
    if user_id in pages and pages[user_id]["embeds"]:
        pages[user_id]["current_page"] += 1
        if pages[user_id]["current_page"] >= len(pages[user_id]["embeds"]):
            pages[user_id]["current_page"] = 0
        await ctx.send(embed=pages[user_id]["embeds"][pages[user_id]["current_page"]])

@bot.command()
async def box_back(ctx):
    user_id = str(ctx.author.id)
    if user_id in pages and pages[user_id]["embeds"]:
        pages[user_id]["current_page"] -= 1
        if pages[user_id]["current_page"] < 0:
            pages[user_id]["current_page"] = len(pages[user_id]["embeds"]) - 1
        await ctx.send(embed=pages[user_id]["embeds"][pages[user_id]["current_page"]])

# ボックスにポケモンを預けるコマンド
@bot.command()
async def deposit(ctx, pokemon_name: str):
    user_id = str(ctx.author.id)
    if user_id not in player_data:
        await ctx.send(f"{ctx.author.mention} あなたのデータが見つかりません。")
        return

    # 場にいるポケモンと手持ちポケモンを合わせて3匹以上か確認
    if len(player_data[user_id]["team"]) + len(player_data[user_id]["field"]) <= 1:
        await ctx.send(f"{ctx.author.mention} 手持ちと場にいるポケモンが少なすぎます。")
        return

    for i, pokemon in enumerate(player_data[user_id]["team"]):
        if pokemon["name"].lower() == pokemon_name.lower():
            player_data[user_id]["box"].append(pokemon)
            del player_data[user_id]["team"][i]
            save_player_data()
            await ctx.send(f"{ctx.author.mention} {pokemon_name} をボックスに預けました。")
            return

    await ctx.send(f"{ctx.author.mention} {pokemon_name} は手持ちにいません。")

# ボックスからポケモンを引き出すコマンド
@bot.command()
async def withdraw(ctx, pokemon_name: str):
    user_id = str(ctx.author.id)
    if user_id not in player_data:
        await ctx.send(f"{ctx.author.mention} あなたのデータが見つかりません。")
        return

    # 場にいるポケモンと手持ちポケモンを合わせて3匹以上か確認
    if len(player_data[user_id]["team"]) + len(player_data[user_id]["field"]) >= 3:
        await ctx.send(f"{ctx.author.mention} 手持ちと場にいるポケモンが多すぎます。")
        return

    possible_pokemons = [p for p in player_data[user_id]["box"] if p["name"].lower() == pokemon_name.lower()]
    if not possible_pokemons:
        await ctx.send(f"{ctx.author.mention} {pokemon_name} はボックスにいません。")
        return

    # 引き出すポケモンを選択する
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


async def auto_return_to_hand(user_id, channel_id, pokemon_name, delay):
    await asyncio.sleep(delay)
    if user_id in player_data and channel_id in channel_data:
        field = channel_data[channel_id]["field_pokemons"].get(user_id, [])
        pokemon = next((p for p in field if p["name"].lower() == pokemon_name.lower()), None)
        if pokemon and not any(channel_info.get("current_pokemon") for channel_info in channel_data.values()):  # 他のチャンネルにポケモンがフィールドにいない場合のみ手持ちに戻す
            field.remove(pokemon)
            save_player_data()
            member = bot.get_user(int(user_id))
            if member:
                await member.send(f'{pokemon_name} がフィールドに出続けたので自動的に手持ちに戻りました。')

@bot.command()
async def go(ctx, pokemon_name: str):
    user_id = str(ctx.author.id)
    channel_id = str(ctx.channel.id)

    if user_id in player_data:
        team = player_data[user_id]["team"]
        field = channel_data[channel_id]["field_pokemons"].get(user_id, [])

        # プレイヤーが既にポケモンを出しているか確認
        if any(p["name"].lower() == pokemon_name.lower() for p in field):
            await ctx.send(f"{ctx.author.mention} は既に {pokemon_name} を出しています。")
            return

        if len(field) >= 1:
            await ctx.send(f"{ctx.author.mention} は既に他のポケモンを出しています。")
            return

        pokemon = next((p for p in team if p["name"].lower() == pokemon_name.lower()), None)

        if pokemon:
            field.append(pokemon)
            channel_data[channel_id]["field_pokemons"][user_id] = field
            skills = ', '.join(pokemon.get("moves", ["なし"]))  # ポケモンの技を表示
            hp_bar = create_hp_bar(pokemon["hp"], pokemon["max_hp"])
            embed = discord.Embed(title=f"{ctx.author.name} の {pokemon['name']} (Lv: {pokemon['level']})")
            embed.set_image(url=pokemon["image"])
            embed.add_field(name="HP", value=hp_bar, inline=False)
            embed.add_field(name="技", value=skills, inline=False)  # 技を表示
            msg = await ctx.send(embed=embed)
            await msg.delete(delay=300)
            bot.loop.create_task(auto_return_to_hand(user_id, channel_id, pokemon_name, 100))  # 100秒後に自動で手持ちに戻すタスクを作成
        else:
            await ctx.send(f"{pokemon_name} は手持ちにいません。")

@bot.command()
async def return_pokemon(ctx, pokemon_name: str):
    user_id = str(ctx.author.id)
    channel_id = str(ctx.channel.id)

    if user_id in player_data and channel_id in channel_data:
        field = channel_data[channel_id]["field_pokemons"].get(user_id, [])
        pokemon = next((p for p in field if p["name"].lower() == pokemon_name.lower()), None)
        if pokemon:
            field.remove(pokemon)
            await ctx.send(f"{pokemon['name']} を手持ちに戻しました。")

@bot.command()
async def rename(ctx, old_name: str, new_name: str):
    user_id = str(ctx.author.id)
    if user_id in player_data:
        team = player_data[user_id]["team"]
        pokemon = next((p for p in team if p["name"].lower() == old_name.lower()), None)
        if pokemon:
            pokemon["name"] = new_name
            await ctx.send(f"{old_name} の名前を {new_name} に変更しました。")

@bot.command()
async def skill(ctx, skill_name: str, target_name: str = None):
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
                    await channel_info["current_pokemon"]["message"].delete()  # メッセージを削除
                except discord.errors.NotFound:
                    pass  # メッセージが見つからなかった場合は無視
            await ctx.send(f"{channel_info['current_pokemon']['name']} は倒れた！")
            await give_exp_on_defeat(ctx, channel_info["current_pokemon"]["level"])  # ポケモンを倒したときの経験値付与
            channel_info["current_pokemon"] = None

            # 場にいるポケモンを手持ちに戻す
            for user_id in channel_info["user_ids"]:
                channel_info["field_pokemons"][user_id] = []
            save_player_data()
        else:
            if channel_info["current_pokemon"]["message"]:
                try:
                    await channel_info["current_pokemon"]["message"].delete()  # メッセージを削除
                except discord.errors.NotFound:
                    pass  # メッセージが見つからなかった場合は無視
            embed = discord.Embed(title=f"野生の{channel_info['current_pokemon']['name']}")
            embed.set_image(url=channel_info["current_pokemon"]["image"])
            embed.add_field(name="HP", value=hp_bar, inline=False)
            channel_info["current_pokemon"]["message"] = await ctx.send(embed=embed)
    else:
        await ctx.send(f"{target_name} はフィールドにいません。")

@bot.command()
@commands.has_permissions(administrator=True)
async def all_data_reset(ctx):
    global caught_pokemons, player_data

    # 全プレイヤーのデータを初期化
    caught_pokemons = {}
    player_data = {}

    # データファイルを初期化
    with open(data_file, 'w') as file:
        json.dump(caught_pokemons, file, ensure_ascii=False, indent=4)

    with open(player_data_file, 'w') as file:
        json.dump(player_data, file, ensure_ascii=False, indent=4)

    await ctx.send("全プレイヤーのデータを初期化しました。")

# 経験値を計算する関数（改良版）
def calculate_exp(level, rarity):
    base_exp = 10 * (level ** 1.5)
    rarity_multiplier = 1 + 0.2 * (rarity - 1)  # レアリティに基づいて経験値倍率を増加
    return int(base_exp * rarity_multiplier)

# ポケモンを倒したときの経験値付与
async def give_exp(user_id, exp):
    if user_id in player_data:
        player_data[user_id]["exp"] += exp
        await check_level_up(user_id)
        save_player_data()

# レベルアップをチェックする関数（改良版）
async def check_level_up(user_id):
    while player_data[user_id]["exp"] >= calculate_exp(player_data[user_id]["level"], 1):  # レアリティ1の基準でレベルアップ
        player_data[user_id]["exp"] -= calculate_exp(player_data[user_id]["level"], 1)
        player_data[user_id]["level"] += 1
        if player_data[user_id]["level"] > 100:
            player_data[user_id]["level"] = 100
            player_data[user_id]["exp"] = 0

        # チーム内のポケモンのレベルをアップデート
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

# 捕獲成功時の経験値付与（改良版）
async def give_exp_on_catch(ctx, pokemon_level):
    exp = calculate_exp(pokemon_level, 1)  # レアリティ1の基準で経験値付与
    for user_id in channel_data[str(ctx.channel.id)]["user_ids"]:
        if channel_data[str(ctx.channel.id)]["field_pokemons"].get(user_id, []):
            await give_exp(user_id, exp)
            member = ctx.guild.get_member(int(user_id))
            if member:
                await ctx.send(f'{member.mention} が {exp} の経験値を獲得しました！')

# ポケモンを倒したときの経験値付与（改良版）
async def give_exp_on_defeat(ctx, pokemon_level):
    exp = calculate_exp(pokemon_level, 1)  # レアリティ1の基準で経験値付与
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

# ポケモンが進化するかチェックする関数
async def check_evolution(ctx, user_id, pokemon):
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

@bot.command()
async def catch(ctx, pokemon_name: str):
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
            current_pokemon_copy["shiny"] = channel_info["current_pokemon"]["shiny"]  # 保持する
            if len(player_data[user_id]["team"]) < 3:
                player_data[user_id]["team"].append(current_pokemon_copy)
            else:
                player_data[user_id]["box"].append(current_pokemon_copy)
            caught_pokemons[user_id].append(current_pokemon_copy)

            # JSONに保存する前にコピーからMessageオブジェクトを削除
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

            await channel_info["current_pokemon"]["message"].delete()  # メッセージを削除
            await ctx.send(f'{ctx.author.mention} が {"" if channel_info["current_pokemon"]["shiny"] else ""}{channel_info["current_pokemon"]["name"]} を捕まえた！')
            if channel_info["current_pokemon"]:
                await give_exp_on_catch(ctx, channel_info["current_pokemon"]["level"])
            channel_info["current_pokemon"] = None
            if channel_info["wild_pokemon_escape_task"] and not channel_info["wild_pokemon_escape_task"].done():
                channel_info["wild_pokemon_escape_task"].cancel()

            # 場にいるポケモンを手持ちに戻す
            for user_id in channel_info["user_ids"]:
                channel_info["field_pokemons"][user_id] = []
            save_player_data()
        else:
            msg = await ctx.send(f'{ctx.author.mention} が {channel_info["current_pokemon"]["name"]} を捕まえ損ねた！')
            await msg.delete(delay=5)
    else:
        await ctx.send(f'{pokemon_name} はここにいない！')

@bot.command()
@has_permissions(administrator=True)
async def reset(ctx, member: discord.Member):
    user_id = str(member.id)
    if user_id in caught_pokemons:
        del caught_pokemons[user_id]

        with open(data_file, 'w') as file:
            json.dump(caught_pokemons, file, ensure_ascii=False, indent=4)

        await ctx.send(f'{member.mention} の所持ポケモンをリセットしました。')
    else:
        await ctx.send(f'{member.mention} はまだポケモンを捕まえていません。')

@reset.error
async def reset_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.send("このコマンドを使用するには管理者権限が必要です。")

@bot.command()
@has_permissions(administrator=True)
async def spawn(ctx):
    await spawn_pokemon(ctx.channel, [str(ctx.author.id)])

@spawn.error
async def spawn_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.send("このコマンドを使用するには管理者権限が必要です。")

@bot.command()
async def inventory(ctx):
    user_id = str(ctx.author.id)
    if user_id in caught_pokemons and caught_pokemons[user_id]:
        pokemons = ', '.join([p["name"] for p in caught_pokemons[user_id]])
        await ctx.send(f'{ctx.author.mention} が捕まえたポケモン: {pokemons}')
    else:
        await ctx.send(f'{ctx.author.mention} はまだポケモンを捕まえていません。')

@bot.command()
async def player_data_command(ctx):
    user_id = str(ctx.author.id)
    if user_id in player_data:
        data = player_data[user_id]
        team_pokemons = ', '.join([f"{p['name']} (Lv: {p['level']})" for p in data["team"]])
        box_count = len(data["box"])
        await ctx.send(f'{ctx.author.mention} のデータ: レベル: {data["level"]}, 経験値: {data["exp"]}, 手持ち: {team_pokemons}, ボックスにいるポケモンの数: {box_count}')
    else:
        await ctx.send(f'{ctx.author.mention} のデータは見つかりませんでした。')

@bot.command()
@has_permissions(administrator=True)
async def reset_player(ctx, member: discord.Member):
    user_id = str(member.id)
    if user_id in player_data:
        del player_data[user_id]
        save_player_data()
        await ctx.send(f'{member.mention} のプレイヤーデータをリセットしました。')
    else:
        await ctx.send(f'{member.mention} のプレイヤーデータは見つかりませんでした。')

@reset_player.error
async def reset_player_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.send("このコマンドを使用するには管理者権限が必要です。")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("有効なコマンドを入力してください。")
    else:
        raise error

# 必要なモジュールのインポート
import asyncio

# 交換提案を保存する辞書
pending_trades = {}

# 交換提案コマンド
@bot.command()
async def propose_trade(ctx, target_member: discord.Member, offer_pokemon_name: str, request_pokemon_name: str):
    proposer_id = str(ctx.author.id)
    target_id = str(target_member.id)

    # 提案者と対象者の両方がプレイヤーデータに存在するか確認
    if proposer_id not in player_data:
        await ctx.send(f"{ctx.author.mention} はプレイヤーデータがありません。")
        return

    if target_id not in player_data:
        await ctx.send(f"{target_member.mention} はプレイヤーデータがありません。")
        return

    # 提案者が交換したいポケモンを持っているか確認
    proposer_pokemon = next((p for p in player_data[proposer_id]["team"] if p["name"].lower() == offer_pokemon_name.lower()), None)
    if not proposer_pokemon:
        await ctx.send(f"{ctx.author.mention} は {offer_pokemon_name} を持っていません。")
        return

    # 対象者が提案者が欲しいポケモンを持っているか確認
    target_pokemon = next((p for p in player_data[target_id]["team"] if p["name"].lower() == request_pokemon_name.lower()), None)
    if not target_pokemon:
        await ctx.send(f"{target_member.mention} は {request_pokemon_name} を持っていません。")
        return

    # 交換提案
    await ctx.send(f"{target_member.mention}, {ctx.author.mention} は {offer_pokemon_name} と {request_pokemon_name} の交換を提案しました。 `!accept_trade` または `!decline_trade` を入力してください。")

    # 交換提案を保存して、応答を追跡
    pending_trades[(proposer_id, target_id)] = (proposer_pokemon, target_pokemon)

# 交換受け入れコマンド
@bot.command()
async def accept_trade(ctx):
    target_id = str(ctx.author.id)
    proposer_id = next((key[0] for key in pending_trades if key[1] == target_id), None)

    if not proposer_id:
        await ctx.send(f"{ctx.author.mention} は交換提案がありません。")
        return

    # 交換実行
    proposer_pokemon, target_pokemon = pending_trades.pop((proposer_id, target_id))
    player_data[proposer_id]["team"].remove(proposer_pokemon)
    player_data[target_id]["team"].remove(target_pokemon)

    player_data[proposer_id]["team"].append(target_pokemon)
    player_data[target_id]["team"].append(proposer_pokemon)

    save_player_data()
    await ctx.send(f"{ctx.author.mention} と {bot.get_user(int(proposer_id)).mention} の交換が成立しました。")

# 交換拒否コマンド
@bot.command()
async def decline_trade(ctx):
    target_id = str(ctx.author.id)
    proposer_id = next((key[0] for key in pending_trades if key[1] == target_id), None)

    if not proposer_id:
        await ctx.send(f"{ctx.author.mention} は交換提案がありません。")
        return

    # 保留中の交換提案を削除
    pending_trades.pop((proposer_id, target_id))
    await ctx.send(f"{ctx.author.mention} は交換を辞退しました。")


# 最後に bot を実行
my_secret = os.environ['DISCORD_TOKEN']
bot.run(my_secret)
