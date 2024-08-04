pokemon_list = [
    {"name": "フシギダネ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png", "base_stats": {'HP': 45, '攻撃': 49, '防御': 49, '特攻': 65, '特防': 65, '素早さ': 45}, "rarity": 1, "evolve_level": 16, "evolves_to": "フシギソウ", "appear": 1, "moves": ["たいあたり", "つるのムチ"], "shiny": False},
    {"name": "フシギダネ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png", "base_stats": {'HP': 45, '攻撃': 49, '防御': 49, '特攻': 65, '特防': 65, '素早さ': 45}, "rarity": 1, "evolve_level": 16, "evolves_to": "フシギソウ", "appear": 1, "moves": ["たいあたり", "つるのムチ"], "shiny": True},
    {"name": "フシギソウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png", "base_stats": {'HP': 60, '攻撃': 62, '防御': 63, '特攻': 80, '特防': 80, '素早さ': 60}, "rarity": 2, "evolve_level": 32, "evolves_to": "フシギバナ", "appear": 1, "moves": ["つるのムチ", "はっぱカッター"], "shiny": False},
    {"name": "フシギソウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/2.png", "base_stats": {'HP': 60, '攻撃': 62, '防御': 63, '特攻': 80, '特防': 80, '素早さ': 60}, "rarity": 2, "evolve_level": 32, "evolves_to": "フシギバナ", "appear": 1, "moves": ["つるのムチ", "はっぱカッター"], "shiny": True},
    {"name": "フシギバナ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png", "base_stats": {'HP': 80, '攻撃': 82, '防御': 83, '特攻': 100, '特防': 100, '素早さ': 80}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["どくどく", "ソーラービーム"], "shiny": False},
    {"name": "フシギバナ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/3.png", "base_stats": {'HP': 80, '攻撃': 82, '防御': 83, '特攻': 100, '特防': 100, '素早さ': 80}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["どくどく", "ソーラービーム"], "shiny": True},
    {"name": "ヒトカゲ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png", "base_stats": {'HP': 39, '攻撃': 52, '防御': 43, '特攻': 60, '特防': 50, '素早さ': 65}, "rarity": 1, "evolve_level": 16, "evolves_to": "リザード", "appear": 1, "moves": ["ひっかく", "ひのこ"], "shiny": False},
    {"name": "ヒトカゲ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/4.png", "base_stats": {'HP': 39, '攻撃': 52, '防御': 43, '特攻': 60, '特防': 50, '素早さ': 65}, "rarity": 1, "evolve_level": 16, "evolves_to": "リザード", "appear": 1, "moves": ["ひっかく", "ひのこ"], "shiny": True},
    {"name": "リザード", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png", "base_stats": {'HP': 58, '攻撃': 64, '防御': 58, '特攻': 80, '特防': 65, '素早さ': 80}, "rarity": 2, "evolve_level": 36, "evolves_to": "リザードン", "appear": 1, "moves": ["ひのこ", "かえんほうしゃ"], "shiny": False},
    {"name": "リザード", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/5.png", "base_stats": {'HP': 58, '攻撃': 64, '防御': 58, '特攻': 80, '特防': 65, '素早さ': 80}, "rarity": 2, "evolve_level": 36, "evolves_to": "リザードン", "appear": 1, "moves": ["ひのこ", "かえんほうしゃ"], "shiny": True},
    {"name": "リザードン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png", "base_stats": {'HP': 78, '攻撃': 84, '防御': 78, '特攻': 109, '特防': 85, '素早さ': 100}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["エアスラッシュ", "だいもんじ"], "shiny": False},
    {"name": "リザードン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/6.png", "base_stats": {'HP': 78, '攻撃': 84, '防御': 78, '特攻': 109, '特防': 85, '素早さ': 100}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["エアスラッシュ", "だいもんじ"], "shiny": True},
    {"name": "ゼニガメ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png", "base_stats": {'HP': 44, '攻撃': 48, '防御': 65, '特攻': 50, '特防': 64, '素早さ': 43}, "rarity": 1, "evolve_level": 16, "evolves_to": "カメール", "appear": 1, "moves": ["たいあたり", "みずでっぽう"], "shiny": False},
    {"name": "ゼニガメ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/7.png", "base_stats": {'HP': 44, '攻撃': 48, '防御': 65, '特攻': 50, '特防': 64, '素早さ': 43}, "rarity": 1, "evolve_level": 16, "evolves_to": "カメール", "appear": 1, "moves": ["たいあたり", "みずでっぽう"], "shiny": True},
    {"name": "カメール", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/8.png", "base_stats": {'HP': 59, '攻撃': 63, '防御': 80, '特攻': 65, '特防': 80, '素早さ': 58}, "rarity": 2, "evolve_level": 36, "evolves_to": "カメックス", "appear": 1, "moves": ["みずでっぽう", "とっしん"], "shiny": False},
    {"name": "カメール", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/8.png", "base_stats": {'HP': 59, '攻撃': 63, '防御': 80, '特攻': 65, '特防': 80, '素早さ': 58}, "rarity": 2, "evolve_level": 36, "evolves_to": "カメックス", "appear": 1, "moves": ["みずでっぽう", "とっしん"], "shiny": True},
    {"name": "カメックス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png", "base_stats": {'HP': 79, '攻撃': 83, '防御': 100, '特攻': 85, '特防': 105, '素早さ': 78}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["れいとうビーム", "ハイドロポンプ"], "shiny": False},
    {"name": "カメックス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/9.png", "base_stats": {'HP': 79, '攻撃': 83, '防御': 100, '特攻': 85, '特防': 105, '素早さ': 78}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["れいとうビーム", "ハイドロポンプ"], "shiny": True},
    {"name": "キャタピー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10.png", "base_stats": {'HP': 45, '攻撃': 30, '防御': 35, '特攻': 20, '特防': 20, '素早さ': 45}, "rarity": 1, "evolve_level": 7, "evolves_to": "トランセル", "appear": 0, "moves": ["たいあたり"], "shiny": False},
    {"name": "キャタピー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/10.png", "base_stats": {'HP': 45, '攻撃': 30, '防御': 35, '特攻': 20, '特防': 20, '素早さ': 45}, "rarity": 1, "evolve_level": 7, "evolves_to": "トランセル", "appear": 0, "moves": ["たいあたり"], "shiny": True},
    {"name": "トランセル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/11.png", "base_stats": {'HP': 50, '攻撃': 20, '防御': 55, '特攻': 25, '特防': 25, '素早さ': 30}, "rarity": 1, "evolve_level": 10, "evolves_to": "バタフリー", "appear": 0, "moves": ["かたくなる"], "shiny": False},
    {"name": "トランセル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/11.png", "base_stats": {'HP': 50, '攻撃': 20, '防御': 55, '特攻': 25, '特防': 25, '素早さ': 30}, "rarity": 1, "evolve_level": 10, "evolves_to": "バタフリー", "appear": 0, "moves": ["かたくなる"], "shiny": True},
    {"name": "バタフリー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/12.png", "base_stats": {'HP': 60, '攻撃': 45, '防御': 50, '特攻': 90, '特防': 80, '素早さ': 70}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "むしのさざめき"], "shiny": False},
    {"name": "バタフリー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/12.png", "base_stats": {'HP': 60, '攻撃': 45, '防御': 50, '特攻': 90, '特防': 80, '素早さ': 70}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "むしのさざめき"], "shiny": True},
    {"name": "ビードル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/13.png", "base_stats": {'HP': 40, '攻撃': 35, '防御': 30, '特攻': 20, '特防': 20, '素早さ': 50}, "rarity": 1, "evolve_level": 7, "evolves_to": "コクーン", "appear": 0, "moves": ["どくばり"], "shiny": False},
    {"name": "ビードル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/13.png", "base_stats": {'HP': 40, '攻撃': 35, '防御': 30, '特攻': 20, '特防': 20, '素早さ': 50}, "rarity": 1, "evolve_level": 7, "evolves_to": "コクーン", "appear": 0, "moves": ["どくばり"], "shiny": True},
    {"name": "コクーン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/14.png", "base_stats": {'HP': 45, '攻撃': 25, '防御': 50, '特攻': 25, '特防': 25, '素早さ': 35}, "rarity": 1, "evolve_level": 10, "evolves_to": "スピアー", "appear": 0, "moves": ["かたくなる"], "shiny": False},
    {"name": "コクーン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/14.png", "base_stats": {'HP': 45, '攻撃': 25, '防御': 50, '特攻': 25, '特防': 25, '素早さ': 35}, "rarity": 1, "evolve_level": 10, "evolves_to": "スピアー", "appear": 0, "moves": ["かたくなる"], "shiny": True},
    {"name": "スピアー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/15.png", "base_stats": {'HP': 65, '攻撃': 90, '防御': 40, '特攻': 45, '特防': 80, '素早さ': 75}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "ダブルニードル"], "shiny": False},
    {"name": "スピアー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/15.png", "base_stats": {'HP': 65, '攻撃': 90, '防御': 40, '特攻': 45, '特防': 80, '素早さ': 75}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "ダブルニードル"], "shiny": True},
    {"name": "ポッポ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/16.png", "base_stats": {'HP': 40, '攻撃': 45, '防御': 40, '特攻': 35, '特防': 35, '素早さ': 56}, "rarity": 1, "evolve_level": 18, "evolves_to": "ピジョン", "appear": 0, "moves": ["たいあたり", "つつく"], "shiny": False},
    {"name": "ポッポ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/16.png", "base_stats": {'HP': 40, '攻撃': 45, '防御': 40, '特攻': 35, '特防': 35, '素早さ': 56}, "rarity": 1, "evolve_level": 18, "evolves_to": "ピジョン", "appear": 0, "moves": ["たいあたり", "つつく"], "shiny": True},
    {"name": "ピジョン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png", "base_stats": {'HP': 63, '攻撃': 60, '防御': 55, '特攻': 50, '特防': 50, '素早さ': 71}, "rarity": 2, "evolve_level": 36, "evolves_to": "ピジョット", "appear": 0, "moves": ["つつく", "かぜおこし"], "shiny": False},
    {"name": "ピジョン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/17.png", "base_stats": {'HP': 63, '攻撃': 60, '防御': 55, '特攻': 50, '特防': 50, '素早さ': 71}, "rarity": 2, "evolve_level": 36, "evolves_to": "ピジョット", "appear": 0, "moves": ["つつく", "かぜおこし"], "shiny": True},
    {"name": "ピジョット", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/18.png", "base_stats": {'HP': 83, '攻撃': 80, '防御': 75, '特攻': 70, '特防': 70, '素早さ': 101}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["つばさでうつ", "そらをとぶ"], "shiny": False},
    {"name": "ピジョット", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/18.png", "base_stats": {'HP': 83, '攻撃': 80, '防御': 75, '特攻': 70, '特防': 70, '素早さ': 101}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["つばさでうつ", "そらをとぶ"], "shiny": True},
    {"name": "コラッタ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/19.png", "base_stats": {'HP': 30, '攻撃': 56, '防御': 35, '特攻': 25, '特防': 35, '素早さ': 72}, "rarity": 1, "evolve_level": 20, "evolves_to": "ラッタ", "appear": 0, "moves": ["たいあたり", "ひっかく"], "shiny": False},
    {"name": "コラッタ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/19.png", "base_stats": {'HP': 30, '攻撃': 56, '防御': 35, '特攻': 25, '特防': 35, '素早さ': 72}, "rarity": 1, "evolve_level": 20, "evolves_to": "ラッタ", "appear": 0, "moves": ["たいあたり", "ひっかく"], "shiny": True},
    {"name": "ラッタ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/20.png", "base_stats": {'HP': 55, '攻撃': 81, '防御': 60, '特攻': 50, '特防': 70, '素早さ': 97}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ひっさつまえば", "かみつく"], "shiny": False},
    {"name": "ラッタ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/20.png", "base_stats": {'HP': 55, '攻撃': 81, '防御': 60, '特攻': 50, '特防': 70, '素早さ': 97}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ひっさつまえば", "かみつく"], "shiny": True},
    {"name": "オニスズメ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/21.png", "base_stats": {'HP': 40, '攻撃': 60, '防御': 30, '特攻': 31, '特防': 31, '素早さ': 70}, "rarity": 1, "evolve_level": 20, "evolves_to": "オニドリル", "appear": 0, "moves": ["つつく", "かぜおこし"], "shiny": False},
    {"name": "オニスズメ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/21.png", "base_stats": {'HP': 40, '攻撃': 60, '防御': 30, '特攻': 31, '特防': 31, '素早さ': 70}, "rarity": 1, "evolve_level": 20, "evolves_to": "オニドリル", "appear": 0, "moves": ["つつく", "かぜおこし"], "shiny": True},
    {"name": "オニドリル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/22.png", "base_stats": {'HP': 65, '攻撃': 90, '防御': 65, '特攻': 61, '特防': 61, '素早さ': 100}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ドリルくちばし", "とっしん"], "shiny": False},
    {"name": "オニドリル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/22.png", "base_stats": {'HP': 65, '攻撃': 90, '防御': 65, '特攻': 61, '特防': 61, '素早さ': 100}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ドリルくちばし", "とっしん"], "shiny": True},
    {"name": "アーボ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png", "base_stats": {'HP': 35, '攻撃': 60, '防御': 44, '特攻': 40, '特防': 54, '素早さ': 55}, "rarity": 1, "evolve_level": 22, "evolves_to": "アーボック", "appear": 0, "moves": ["どくばり", "かみつく"], "shiny": False},
    {"name": "アーボ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/23.png", "base_stats": {'HP': 35, '攻撃': 60, '防御': 44, '特攻': 40, '特防': 54, '素早さ': 55}, "rarity": 1, "evolve_level": 22, "evolves_to": "アーボック", "appear": 0, "moves": ["どくばり", "かみつく"], "shiny": True},
    {"name": "アーボック", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/24.png", "base_stats": {'HP': 60, '攻撃': 95, '防御': 69, '特攻': 65, '特防': 79, '素早さ': 80}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かみくだく", "どくづき"], "shiny": False},
    {"name": "アーボック", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/24.png", "base_stats": {'HP': 60, '攻撃': 95, '防御': 69, '特攻': 65, '特防': 79, '素早さ': 80}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かみくだく", "どくづき"], "shiny": True},
    {"name": "ピカチュウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png", "base_stats": {'HP': 35, '攻撃': 55, '防御': 40, '特攻': 50, '特防': 50, '素早さ': 90}, "rarity": 1, "evolve_level": None, "evolves_to": "ライチュウ", "appear": 0, "moves": ["でんきショック", "スピードスター"], "shiny": False},
    {"name": "ピカチュウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png", "base_stats": {'HP': 35, '攻撃': 55, '防御': 40, '特攻': 50, '特防': 50, '素早さ': 90}, "rarity": 1, "evolve_level": None, "evolves_to": "ライチュウ", "appear": 0, "moves": ["でんきショック", "スピードスター"], "shiny": True},
    {"name": "ライチュウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png", "base_stats": {'HP': 60, '攻撃': 90, '防御': 55, '特攻': 90, '特防': 80, '素早さ': 110}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かみなりパンチ", "10まんボルト"], "shiny": False},
    {"name": "ライチュウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/26.png", "base_stats": {'HP': 60, '攻撃': 90, '防御': 55, '特攻': 90, '特防': 80, '素早さ': 110}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かみなりパンチ", "10まんボルト"], "shiny": True},
    {"name": "サンド", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/27.png", "base_stats": {'HP': 50, '攻撃': 75, '防御': 85, '特攻': 20, '特防': 30, '素早さ': 40}, "rarity": 1, "evolve_level": 22, "evolves_to": "サンドパン", "appear": 0, "moves": ["ひっかく", "あなをほる"], "shiny": False},
    {"name": "サンド", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/27.png", "base_stats": {'HP': 50, '攻撃': 75, '防御': 85, '特攻': 20, '特防': 30, '素早さ': 40}, "rarity": 1, "evolve_level": 22, "evolves_to": "サンドパン", "appear": 0, "moves": ["ひっかく", "あなをほる"], "shiny": True},
    {"name": "サンドパン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/28.png", "base_stats": {'HP': 75, '攻撃': 100, '防御': 110, '特攻': 45, '特防': 55, '素早さ': 65}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["すなあらし", "じしん"], "shiny": False},
    {"name": "サンドパン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/28.png", "base_stats": {'HP': 75, '攻撃': 100, '防御': 110, '特攻': 45, '特防': 55, '素早さ': 65}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["すなあらし", "じしん"], "shiny": True},
    {"name": "ニドラン♀", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/29.png", "base_stats": {'HP': 55, '攻撃': 47, '防御': 52, '特攻': 40, '特防': 40, '素早さ': 41}, "rarity": 1, "evolve_level": 16, "evolves_to": "ニドリーナ", "appear": 0, "moves": ["どくばり", "たいあたり"], "shiny": False},
    {"name": "ニドラン♀", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/29.png", "base_stats": {'HP': 55, '攻撃': 47, '防御': 52, '特攻': 40, '特防': 40, '素早さ': 41}, "rarity": 1, "evolve_level": 16, "evolves_to": "ニドリーナ", "appear": 0, "moves": ["どくばり", "たいあたり"], "shiny": True},
    {"name": "ニドリーナ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png", "base_stats": {'HP': 70, '攻撃': 62, '防御': 67, '特攻': 55, '特防': 55, '素早さ': 56}, "rarity": 2, "evolve_level": 36, "evolves_to": "ニドクイン", "appear": 0, "moves": ["かみなりパンチ", "どくづき"], "shiny": False},
    {"name": "ニドリーナ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/30.png", "base_stats": {'HP': 70, '攻撃': 62, '防御': 67, '特攻': 55, '特防': 55, '素早さ': 56}, "rarity": 2, "evolve_level": 36, "evolves_to": "ニドクイン", "appear": 0, "moves": ["かみなりパンチ", "どくづき"], "shiny": True},
    {"name": "ニドクイン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/31.png", "base_stats": {'HP': 90, '攻撃': 92, '防御': 87, '特攻': 75, '特防': 85, '素早さ': 76}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["どくばり", "じしん"], "shiny": False},
    {"name": "ニドクイン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/31.png", "base_stats": {'HP': 90, '攻撃': 92, '防御': 87, '特攻': 75, '特防': 85, '素早さ': 76}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["どくばり", "じしん"], "shiny": True},
    {"name": "ニドラン♂", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/32.png", "base_stats": {'HP': 46, '攻撃': 57, '防御': 40, '特攻': 40, '特防': 40, '素早さ': 50}, "rarity": 1, "evolve_level": 16, "evolves_to": "ニドリーノ", "appear": 0, "moves": ["どくばり", "たいあたり"], "shiny": False},
    {"name": "ニドラン♂", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/32.png", "base_stats": {'HP': 46, '攻撃': 57, '防御': 40, '特攻': 40, '特防': 40, '素早さ': 50}, "rarity": 1, "evolve_level": 16, "evolves_to": "ニドリーノ", "appear": 0, "moves": ["どくばり", "たいあたり"], "shiny": True},
    {"name": "ニドリーノ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/33.png", "base_stats": {'HP': 61, '攻撃': 72, '防御': 57, '特攻': 55, '特防': 55, '素早さ': 65}, "rarity": 2, "evolve_level": 36, "evolves_to": "ニドキング", "appear": 0, "moves": ["かみなりパンチ", "どくづき"], "shiny": False},
    {"name": "ニドリーノ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/33.png", "base_stats": {'HP': 61, '攻撃': 72, '防御': 57, '特攻': 55, '特防': 55, '素早さ': 65}, "rarity": 2, "evolve_level": 36, "evolves_to": "ニドキング", "appear": 0, "moves": ["かみなりパンチ", "どくづき"], "shiny": True},
    {"name": "ニドキング", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/34.png", "base_stats": {'HP': 81, '攻撃': 102, '防御': 77, '特攻': 85, '特防': 75, '素早さ': 85}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["どくばり", "じしん"], "shiny": False},
    {"name": "ニドキング", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/34.png", "base_stats": {'HP': 81, '攻撃': 102, '防御': 77, '特攻': 85, '特防': 75, '素早さ': 85}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["どくばり", "じしん"], "shiny": True},
    {"name": "ピッピ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png", "base_stats": {'HP': 70, '攻撃': 45, '防御': 48, '特攻': 60, '特防': 65, '素早さ': 35}, "rarity": 1, "evolve_level": None, "evolves_to": "ピクシー", "appear": 0, "moves": ["うたう", "メロメロ"], "shiny": False},
    {"name": "ピッピ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/35.png", "base_stats": {'HP': 70, '攻撃': 45, '防御': 48, '特攻': 60, '特防': 65, '素早さ': 35}, "rarity": 1, "evolve_level": None, "evolves_to": "ピクシー", "appear": 0, "moves": ["うたう", "メロメロ"], "shiny": True},
    {"name": "ピクシー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png", "base_stats": {'HP': 95, '攻撃': 70, '防御': 73, '特攻': 95, '特防': 90, '素早さ': 60}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ゆびをふる", "メロメロ"], "shiny": False},
    {"name": "ピクシー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/36.png", "base_stats": {'HP': 95, '攻撃': 70, '防御': 73, '特攻': 95, '特防': 90, '素早さ': 60}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ゆびをふる", "メロメロ"], "shiny": True},
    {"name": "ロコン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/37.png", "base_stats": {'HP': 38, '攻撃': 41, '防御': 40, '特攻': 50, '特防': 65, '素早さ': 65}, "rarity": 1, "evolve_level": None, "evolves_to": "キュウコン", "appear": 0, "moves": ["ひのこ", "かえんほうしゃ"], "shiny": False},
    {"name": "ロコン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/37.png", "base_stats": {'HP': 38, '攻撃': 41, '防御': 40, '特攻': 50, '特防': 65, '素早さ': 65}, "rarity": 1, "evolve_level": None, "evolves_to": "キュウコン", "appear": 0, "moves": ["ひのこ", "かえんほうしゃ"], "shiny": True},
    {"name": "キュウコン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png", "base_stats": {'HP': 73, '攻撃': 76, '防御': 75, '特攻': 81, '特防': 100, '素早さ': 100}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かえんほうしゃ", "だいもんじ"], "shiny": False},
    {"name": "キュウコン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/38.png", "base_stats": {'HP': 73, '攻撃': 76, '防御': 75, '特攻': 81, '特防': 100, '素早さ': 100}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かえんほうしゃ", "だいもんじ"], "shiny": True},
    {"name": "プリン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png", "base_stats": {'HP': 115, '攻撃': 45, '防御': 20, '特攻': 45, '特防': 25, '素早さ': 20}, "rarity": 1, "evolve_level": None, "evolves_to": "プクリン", "appear": 0, "moves": ["うたう", "はたく"], "shiny": False},
    {"name": "プリン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/39.png", "base_stats": {'HP': 115, '攻撃': 45, '防御': 20, '特攻': 45, '特防': 25, '素早さ': 20}, "rarity": 1, "evolve_level": None, "evolves_to": "プクリン", "appear": 0, "moves": ["うたう", "はたく"], "shiny": True},
    {"name": "プクリン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/40.png", "base_stats": {'HP': 140, '攻撃': 70, '防御': 45, '特攻': 85, '特防': 50, '素早さ': 45}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["うたう", "はたく"], "shiny": False},
    {"name": "プクリン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/40.png", "base_stats": {'HP': 140, '攻撃': 70, '防御': 45, '特攻': 85, '特防': 50, '素早さ': 45}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["うたう", "はたく"], "shiny": True},
    {"name": "ズバット", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/41.png", "base_stats": {'HP': 40, '攻撃': 45, '防御': 35, '特攻': 30, '特防': 40, '素早さ': 55}, "rarity": 1, "evolve_level": 22, "evolves_to": "ゴルバット", "appear": 0, "moves": ["ちょうおんぱ", "かみつく"], "shiny": False},
    {"name": "ズバット", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/41.png", "base_stats": {'HP': 40, '攻撃': 45, '防御': 35, '特攻': 30, '特防': 40, '素早さ': 55}, "rarity": 1, "evolve_level": 22, "evolves_to": "ゴルバット", "appear": 0, "moves": ["ちょうおんぱ", "かみつく"], "shiny": True},
    {"name": "ゴルバット", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/42.png", "base_stats": {'HP': 75, '攻撃': 80, '防御': 70, '特攻': 65, '特防': 75, '素早さ': 90}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["どくばり", "かみつく"], "shiny": False},
    {"name": "ゴルバット", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/42.png", "base_stats": {'HP': 75, '攻撃': 80, '防御': 70, '特攻': 65, '特防': 75, '素早さ': 90}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["どくばり", "かみつく"], "shiny": True},
    {"name": "ナゾノクサ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/43.png", "base_stats": {'HP': 45, '攻撃': 50, '防御': 55, '特攻': 75, '特防': 65, '素早さ': 30}, "rarity": 1, "evolve_level": 21, "evolves_to": "クサイハナ", "appear": 0, "moves": ["つるのムチ", "どくのこな"], "shiny": False},
    {"name": "ナゾノクサ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/43.png", "base_stats": {'HP': 45, '攻撃': 50, '防御': 55, '特攻': 75, '特防': 65, '素早さ': 30}, "rarity": 1, "evolve_level": 21, "evolves_to": "クサイハナ", "appear": 0, "moves": ["つるのムチ", "どくのこな"], "shiny": True},
    {"name": "クサイハナ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/44.png", "base_stats": {'HP': 60, '攻撃': 65, '防御': 70, '特攻': 85, '特防': 75, '素早さ': 40}, "rarity": 2, "evolve_level": None, "evolves_to": "ラフレシア", "appear": 0, "moves": ["つるのムチ", "どくのこな"], "shiny": False},
    {"name": "クサイハナ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/44.png", "base_stats": {'HP': 60, '攻撃': 65, '防御': 70, '特攻': 85, '特防': 75, '素早さ': 40}, "rarity": 2, "evolve_level": None, "evolves_to": "ラフレシア", "appear": 0, "moves": ["つるのムチ", "どくのこな"], "shiny": True},
    {"name": "ラフレシア", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/45.png", "base_stats": {'HP': 75, '攻撃': 80, '防御': 85, '特攻': 110, '特防': 90, '素早さ': 50}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ソーラービーム", "どくどく"], "shiny": False},
    {"name": "ラフレシア", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/45.png", "base_stats": {'HP': 75, '攻撃': 80, '防御': 85, '特攻': 110, '特防': 90, '素早さ': 50}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ソーラービーム", "どくどく"], "shiny": True},
    {"name": "パラス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/46.png", "base_stats": {'HP': 35, '攻撃': 70, '防御': 55, '特攻': 45, '特防': 55, '素早さ': 25}, "rarity": 1, "evolve_level": 24, "evolves_to": "パラセクト", "appear": 0, "moves": ["ひっかく", "きゅうけつ"], "shiny": False},
    {"name": "パラス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/46.png", "base_stats": {'HP': 35, '攻撃': 70, '防御': 55, '特攻': 45, '特防': 55, '素早さ': 25}, "rarity": 1, "evolve_level": 24, "evolves_to": "パラセクト", "appear": 0, "moves": ["ひっかく", "きゅうけつ"], "shiny": True},
    {"name": "パラセクト", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/47.png", "base_stats": {'HP': 60, '攻撃': 95, '防御': 80, '特攻': 60, '特防': 80, '素早さ': 30}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["きゅうけつ", "ソーラービーム"], "shiny": False},
    {"name": "パラセクト", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/47.png", "base_stats": {'HP': 60, '攻撃': 95, '防御': 80, '特攻': 60, '特防': 80, '素早さ': 30}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["きゅうけつ", "ソーラービーム"], "shiny": True},
    {"name": "コンパン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/48.png", "base_stats": {'HP': 60, '攻撃': 55, '防御': 50, '特攻': 40, '特防': 55, '素早さ': 45}, "rarity": 1, "evolve_level": 31, "evolves_to": "モルフォン", "appear": 0, "moves": ["サイケこうせん", "かぜおこし"], "shiny": False},
    {"name": "コンパン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/48.png", "base_stats": {'HP': 60, '攻撃': 55, '防御': 50, '特攻': 40, '特防': 55, '素早さ': 45}, "rarity": 1, "evolve_level": 31, "evolves_to": "モルフォン", "appear": 0, "moves": ["サイケこうせん", "かぜおこし"], "shiny": True},
    {"name": "モルフォン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/49.png", "base_stats": {'HP': 70, '攻撃': 65, '防御': 60, '特攻': 90, '特防': 75, '素早さ': 90}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かぜおこし", "むしのさざめき"], "shiny": False},
    {"name": "モルフォン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/49.png", "base_stats": {'HP': 70, '攻撃': 65, '防御': 60, '特攻': 90, '特防': 75, '素早さ': 90}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かぜおこし", "むしのさざめき"], "shiny": True},
    {"name": "ディグダ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/50.png", "base_stats": {'HP': 10, '攻撃': 55, '防御': 25, '特攻': 35, '特防': 45, '素早さ': 95}, "rarity": 1, "evolve_level": 26, "evolves_to": "ダグトリオ", "appear": 0, "moves": ["すなかけ", "あなをほる"], "shiny": False},
    {"name": "ディグダ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/50.png", "base_stats": {'HP': 10, '攻撃': 55, '防御': 25, '特攻': 35, '特防': 45, '素早さ': 95}, "rarity": 1, "evolve_level": 26, "evolves_to": "ダグトリオ", "appear": 0, "moves": ["すなかけ", "あなをほる"], "shiny": True},
    {"name": "ダグトリオ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/51.png", "base_stats": {'HP': 35, '攻撃': 100, '防御': 50, '特攻': 50, '特防': 70, '素早さ': 120}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["じしん", "あなをほる"], "shiny": False},
    {"name": "ダグトリオ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/51.png", "base_stats": {'HP': 35, '攻撃': 100, '防御': 50, '特攻': 50, '特防': 70, '素早さ': 120}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["じしん", "あなをほる"], "shiny": True},
    {"name": "ニャース", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/52.png", "base_stats": {'HP': 40, '攻撃': 45, '防御': 35, '特攻': 40, '特防': 40, '素早さ': 90}, "rarity": 1, "evolve_level": 28, "evolves_to": "ペルシアン", "appear": 0, "moves": ["ひっかく", "しっぽをふる"], "shiny": False},
    {"name": "ニャース", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/52.png", "base_stats": {'HP': 40, '攻撃': 45, '防御': 35, '特攻': 40, '特防': 40, '素早さ': 90}, "rarity": 1, "evolve_level": 28, "evolves_to": "ペルシアン", "appear": 0, "moves": ["ひっかく", "しっぽをふる"], "shiny": True},
    {"name": "ペルシアン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/53.png", "base_stats": {'HP': 65, '攻撃': 70, '防御': 60, '特攻': 65, '特防': 65, '素早さ': 115}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["スピードスター", "かみつく"], "shiny": False},
    {"name": "ペルシアン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/53.png", "base_stats": {'HP': 65, '攻撃': 70, '防御': 60, '特攻': 65, '特防': 65, '素早さ': 115}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["スピードスター", "かみつく"], "shiny": True},
    {"name": "コダック", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png", "base_stats": {'HP': 50, '攻撃': 52, '防御': 48, '特攻': 65, '特防': 50, '素早さ': 55}, "rarity": 1, "evolve_level": 33, "evolves_to": "ゴルダック", "appear": 0, "moves": ["みずでっぽう"], "shiny": False},
    {"name": "コダック", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/54.png", "base_stats": {'HP': 50, '攻撃': 52, '防御': 48, '特攻': 65, '特防': 50, '素早さ': 55}, "rarity": 1, "evolve_level": 33, "evolves_to": "ゴルダック", "appear": 0, "moves": ["みずでっぽう"], "shiny": True},
    {"name": "ゴルダック", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/55.png", "base_stats": {'HP': 80, '攻撃': 82, '防御': 78, '特攻': 95, '特防': 80, '素早さ': 85}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["みずでっぽう", "ハイドロポンプ"], "shiny": False},
    {"name": "ゴルダック", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/55.png", "base_stats": {'HP': 80, '攻撃': 82, '防御': 78, '特攻': 95, '特防': 80, '素早さ': 85}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["みずでっぽう", "ハイドロポンプ"], "shiny": True},
    {"name": "マンキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/56.png", "base_stats": {'HP': 40, '攻撃': 80, '防御': 35, '特攻': 35, '特防': 45, '素早さ': 70}, "rarity": 1, "evolve_level": 28, "evolves_to": "オコリザル", "appear": 0, "moves": ["けたぐり", "いかり"], "shiny": False},
    {"name": "マンキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/56.png", "base_stats": {'HP': 40, '攻撃': 80, '防御': 35, '特攻': 35, '特防': 45, '素早さ': 70}, "rarity": 1, "evolve_level": 28, "evolves_to": "オコリザル", "appear": 0, "moves": ["けたぐり", "いかり"], "shiny": True},
    {"name": "オコリザル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/57.png", "base_stats": {'HP': 65, '攻撃': 105, '防御': 60, '特攻': 60, '特防': 70, '素早さ': 95}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["からてチョップ", "けたぐり"], "shiny": False},
    {"name": "オコリザル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/57.png", "base_stats": {'HP': 65, '攻撃': 105, '防御': 60, '特攻': 60, '特防': 70, '素早さ': 95}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["からてチョップ", "けたぐり"], "shiny": True},
    {"name": "ガーディ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/58.png", "base_stats": {'HP': 55, '攻撃': 70, '防御': 45, '特攻': 70, '特防': 50, '素早さ': 60}, "rarity": 1, "evolve_level": None, "evolves_to": "ウインディ", "appear": 0, "moves": ["ひのこ", "かえんほうしゃ"], "shiny": False},
    {"name": "ガーディ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/58.png", "base_stats": {'HP': 55, '攻撃': 70, '防御': 45, '特攻': 70, '特防': 50, '素早さ': 60}, "rarity": 1, "evolve_level": None, "evolves_to": "ウインディ", "appear": 0, "moves": ["ひのこ", "かえんほうしゃ"], "shiny": True},
    {"name": "ウインディ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/59.png", "base_stats": {'HP': 90, '攻撃': 110, '防御': 80, '特攻': 100, '特防': 80, '素早さ': 95}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かえんほうしゃ", "だいもんじ"], "shiny": False},
    {"name": "ウインディ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/59.png", "base_stats": {'HP': 90, '攻撃': 110, '防御': 80, '特攻': 100, '特防': 80, '素早さ': 95}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かえんほうしゃ", "だいもんじ"], "shiny": True},
    {"name": "ニョロモ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/60.png", "base_stats": {'HP': 40, '攻撃': 50, '防御': 40, '特攻': 40, '特防': 40, '素早さ': 90}, "rarity": 1, "evolve_level": 25, "evolves_to": "ニョロゾ", "appear": 0, "moves": ["みずでっぽう"], "shiny": False},
    {"name": "ニョロモ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/60.png", "base_stats": {'HP': 40, '攻撃': 50, '防御': 40, '特攻': 40, '特防': 40, '素早さ': 90}, "rarity": 1, "evolve_level": 25, "evolves_to": "ニョロゾ", "appear": 0, "moves": ["みずでっぽう"], "shiny": True},
    {"name": "ニョロゾ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/61.png", "base_stats": {'HP': 65, '攻撃': 65, '防御': 65, '特攻': 50, '特防': 50, '素早さ': 90}, "rarity": 2, "evolve_level": 36, "evolves_to": "ニョロボン", "appear": 0, "moves": ["みずでっぽう", "かみなりパンチ"], "shiny": False},
    {"name": "ニョロゾ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/61.png", "base_stats": {'HP': 65, '攻撃': 65, '防御': 65, '特攻': 50, '特防': 50, '素早さ': 90}, "rarity": 2, "evolve_level": 36, "evolves_to": "ニョロボン", "appear": 0, "moves": ["みずでっぽう", "かみなりパンチ"], "shiny": True},
    {"name": "ニョロボン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/62.png", "base_stats": {'HP': 90, '攻撃': 85, '防御': 95, '特攻': 70, '特防': 90, '素早さ': 70}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ハイドロポンプ", "かみなりパンチ"], "shiny": False},
    {"name": "ニョロボン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/62.png", "base_stats": {'HP': 90, '攻撃': 85, '防御': 95, '特攻': 70, '特防': 90, '素早さ': 70}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ハイドロポンプ", "かみなりパンチ"], "shiny": True},
    {"name": "ケーシィ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/63.png", "base_stats": {'HP': 25, '攻撃': 20, '防御': 15, '特攻': 105, '特防': 55, '素早さ': 90}, "rarity": 1, "evolve_level": 16, "evolves_to": "ユンゲラー", "appear": 0, "moves": ["テレポート"], "shiny": False},
    {"name": "ケーシィ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/63.png", "base_stats": {'HP': 25, '攻撃': 20, '防御': 15, '特攻': 105, '特防': 55, '素早さ': 90}, "rarity": 1, "evolve_level": 16, "evolves_to": "ユンゲラー", "appear": 0, "moves": ["テレポート"], "shiny": True},
    {"name": "ユンゲラー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/64.png", "base_stats": {'HP': 40, '攻撃': 35, '防御': 30, '特攻': 120, '特防': 70, '素早さ': 105}, "rarity": 2, "evolve_level": 36, "evolves_to": "フーディン", "appear": 0, "moves": ["サイコキネシス", "かげぶんしん"], "shiny": False},
    {"name": "ユンゲラー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/64.png", "base_stats": {'HP': 40, '攻撃': 35, '防御': 30, '特攻': 120, '特防': 70, '素早さ': 105}, "rarity": 2, "evolve_level": 36, "evolves_to": "フーディン", "appear": 0, "moves": ["サイコキネシス", "かげぶんしん"], "shiny": True},
    {"name": "フーディン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png", "base_stats": {'HP': 55, '攻撃': 50, '防御': 45, '特攻': 135, '特防': 95, '素早さ': 120}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "じこさいせい"], "shiny": False},
    {"name": "フーディン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/65.png", "base_stats": {'HP': 55, '攻撃': 50, '防御': 45, '特攻': 135, '特防': 95, '素早さ': 120}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "じこさいせい"], "shiny": True},
    {"name": "ワンリキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/66.png", "base_stats": {'HP': 70, '攻撃': 80, '防御': 50, '特攻': 35, '特防': 35, '素早さ': 35}, "rarity": 1, "evolve_level": 28, "evolves_to": "ゴーリキー", "appear": 0, "moves": ["けたぐり", "からてチョップ"], "shiny": False},
    {"name": "ワンリキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/66.png", "base_stats": {'HP': 70, '攻撃': 80, '防御': 50, '特攻': 35, '特防': 35, '素早さ': 35}, "rarity": 1, "evolve_level": 28, "evolves_to": "ゴーリキー", "appear": 0, "moves": ["けたぐり", "からてチョップ"], "shiny": True},
    {"name": "ゴーリキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/67.png", "base_stats": {'HP': 80, '攻撃': 100, '防御': 70, '特攻': 50, '特防': 60, '素早さ': 45}, "rarity": 2, "evolve_level": 36, "evolves_to": "カイリキー", "appear": 0, "moves": ["けたぐり", "からてチョップ"], "shiny": False},
    {"name": "ゴーリキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/67.png", "base_stats": {'HP': 80, '攻撃': 100, '防御': 70, '特攻': 50, '特防': 60, '素早さ': 45}, "rarity": 2, "evolve_level": 36, "evolves_to": "カイリキー", "appear": 0, "moves": ["けたぐり", "からてチョップ"], "shiny": True},
    {"name": "カイリキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png", "base_stats": {'HP': 90, '攻撃': 130, '防御': 80, '特攻': 65, '特防': 85, '素早さ': 55}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かみなりパンチ", "けたぐり"], "shiny": False},
    {"name": "カイリキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/68.png", "base_stats": {'HP': 90, '攻撃': 130, '防御': 80, '特攻': 65, '特防': 85, '素早さ': 55}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かみなりパンチ", "けたぐり"], "shiny": True},
    {"name": "マダツボミ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/69.png", "base_stats": {'HP': 50, '攻撃': 75, '防御': 35, '特攻': 70, '特防': 30, '素早さ': 40}, "rarity": 1, "evolve_level": 21, "evolves_to": "ウツドン", "appear": 0, "moves": ["つるのムチ"], "shiny": False},
    {"name": "マダツボミ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/69.png", "base_stats": {'HP': 50, '攻撃': 75, '防御': 35, '特攻': 70, '特防': 30, '素早さ': 40}, "rarity": 1, "evolve_level": 21, "evolves_to": "ウツドン", "appear": 0, "moves": ["つるのムチ"], "shiny": True},
    {"name": "ウツドン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/70.png", "base_stats": {'HP': 65, '攻撃': 90, '防御': 50, '特攻': 85, '特防': 45, '素早さ': 55}, "rarity": 2, "evolve_level": 36, "evolves_to": "ウツボット", "appear": 0, "moves": ["はっぱカッター"], "shiny": False},
    {"name": "ウツドン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/70.png", "base_stats": {'HP': 65, '攻撃': 90, '防御': 50, '特攻': 85, '特防': 45, '素早さ': 55}, "rarity": 2, "evolve_level": 36, "evolves_to": "ウツボット", "appear": 0, "moves": ["はっぱカッター"], "shiny": True},
    {"name": "ウツボット", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/71.png", "base_stats": {'HP': 80, '攻撃': 105, '防御': 65, '特攻': 100, '特防': 60, '素早さ': 70}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["はっぱカッター", "ソーラービーム"], "shiny": False},
    {"name": "ウツボット", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/71.png", "base_stats": {'HP': 80, '攻撃': 105, '防御': 65, '特攻': 100, '特防': 60, '素早さ': 70}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["はっぱカッター", "ソーラービーム"], "shiny": True},
    {"name": "メノクラゲ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/72.png", "base_stats": {'HP': 40, '攻撃': 40, '防御': 35, '特攻': 50, '特防': 100, '素早さ': 70}, "rarity": 1, "evolve_level": 30, "evolves_to": "ドククラゲ", "appear": 0, "moves": ["バブルこうせん", "どくどく"], "shiny": False},
    {"name": "メノクラゲ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/72.png", "base_stats": {'HP': 40, '攻撃': 40, '防御': 35, '特攻': 50, '特防': 100, '素早さ': 70}, "rarity": 1, "evolve_level": 30, "evolves_to": "ドククラゲ", "appear": 0, "moves": ["バブルこうせん", "どくどく"], "shiny": True},
    {"name": "ドククラゲ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/73.png", "base_stats": {'HP': 80, '攻撃': 70, '防御': 65, '特攻': 80, '特防': 120, '素早さ': 100}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ハイドロポンプ", "どくづき"], "shiny": False},
    {"name": "ドククラゲ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/73.png", "base_stats": {'HP': 80, '攻撃': 70, '防御': 65, '特攻': 80, '特防': 120, '素早さ': 100}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ハイドロポンプ", "どくづき"], "shiny": True},
    {"name": "イシツブテ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/74.png", "base_stats": {'HP': 40, '攻撃': 80, '防御': 100, '特攻': 30, '特防': 30, '素早さ': 20}, "rarity": 1, "evolve_level": 25, "evolves_to": "ゴローン", "appear": 0, "moves": ["ころがる"], "shiny": False},
    {"name": "イシツブテ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/74.png", "base_stats": {'HP': 40, '攻撃': 80, '防御': 100, '特攻': 30, '特防': 30, '素早さ': 20}, "rarity": 1, "evolve_level": 25, "evolves_to": "ゴローン", "appear": 0, "moves": ["ころがる"], "shiny": True},
    {"name": "ゴローン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/75.png", "base_stats": {'HP': 55, '攻撃': 95, '防御': 115, '特攻': 45, '特防': 45, '素早さ': 35}, "rarity": 2, "evolve_level": 40, "evolves_to": "ゴローニャ", "appear": 0, "moves": ["じしん", "いわおとし"], "shiny": False},
    {"name": "ゴローン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/75.png", "base_stats": {'HP': 55, '攻撃': 95, '防御': 115, '特攻': 45, '特防': 45, '素早さ': 35}, "rarity": 2, "evolve_level": 40, "evolves_to": "ゴローニャ", "appear": 0, "moves": ["じしん", "いわおとし"], "shiny": True},
    {"name": "ゴローニャ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/76.png", "base_stats": {'HP': 80, '攻撃': 120, '防御': 130, '特攻': 55, '特防': 65, '素早さ': 45}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["じしん", "いわなだれ"], "shiny": False},
    {"name": "ゴローニャ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/76.png", "base_stats": {'HP': 80, '攻撃': 120, '防御': 130, '特攻': 55, '特防': 65, '素早さ': 45}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["じしん", "いわなだれ"], "shiny": True},
    {"name": "ポニータ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/77.png", "base_stats": {'HP': 50, '攻撃': 85, '防御': 55, '特攻': 65, '特防': 65, '素早さ': 90}, "rarity": 1, "evolve_level": 40, "evolves_to": "ギャロップ", "appear": 0, "moves": ["ひのこ"], "shiny": False},
    {"name": "ポニータ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/77.png", "base_stats": {'HP': 50, '攻撃': 85, '防御': 55, '特攻': 65, '特防': 65, '素早さ': 90}, "rarity": 1, "evolve_level": 40, "evolves_to": "ギャロップ", "appear": 0, "moves": ["ひのこ"], "shiny": True},
    {"name": "ギャロップ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/78.png", "base_stats": {'HP': 65, '攻撃': 100, '防御': 70, '特攻': 80, '特防': 80, '素早さ': 105}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かえんほうしゃ", "けたぐり"], "shiny": False},
    {"name": "ギャロップ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/78.png", "base_stats": {'HP': 65, '攻撃': 100, '防御': 70, '特攻': 80, '特防': 80, '素早さ': 105}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かえんほうしゃ", "けたぐり"], "shiny": True},
    {"name": "ヤドン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/79.png", "base_stats": {'HP': 90, '攻撃': 65, '防御': 65, '特攻': 40, '特防': 40, '素早さ': 15}, "rarity": 1, "evolve_level": 37, "evolves_to": "ヤドラン", "appear": 0, "moves": ["ねんりき"], "shiny": False},
    {"name": "ヤドン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/79.png", "base_stats": {'HP': 90, '攻撃': 65, '防御': 65, '特攻': 40, '特防': 40, '素早さ': 15}, "rarity": 1, "evolve_level": 37, "evolves_to": "ヤドラン", "appear": 0, "moves": ["ねんりき"], "shiny": True},
    {"name": "ヤドラン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/80.png", "base_stats": {'HP': 95, '攻撃': 75, '防御': 110, '特攻': 100, '特防': 80, '素早さ': 30}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "ドわすれ"], "shiny": False},
    {"name": "ヤドラン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/80.png", "base_stats": {'HP': 95, '攻撃': 75, '防御': 110, '特攻': 100, '特防': 80, '素早さ': 30}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "ドわすれ"], "shiny": True},
    {"name": "コイル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/81.png", "base_stats": {'HP': 25, '攻撃': 35, '防御': 70, '特攻': 95, '特防': 55, '素早さ': 45}, "rarity": 1, "evolve_level": 30, "evolves_to": "レアコイル", "appear": 0, "moves": ["でんきショック"], "shiny": False},
    {"name": "コイル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/81.png", "base_stats": {'HP': 25, '攻撃': 35, '防御': 70, '特攻': 95, '特防': 55, '素早さ': 45}, "rarity": 1, "evolve_level": 30, "evolves_to": "レアコイル", "appear": 0, "moves": ["でんきショック"], "shiny": True},
    {"name": "レアコイル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/82.png", "base_stats": {'HP': 50, '攻撃': 60, '防御': 95, '特攻': 120, '特防': 70, '素早さ': 70}, "rarity": 2, "evolve_level": None, "evolves_to": "ジバコイル", "appear": 0, "moves": ["10まんボルト", "いやなおと"], "shiny": False},
    {"name": "レアコイル", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/82.png", "base_stats": {'HP': 50, '攻撃': 60, '防御': 95, '特攻': 120, '特防': 70, '素早さ': 70}, "rarity": 2, "evolve_level": None, "evolves_to": "ジバコイル", "appear": 0, "moves": ["10まんボルト", "いやなおと"], "shiny": True},
    {"name": "カモネギ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/83.png", "base_stats": {'HP': 52, '攻撃': 90, '防御': 55, '特攻': 58, '特防': 62, '素早さ': 60}, "rarity": 1, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["つばめがえし", "つじぎり"], "shiny": False},
    {"name": "カモネギ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/83.png", "base_stats": {'HP': 52, '攻撃': 90, '防御': 55, '特攻': 58, '特防': 62, '素早さ': 60}, "rarity": 1, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["つばめがえし", "つじぎり"], "shiny": True},
    {"name": "ドードー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/84.png", "base_stats": {'HP': 35, '攻撃': 85, '防御': 45, '特攻': 35, '特防': 35, '素早さ': 75}, "rarity": 1, "evolve_level": 31, "evolves_to": "ドードリオ", "appear": 0, "moves": ["でんこうせっか", "とっしん"], "shiny": False},
    {"name": "ドードー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/84.png", "base_stats": {'HP': 35, '攻撃': 85, '防御': 45, '特攻': 35, '特防': 35, '素早さ': 75}, "rarity": 1, "evolve_level": 31, "evolves_to": "ドードリオ", "appear": 0, "moves": ["でんこうせっか", "とっしん"], "shiny": True},
    {"name": "ドードリオ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/85.png", "base_stats": {'HP': 60, '攻撃': 110, '防御': 70, '特攻': 60, '特防': 60, '素早さ': 100}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["トライアタック", "とっしん"], "shiny": False},
    {"name": "ドードリオ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/85.png", "base_stats": {'HP': 60, '攻撃': 110, '防御': 70, '特攻': 60, '特防': 60, '素早さ': 100}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["トライアタック", "とっしん"], "shiny": True},
    {"name": "パウワウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/86.png", "base_stats": {'HP': 65, '攻撃': 45, '防御': 55, '特攻': 45, '特防': 70, '素早さ': 45}, "rarity": 1, "evolve_level": 34, "evolves_to": "ジュゴン", "appear": 0, "moves": ["ころがる", "あわ"], "shiny": False},
    {"name": "パウワウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/86.png", "base_stats": {'HP': 65, '攻撃': 45, '防御': 55, '特攻': 45, '特防': 70, '素早さ': 45}, "rarity": 1, "evolve_level": 34, "evolves_to": "ジュゴン", "appear": 0, "moves": ["ころがる", "あわ"], "shiny": True},
    {"name": "ジュゴン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/87.png", "base_stats": {'HP': 90, '攻撃': 70, '防御': 80, '特攻': 70, '特防': 95, '素早さ': 70}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["れいとうビーム", "みずでっぽう"], "shiny": False},
    {"name": "ジュゴン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/87.png", "base_stats": {'HP': 90, '攻撃': 70, '防御': 80, '特攻': 70, '特防': 95, '素早さ': 70}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["れいとうビーム", "みずでっぽう"], "shiny": True},
    {"name": "ベトベター", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/88.png", "base_stats": {'HP': 80, '攻撃': 80, '防御': 50, '特攻': 40, '特防': 50, '素早さ': 25}, "rarity": 1, "evolve_level": 38, "evolves_to": "ベトベトン", "appear": 0, "moves": ["どくづき", "どくガス"], "shiny": False},
    {"name": "ベトベター", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/88.png", "base_stats": {'HP': 80, '攻撃': 80, '防御': 50, '特攻': 40, '特防': 50, '素早さ': 25}, "rarity": 1, "evolve_level": 38, "evolves_to": "ベトベトン", "appear": 0, "moves": ["どくづき", "どくガス"], "shiny": True},
    {"name": "ベトベトン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/89.png", "base_stats": {'HP': 105, '攻撃': 105, '防御': 75, '特攻': 65, '特防': 100, '素早さ': 50}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["どくづき", "どくガス"], "shiny": False},
    {"name": "ベトベトン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/89.png", "base_stats": {'HP': 105, '攻撃': 105, '防御': 75, '特攻': 65, '特防': 100, '素早さ': 50}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["どくづき", "どくガス"], "shiny": True},
    {"name": "シェルダー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/90.png", "base_stats": {'HP': 30, '攻撃': 65, '防御': 100, '特攻': 45, '特防': 25, '素早さ': 40}, "rarity": 1, "evolve_level": None, "evolves_to": "パルシェン", "appear": 0, "moves": ["つららばり", "からにこもる"], "shiny": False},
    {"name": "シェルダー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/90.png", "base_stats": {'HP': 30, '攻撃': 65, '防御': 100, '特攻': 45, '特防': 25, '素早さ': 40}, "rarity": 1, "evolve_level": None, "evolves_to": "パルシェン", "appear": 0, "moves": ["つららばり", "からにこもる"], "shiny": True},
    {"name": "パルシェン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/91.png", "base_stats": {'HP': 50, '攻撃': 95, '防御': 180, '特攻': 85, '特防': 45, '素早さ': 70}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["つららばり", "ハイドロポンプ"], "shiny": False},
    {"name": "パルシェン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/91.png", "base_stats": {'HP': 50, '攻撃': 95, '防御': 180, '特攻': 85, '特防': 45, '素早さ': 70}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["つららばり", "ハイドロポンプ"], "shiny": True},
    {"name": "ゴース", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/92.png", "base_stats": {'HP': 30, '攻撃': 35, '防御': 30, '特攻': 100, '特防': 35, '素早さ': 80}, "rarity": 1, "evolve_level": 25, "evolves_to": "ゴースト", "appear": 0, "moves": ["シャドーボール", "ヘドロこうげき"], "shiny": False},
    {"name": "ゴース", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/92.png", "base_stats": {'HP': 30, '攻撃': 35, '防御': 30, '特攻': 100, '特防': 35, '素早さ': 80}, "rarity": 1, "evolve_level": 25, "evolves_to": "ゴースト", "appear": 0, "moves": ["シャドーボール", "ヘドロこうげき"], "shiny": True},
    {"name": "ゴースト", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/93.png", "base_stats": {'HP': 45, '攻撃': 50, '防御': 45, '特攻': 115, '特防': 55, '素早さ': 95}, "rarity": 2, "evolve_level": None, "evolves_to": "ゲンガー", "appear": 0, "moves": ["シャドーボール", "ヘドロこうげき"], "shiny": False},
    {"name": "ゴースト", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/93.png", "base_stats": {'HP': 45, '攻撃': 50, '防御': 45, '特攻': 115, '特防': 55, '素早さ': 95}, "rarity": 2, "evolve_level": None, "evolves_to": "ゲンガー", "appear": 0, "moves": ["シャドーボール", "ヘドロこうげき"], "shiny": True},
    {"name": "ゲンガー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png", "base_stats": {'HP': 60, '攻撃': 65, '防御': 60, '特攻': 130, '特防': 75, '素早さ': 110}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["シャドーボール", "ヘドロこうげき"], "shiny": False},
    {"name": "ゲンガー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/94.png", "base_stats": {'HP': 60, '攻撃': 65, '防御': 60, '特攻': 130, '特防': 75, '素早さ': 110}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["シャドーボール", "ヘドロこうげき"], "shiny": True},
    {"name": "イワーク", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/95.png", "base_stats": {'HP': 35, '攻撃': 45, '防御': 160, '特攻': 30, '特防': 45, '素早さ': 70}, "rarity": 1, "evolve_level": None, "evolves_to": "ハガネール", "appear": 0, "moves": ["いわおとし"], "shiny": False},
    {"name": "イワーク", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/95.png", "base_stats": {'HP': 35, '攻撃': 45, '防御': 160, '特攻': 30, '特防': 45, '素早さ': 70}, "rarity": 1, "evolve_level": None, "evolves_to": "ハガネール", "appear": 0, "moves": ["いわおとし"], "shiny": True},
    {"name": "スリープ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/96.png", "base_stats": {'HP': 60, '攻撃': 48, '防御': 45, '特攻': 43, '特防': 90, '素早さ': 42}, "rarity": 1, "evolve_level": 26, "evolves_to": "スリーパー", "appear": 0, "moves": ["ねんりき"], "shiny": False},
    {"name": "スリープ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/96.png", "base_stats": {'HP': 60, '攻撃': 48, '防御': 45, '特攻': 43, '特防': 90, '素早さ': 42}, "rarity": 1, "evolve_level": 26, "evolves_to": "スリーパー", "appear": 0, "moves": ["ねんりき"], "shiny": True},
    {"name": "スリーパー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/97.png", "base_stats": {'HP': 85, '攻撃': 73, '防御': 70, '特攻': 73, '特防': 115, '素早さ': 67}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ねんりき", "サイコキネシス"], "shiny": False},
    {"name": "スリーパー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/97.png", "base_stats": {'HP': 85, '攻撃': 73, '防御': 70, '特攻': 73, '特防': 115, '素早さ': 67}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ねんりき", "サイコキネシス"], "shiny": True},
    {"name": "クラブ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/98.png", "base_stats": {'HP': 30, '攻撃': 105, '防御': 90, '特攻': 25, '特防': 25, '素早さ': 50}, "rarity": 1, "evolve_level": 28, "evolves_to": "キングラー", "appear": 0, "moves": ["クラブハンマー", "あわ"], "shiny": False},
    {"name": "クラブ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/98.png", "base_stats": {'HP': 30, '攻撃': 105, '防御': 90, '特攻': 25, '特防': 25, '素早さ': 50}, "rarity": 1, "evolve_level": 28, "evolves_to": "キングラー", "appear": 0, "moves": ["クラブハンマー", "あわ"], "shiny": True},
    {"name": "キングラー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/99.png", "base_stats": {'HP': 55, '攻撃': 130, '防御': 115, '特攻': 50, '特防': 50, '素早さ': 75}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["クラブハンマー", "はたく"], "shiny": False},
    {"name": "キングラー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/99.png", "base_stats": {'HP': 55, '攻撃': 130, '防御': 115, '特攻': 50, '特防': 50, '素早さ': 75}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["クラブハンマー", "はたく"], "shiny": True},
    {"name": "ビリリダマ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/100.png", "base_stats": {'HP': 40, '攻撃': 30, '防御': 50, '特攻': 55, '特防': 55, '素早さ': 100}, "rarity": 1, "evolve_level": 30, "evolves_to": "マルマイン", "appear": 0, "moves": ["じばく", "たいあたり"], "shiny": False},
    {"name": "ビリリダマ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/100.png", "base_stats": {'HP': 40, '攻撃': 30, '防御': 50, '特攻': 55, '特防': 55, '素早さ': 100}, "rarity": 1, "evolve_level": 30, "evolves_to": "マルマイン", "appear": 0, "moves": ["じばく", "たいあたり"], "shiny": True},
    {"name": "マルマイン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/101.png", "base_stats": {'HP': 60, '攻撃': 50, '防御': 70, '特攻': 80, '特防': 80, '素早さ': 150}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["だいばくはつ", "10まんボルト"], "shiny": False},
    {"name": "マルマイン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/101.png", "base_stats": {'HP': 60, '攻撃': 50, '防御': 70, '特攻': 80, '特防': 80, '素早さ': 150}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["だいばくはつ", "10まんボルト"], "shiny": True},
    {"name": "タマタマ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/102.png", "base_stats": {'HP': 60, '攻撃': 40, '防御': 80, '特攻': 60, '特防': 45, '素早さ': 40}, "rarity": 1, "evolve_level": 35, "evolves_to": "ナッシー", "appear": 0, "moves": ["ねんりき", "はっぱカッター"], "shiny": False},
    {"name": "タマタマ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/102.png", "base_stats": {'HP': 60, '攻撃': 40, '防御': 80, '特攻': 60, '特防': 45, '素早さ': 40}, "rarity": 1, "evolve_level": 35, "evolves_to": "ナッシー", "appear": 0, "moves": ["ねんりき", "はっぱカッター"], "shiny": True},
    {"name": "ナッシー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/103.png", "base_stats": {'HP': 95, '攻撃': 95, '防御': 85, '特攻': 125, '特防': 75, '素早さ': 55}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "ソーラービーム"], "shiny": False},
    {"name": "ナッシー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/103.png", "base_stats": {'HP': 95, '攻撃': 95, '防御': 85, '特攻': 125, '特防': 75, '素早さ': 55}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "ソーラービーム"], "shiny": True},
    {"name": "カラカラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/104.png", "base_stats": {'HP': 50, '攻撃': 50, '防御': 95, '特攻': 40, '特防': 50, '素早さ': 35}, "rarity": 1, "evolve_level": 28, "evolves_to": "ガラガラ", "appear": 0, "moves": ["ホネブーメラン"], "shiny": False},
    {"name": "カラカラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/104.png", "base_stats": {'HP': 50, '攻撃': 50, '防御': 95, '特攻': 40, '特防': 50, '素早さ': 35}, "rarity": 1, "evolve_level": 28, "evolves_to": "ガラガラ", "appear": 0, "moves": ["ホネブーメラン"], "shiny": True},
    {"name": "ガラガラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/105.png", "base_stats": {'HP': 60, '攻撃': 80, '防御': 110, '特攻': 50, '特防': 80, '素早さ': 45}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ホネブーメラン", "じしん"], "shiny": False},
    {"name": "ガラガラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/105.png", "base_stats": {'HP': 60, '攻撃': 80, '防御': 110, '特攻': 50, '特防': 80, '素早さ': 45}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ホネブーメラン", "じしん"], "shiny": True},
    {"name": "サワムラー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/106.png", "base_stats": {'HP': 50, '攻撃': 120, '防御': 53, '特攻': 35, '特防': 110, '素早さ': 87}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["とびひざげり", "けたぐり"], "shiny": False},
    {"name": "サワムラー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/106.png", "base_stats": {'HP': 50, '攻撃': 120, '防御': 53, '特攻': 35, '特防': 110, '素早さ': 87}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["とびひざげり", "けたぐり"], "shiny": True},
    {"name": "エビワラー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/107.png", "base_stats": {'HP': 50, '攻撃': 105, '防御': 79, '特攻': 35, '特防': 110, '素早さ': 76}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かみなりパンチ", "れいとうパンチ"], "shiny": False},
    {"name": "エビワラー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/107.png", "base_stats": {'HP': 50, '攻撃': 105, '防御': 79, '特攻': 35, '特防': 110, '素早さ': 76}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かみなりパンチ", "れいとうパンチ"], "shiny": True},
    {"name": "ベロリンガ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/108.png", "base_stats": {'HP': 90, '攻撃': 55, '防御': 75, '特攻': 60, '特防': 75, '素早さ': 30}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ドわすれ", "のしかかり"], "shiny": False},
    {"name": "ベロリンガ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/108.png", "base_stats": {'HP': 90, '攻撃': 55, '防御': 75, '特攻': 60, '特防': 75, '素早さ': 30}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ドわすれ", "のしかかり"], "shiny": True},
    {"name": "ドガース", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/109.png", "base_stats": {'HP': 40, '攻撃': 65, '防御': 95, '特攻': 60, '特防': 45, '素早さ': 35}, "rarity": 1, "evolve_level": 35, "evolves_to": "マタドガス", "appear": 0, "moves": ["ヘドロこうげき"], "shiny": False},
    {"name": "ドガース", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/109.png", "base_stats": {'HP': 40, '攻撃': 65, '防御': 95, '特攻': 60, '特防': 45, '素早さ': 35}, "rarity": 1, "evolve_level": 35, "evolves_to": "マタドガス", "appear": 0, "moves": ["ヘドロこうげき"], "shiny": True},
    {"name": "マタドガス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/110.png", "base_stats": {'HP': 65, '攻撃': 90, '防御': 120, '特攻': 85, '特防': 70, '素早さ': 60}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ヘドロこうげき", "じばく"], "shiny": False},
    {"name": "マタドガス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/110.png", "base_stats": {'HP': 65, '攻撃': 90, '防御': 120, '特攻': 85, '特防': 70, '素早さ': 60}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ヘドロこうげき", "じばく"], "shiny": True},
    {"name": "サイホーン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/111.png", "base_stats": {'HP': 80, '攻撃': 85, '防御': 95, '特攻': 30, '特防': 30, '素早さ': 25}, "rarity": 1, "evolve_level": 42, "evolves_to": "サイドン", "appear": 0, "moves": ["とっしん"], "shiny": False},
    {"name": "サイホーン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/111.png", "base_stats": {'HP': 80, '攻撃': 85, '防御': 95, '特攻': 30, '特防': 30, '素早さ': 25}, "rarity": 1, "evolve_level": 42, "evolves_to": "サイドン", "appear": 0, "moves": ["とっしん"], "shiny": True},
    {"name": "サイドン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/112.png", "base_stats": {'HP': 105, '攻撃': 130, '防御': 120, '特攻': 45, '特防': 45, '素早さ': 40}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["じしん", "とっしん"], "shiny": False},
    {"name": "サイドン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/112.png", "base_stats": {'HP': 105, '攻撃': 130, '防御': 120, '特攻': 45, '特防': 45, '素早さ': 40}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["じしん", "とっしん"], "shiny": True},
    {"name": "ラッキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png", "base_stats": {'HP': 250, '攻撃': 5, '防御': 5, '特攻': 35, '特防': 105, '素早さ': 50}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ちきゅうなげ", "たまごばくだん"], "shiny": False},
    {"name": "ラッキー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/113.png", "base_stats": {'HP': 250, '攻撃': 5, '防御': 5, '特攻': 35, '特防': 105, '素早さ': 50}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ちきゅうなげ", "たまごばくだん"], "shiny": True},
    {"name": "モンジャラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/114.png", "base_stats": {'HP': 65, '攻撃': 55, '防御': 115, '特攻': 100, '特防': 40, '素早さ': 60}, "rarity": 1, "evolve_level": None, "evolves_to": "モジャンボ", "appear": 0, "moves": ["つるのムチ", "はっぱカッター"], "shiny": False},
    {"name": "モンジャラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/114.png", "base_stats": {'HP': 65, '攻撃': 55, '防御': 115, '特攻': 100, '特防': 40, '素早さ': 60}, "rarity": 1, "evolve_level": None, "evolves_to": "モジャンボ", "appear": 0, "moves": ["つるのムチ", "はっぱカッター"], "shiny": True},
    {"name": "ガルーラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/115.png", "base_stats": {'HP': 105, '攻撃': 95, '防御': 80, '特攻': 40, '特防': 80, '素早さ': 90}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["のしかかり", "れいとうパンチ"], "shiny": False},
    {"name": "ガルーラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/115.png", "base_stats": {'HP': 105, '攻撃': 95, '防御': 80, '特攻': 40, '特防': 80, '素早さ': 90}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["のしかかり", "れいとうパンチ"], "shiny": True},
    {"name": "タッツー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/116.png", "base_stats": {'HP': 30, '攻撃': 40, '防御': 70, '特攻': 70, '特防': 25, '素早さ': 60}, "rarity": 1, "evolve_level": 32, "evolves_to": "シードラ", "appear": 0, "moves": ["バブルこうせん"], "shiny": False},
    {"name": "タッツー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/116.png", "base_stats": {'HP': 30, '攻撃': 40, '防御': 70, '特攻': 70, '特防': 25, '素早さ': 60}, "rarity": 1, "evolve_level": 32, "evolves_to": "シードラ", "appear": 0, "moves": ["バブルこうせん"], "shiny": True},
    {"name": "シードラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/117.png", "base_stats": {'HP': 55, '攻撃': 65, '防御': 95, '特攻': 95, '特防': 45, '素早さ': 85}, "rarity": 2, "evolve_level": None, "evolves_to": "キングドラ", "appear": 0, "moves": ["バブルこうせん", "りゅうのいぶき"], "shiny": False},
    {"name": "シードラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/117.png", "base_stats": {'HP': 55, '攻撃': 65, '防御': 95, '特攻': 95, '特防': 45, '素早さ': 85}, "rarity": 2, "evolve_level": None, "evolves_to": "キングドラ", "appear": 0, "moves": ["バブルこうせん", "りゅうのいぶき"], "shiny": True},
    {"name": "トサキント", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/118.png", "base_stats": {'HP': 45, '攻撃': 67, '防御': 60, '特攻': 35, '特防': 50, '素早さ': 63}, "rarity": 1, "evolve_level": 33, "evolves_to": "アズマオウ", "appear": 0, "moves": ["みずでっぽう", "とびはねる"], "shiny": False},
    {"name": "トサキント", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/118.png", "base_stats": {'HP': 45, '攻撃': 67, '防御': 60, '特攻': 35, '特防': 50, '素早さ': 63}, "rarity": 1, "evolve_level": 33, "evolves_to": "アズマオウ", "appear": 0, "moves": ["みずでっぽう", "とびはねる"], "shiny": True},
    {"name": "アズマオウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/119.png", "base_stats": {'HP': 80, '攻撃': 92, '防御': 65, '特攻': 65, '特防': 80, '素早さ': 68}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["みずでっぽう", "つつく"], "shiny": False},
    {"name": "アズマオウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/119.png", "base_stats": {'HP': 80, '攻撃': 92, '防御': 65, '特攻': 65, '特防': 80, '素早さ': 68}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["みずでっぽう", "つつく"], "shiny": True},
    {"name": "ヒトデマン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/120.png", "base_stats": {'HP': 30, '攻撃': 45, '防御': 55, '特攻': 70, '特防': 55, '素早さ': 85}, "rarity": 1, "evolve_level": 35, "evolves_to": "スターミー", "appear": 0, "moves": ["あわ", "スピードスター"], "shiny": False},
    {"name": "ヒトデマン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/120.png", "base_stats": {'HP': 30, '攻撃': 45, '防御': 55, '特攻': 70, '特防': 55, '素早さ': 85}, "rarity": 1, "evolve_level": 35, "evolves_to": "スターミー", "appear": 0, "moves": ["あわ", "スピードスター"], "shiny": True},
    {"name": "スターミー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/121.png", "base_stats": {'HP': 60, '攻撃': 75, '防御': 85, '特攻': 100, '特防': 85, '素早さ': 115}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["バブルこうせん", "サイコキネシス"], "shiny": False},
    {"name": "スターミー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/121.png", "base_stats": {'HP': 60, '攻撃': 75, '防御': 85, '特攻': 100, '特防': 85, '素早さ': 115}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["バブルこうせん", "サイコキネシス"], "shiny": True},
    {"name": "バリヤード", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/122.png", "base_stats": {'HP': 40, '攻撃': 45, '防御': 65, '特攻': 100, '特防': 120, '素早さ': 90}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "バリアー"], "shiny": False},
    {"name": "バリヤード", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/122.png", "base_stats": {'HP': 40, '攻撃': 45, '防御': 65, '特攻': 100, '特防': 120, '素早さ': 90}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "バリアー"], "shiny": True},
    {"name": "ストライク", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/123.png", "base_stats": {'HP': 70, '攻撃': 110, '防御': 80, '特攻': 55, '特防': 80, '素早さ': 105}, "rarity": 2, "evolve_level": None, "evolves_to": "ハッサム", "appear": 0, "moves": ["エアスラッシュ", "きりさく"], "shiny": False},
    {"name": "ストライク", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/123.png", "base_stats": {'HP': 70, '攻撃': 110, '防御': 80, '特攻': 55, '特防': 80, '素早さ': 105}, "rarity": 2, "evolve_level": None, "evolves_to": "ハッサム", "appear": 0, "moves": ["エアスラッシュ", "きりさく"], "shiny": True},
    {"name": "ルージュラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/124.png", "base_stats": {'HP': 65, '攻撃': 50, '防御': 35, '特攻': 115, '特防': 95, '素早さ': 95}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["れいとうビーム", "サイコキネシス"], "shiny": False},
    {"name": "ルージュラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/124.png", "base_stats": {'HP': 65, '攻撃': 50, '防御': 35, '特攻': 115, '特防': 95, '素早さ': 95}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["れいとうビーム", "サイコキネシス"], "shiny": True},
    {"name": "エレブー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/125.png", "base_stats": {'HP': 65, '攻撃': 83, '防御': 57, '特攻': 95, '特防': 85, '素早さ': 105}, "rarity": 2, "evolve_level": None, "evolves_to": "エレキブル", "appear": 0, "moves": ["かみなりパンチ", "10まんボルト"], "shiny": False},
    {"name": "エレブー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/125.png", "base_stats": {'HP': 65, '攻撃': 83, '防御': 57, '特攻': 95, '特防': 85, '素早さ': 105}, "rarity": 2, "evolve_level": None, "evolves_to": "エレキブル", "appear": 0, "moves": ["かみなりパンチ", "10まんボルト"], "shiny": True},
    {"name": "ブーバー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/126.png", "base_stats": {'HP': 65, '攻撃': 95, '防御': 57, '特攻': 100, '特防': 85, '素早さ': 93}, "rarity": 2, "evolve_level": None, "evolves_to": "ブーバーン", "appear": 0, "moves": ["かえんほうしゃ", "ほのおのパンチ"], "shiny": False},
    {"name": "ブーバー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/126.png", "base_stats": {'HP': 65, '攻撃': 95, '防御': 57, '特攻': 100, '特防': 85, '素早さ': 93}, "rarity": 2, "evolve_level": None, "evolves_to": "ブーバーン", "appear": 0, "moves": ["かえんほうしゃ", "ほのおのパンチ"], "shiny": True},
    {"name": "カイロス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/127.png", "base_stats": {'HP': 65, '攻撃': 125, '防御': 100, '特攻': 55, '特防': 70, '素早さ': 85}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["はさみギロチン", "つじぎり"], "shiny": False},
    {"name": "カイロス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/127.png", "base_stats": {'HP': 65, '攻撃': 125, '防御': 100, '特攻': 55, '特防': 70, '素早さ': 85}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["はさみギロチン", "つじぎり"], "shiny": True},
    {"name": "ケンタロス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/128.png", "base_stats": {'HP': 75, '攻撃': 100, '防御': 95, '特攻': 40, '特防': 70, '素早さ': 110}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["のしかかり", "とっしん"], "shiny": False},
    {"name": "ケンタロス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/128.png", "base_stats": {'HP': 75, '攻撃': 100, '防御': 95, '特攻': 40, '特防': 70, '素早さ': 110}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["のしかかり", "とっしん"], "shiny": True},
    {"name": "コイキング", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/129.png", "base_stats": {'HP': 20, '攻撃': 10, '防御': 55, '特攻': 15, '特防': 20, '素早さ': 80}, "rarity": 1, "evolve_level": 20, "evolves_to": "ギャラドス", "appear": 0, "moves": ["はねる"], "shiny": False},
    {"name": "コイキング", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/129.png", "base_stats": {'HP': 20, '攻撃': 10, '防御': 55, '特攻': 15, '特防': 20, '素早さ': 80}, "rarity": 1, "evolve_level": 20, "evolves_to": "ギャラドス", "appear": 0, "moves": ["はねる"], "shiny": True},
    {"name": "ギャラドス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png", "base_stats": {'HP': 95, '攻撃': 125, '防御': 79, '特攻': 60, '特防': 100, '素早さ': 81}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["ハイドロポンプ", "げきりん"], "shiny": False},
    {"name": "ギャラドス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/130.png", "base_stats": {'HP': 95, '攻撃': 125, '防御': 79, '特攻': 60, '特防': 100, '素早さ': 81}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["ハイドロポンプ", "げきりん"], "shiny": True},
    {"name": "ラプラス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png", "base_stats": {'HP': 130, '攻撃': 85, '防御': 80, '特攻': 85, '特防': 95, '素早さ': 60}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["れいとうビーム", "ハイドロポンプ"], "shiny": False},
    {"name": "ラプラス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/131.png", "base_stats": {'HP': 130, '攻撃': 85, '防御': 80, '特攻': 85, '特防': 95, '素早さ': 60}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["れいとうビーム", "ハイドロポンプ"], "shiny": True},
    {"name": "メタモン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png", "base_stats": {'HP': 48, '攻撃': 48, '防御': 48, '特攻': 48, '特防': 48, '素早さ': 48}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["へんしん"], "shiny": False},
    {"name": "メタモン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/132.png", "base_stats": {'HP': 48, '攻撃': 48, '防御': 48, '特攻': 48, '特防': 48, '素早さ': 48}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["へんしん"], "shiny": True},
    {"name": "イーブイ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png", "base_stats": {'HP': 55, '攻撃': 55, '防御': 50, '特攻': 45, '特防': 65, '素早さ': 55}, "rarity": 1, "evolve_level": None, "evolves_to": "シャワーズ", "appear": 0, "moves": ["たいあたり", "かみつく"], "shiny": False},
    {"name": "イーブイ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/133.png", "base_stats": {'HP': 55, '攻撃': 55, '防御': 50, '特攻': 45, '特防': 65, '素早さ': 55}, "rarity": 1, "evolve_level": None, "evolves_to": "シャワーズ", "appear": 0, "moves": ["たいあたり", "かみつく"], "shiny": True},
    {"name": "シャワーズ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/134.png", "base_stats": {'HP': 130, '攻撃': 65, '防御': 60, '特攻': 110, '特防': 95, '素早さ': 65}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["みずでっぽう", "ハイドロポンプ"], "shiny": False},
    {"name": "シャワーズ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/134.png", "base_stats": {'HP': 130, '攻撃': 65, '防御': 60, '特攻': 110, '特防': 95, '素早さ': 65}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["みずでっぽう", "ハイドロポンプ"], "shiny": True},
    {"name": "サンダース", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/135.png", "base_stats": {'HP': 65, '攻撃': 65, '防御': 60, '特攻': 110, '特防': 95, '素早さ': 130}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["でんきショック", "10まんボルト"], "shiny": False},
    {"name": "サンダース", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/135.png", "base_stats": {'HP': 65, '攻撃': 65, '防御': 60, '特攻': 110, '特防': 95, '素早さ': 130}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["でんきショック", "10まんボルト"], "shiny": True},
    {"name": "ブースター", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/136.png", "base_stats": {'HP': 65, '攻撃': 130, '防御': 60, '特攻': 95, '特防': 110, '素早さ': 65}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かえんほうしゃ", "フレアドライブ"], "shiny": False},
    {"name": "ブースター", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/136.png", "base_stats": {'HP': 65, '攻撃': 130, '防御': 60, '特攻': 95, '特防': 110, '素早さ': 65}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["かえんほうしゃ", "フレアドライブ"], "shiny": True},
    {"name": "ポリゴン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png", "base_stats": {'HP': 65, '攻撃': 60, '防御': 70, '特攻': 85, '特防': 75, '素早さ': 40}, "rarity": 2, "evolve_level": None, "evolves_to": "ポリゴン２", "appear": 0, "moves": ["ねんりき", "トライアタック"], "shiny": False},
    {"name": "ポリゴン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/137.png", "base_stats": {'HP': 65, '攻撃': 60, '防御': 70, '特攻': 85, '特防': 75, '素早さ': 40}, "rarity": 2, "evolve_level": None, "evolves_to": "ポリゴン２", "appear": 0, "moves": ["ねんりき", "トライアタック"], "shiny": True},
    {"name": "オムナイト", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/138.png", "base_stats": {'HP': 35, '攻撃': 40, '防御': 100, '特攻': 90, '特防': 55, '素早さ': 35}, "rarity": 1, "evolve_level": 40, "evolves_to": "オムスター", "appear": 0, "moves": ["あわ", "げんしのちから"], "shiny": False},
    {"name": "オムナイト", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/138.png", "base_stats": {'HP': 35, '攻撃': 40, '防御': 100, '特攻': 90, '特防': 55, '素早さ': 35}, "rarity": 1, "evolve_level": 40, "evolves_to": "オムスター", "appear": 0, "moves": ["あわ", "げんしのちから"], "shiny": True},
    {"name": "オムスター", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/139.png", "base_stats": {'HP': 70, '攻撃': 60, '防御': 125, '特攻': 115, '特防': 70, '素早さ': 55}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ハイドロポンプ", "げんしのちから"], "shiny": False},
    {"name": "オムスター", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/139.png", "base_stats": {'HP': 70, '攻撃': 60, '防御': 125, '特攻': 115, '特防': 70, '素早さ': 55}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["ハイドロポンプ", "げんしのちから"], "shiny": True},
    {"name": "カブト", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/140.png", "base_stats": {'HP': 30, '攻撃': 80, '防御': 90, '特攻': 55, '特防': 45, '素早さ': 55}, "rarity": 1, "evolve_level": 40, "evolves_to": "カブトプス", "appear": 0, "moves": ["たいあたり", "げんしのちから"], "shiny": False},
    {"name": "カブト", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/140.png", "base_stats": {'HP': 30, '攻撃': 80, '防御': 90, '特攻': 55, '特防': 45, '素早さ': 55}, "rarity": 1, "evolve_level": 40, "evolves_to": "カブトプス", "appear": 0, "moves": ["たいあたり", "げんしのちから"], "shiny": True},
    {"name": "カブトプス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/141.png", "base_stats": {'HP': 60, '攻撃': 115, '防御': 105, '特攻': 65, '特防': 70, '素早さ': 80}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["つじぎり", "げんしのちから"], "shiny": False},
    {"name": "カブトプス", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/141.png", "base_stats": {'HP': 60, '攻撃': 115, '防御': 105, '特攻': 65, '特防': 70, '素早さ': 80}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["つじぎり", "げんしのちから"], "shiny": True},
    {"name": "プテラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/142.png", "base_stats": {'HP': 80, '攻撃': 105, '防御': 65, '特攻': 60, '特防': 75, '素早さ': 130}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["いわなだれ", "げんしのちから"], "shiny": False},
    {"name": "プテラ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/142.png", "base_stats": {'HP': 80, '攻撃': 105, '防御': 65, '特攻': 60, '特防': 75, '素早さ': 130}, "rarity": 2, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["いわなだれ", "げんしのちから"], "shiny": True},
    {"name": "カビゴン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png", "base_stats": {'HP': 160, '攻撃': 110, '防御': 65, '特攻': 65, '特防': 110, '素早さ': 30}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["のしかかり", "ねむる"], "shiny": False},
    {"name": "カビゴン", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/143.png", "base_stats": {'HP': 160, '攻撃': 110, '防御': 65, '特攻': 65, '特防': 110, '素早さ': 30}, "rarity": 3, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["のしかかり", "ねむる"], "shiny": True},
    {"name": "フリーザー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/144.png", "base_stats": {'HP': 90, '攻撃': 85, '防御': 100, '特攻': 95, '特防': 125, '素早さ': 85}, "rarity": 4, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "ふぶき"], "shiny": False},
    {"name": "フリーザー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/144.png", "base_stats": {'HP': 90, '攻撃': 85, '防御': 100, '特攻': 95, '特防': 125, '素早さ': 85}, "rarity": 4, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "ふぶき"], "shiny": True},
    {"name": "サンダー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png", "base_stats": {'HP': 90, '攻撃': 90, '防御': 85, '特攻': 125, '特防': 90, '素早さ': 100}, "rarity": 4, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "かみなり"], "shiny": False},
    {"name": "サンダー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/145.png", "base_stats": {'HP': 90, '攻撃': 90, '防御': 85, '特攻': 125, '特防': 90, '素早さ': 100}, "rarity": 4, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "かみなり"], "shiny": True},
    {"name": "ファイヤー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/146.png", "base_stats": {'HP': 90, '攻撃': 100, '防御': 90, '特攻': 125, '特防': 85, '素早さ': 90}, "rarity": 4, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "にらみつける"], "shiny": False},
    {"name": "ファイヤー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/146.png", "base_stats": {'HP': 90, '攻撃': 100, '防御': 90, '特攻': 125, '特防': 85, '素早さ': 90}, "rarity": 4, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["エアスラッシュ", "にらみつける"], "shiny": True},
    {"name": "ミニリュウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/147.png", "base_stats": {'HP': 41, '攻撃': 64, '防御': 45, '特攻': 50, '特防': 50, '素早さ': 50}, "rarity": 2, "evolve_level": 30, "evolves_to": "ハクリュー", "appear": 0, "moves": ["りゅうのいぶき"], "shiny": False},
    {"name": "ミニリュウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/147.png", "base_stats": {'HP': 41, '攻撃': 64, '防御': 45, '特攻': 50, '特防': 50, '素早さ': 50}, "rarity": 2, "evolve_level": 30, "evolves_to": "ハクリュー", "appear": 0, "moves": ["りゅうのいぶき"], "shiny": True},
    {"name": "ハクリュー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/148.png", "base_stats": {'HP': 61, '攻撃': 84, '防御': 65, '特攻': 70, '特防': 70, '素早さ': 70}, "rarity": 3, "evolve_level": 55, "evolves_to": "カイリュー", "appear": 0, "moves": ["りゅうのいぶき", "たつまき"], "shiny": False},
    {"name": "ハクリュー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/148.png", "base_stats": {'HP': 61, '攻撃': 84, '防御': 65, '特攻': 70, '特防': 70, '素早さ': 70}, "rarity": 3, "evolve_level": 55, "evolves_to": "カイリュー", "appear": 0, "moves": ["りゅうのいぶき", "たつまき"], "shiny": True},
    {"name": "カイリュー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png", "base_stats": {'HP': 91, '攻撃': 134, '防御': 95, '特攻': 100, '特防': 100, '素早さ': 80}, "rarity": 4, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["げきりん", "たつまき"], "shiny": False},
    {"name": "カイリュー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/149.png", "base_stats": {'HP': 91, '攻撃': 134, '防御': 95, '特攻': 100, '特防': 100, '素早さ': 80}, "rarity": 4, "evolve_level": None, "evolves_to": None, "appear": 1, "moves": ["げきりん", "たつまき"], "shiny": True},
    {"name": "ミュウツー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png", "base_stats": {'HP': 106, '攻撃': 110, '防御': 90, '特攻': 154, '特防': 90, '素早さ': 130}, "rarity": 6, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "じこさいせい"], "shiny": False},
    {"name": "ミュウツー", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/150.png", "base_stats": {'HP': 106, '攻撃': 110, '防御': 90, '特攻': 154, '特防': 90, '素早さ': 130}, "rarity": 6, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "じこさいせい"], "shiny": True},
    {"name": "ミュウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png", "base_stats": {'HP': 100, '攻撃': 100, '防御': 100, '特攻': 100, '特防': 100, '素早さ': 100}, "rarity": 5, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "へんしん"], "shiny": False},
    {"name": "ミュウ", "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/151.png", "base_stats": {'HP': 100, '攻撃': 100, '防御': 100, '特攻': 100, '特防': 100, '素早さ': 100}, "rarity": 5, "evolve_level": None, "evolves_to": None, "appear": 0, "moves": ["サイコキネシス", "へんしん"], "shiny": True},
    {
        "name": "チコリータ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/152.png",
        "base_stats": {
            "HP": 45,
            "攻撃": 49,
            "防御": 65,
            "特攻": 49,
            "特防": 65,
            "素早さ": 45
        },
        "rarity": 1,
        "evolve_level": 16,
        "evolves_to": "ベイリーフ",
        "appear": 1,
        "moves": [
            "たいあたり",
            "つるのムチ"
        ],
        "shiny": False
    },
    {
        "name": "チコリータ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/152.png",
        "base_stats": {
            "HP": 45,
            "攻撃": 49,
            "防御": 65,
            "特攻": 49,
            "特防": 65,
            "素早さ": 45
        },
        "rarity": 1,
        "evolve_level": 16,
        "evolves_to": "ベイリーフ",
        "appear": 1,
        "moves": [
            "たいあたり",
            "つるのムチ"
        ],
        "shiny": True
    },
    {
        "name": "ベイリーフ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/153.png",
        "base_stats": {
            "HP": 60,
            "攻撃": 62,
            "防御": 80,
            "特攻": 63,
            "特防": 80,
            "素早さ": 60
        },
        "rarity": 2,
        "evolve_level": 32,
        "evolves_to": "メガニウム",
        "appear": 1,
        "moves": [
            "マジカルリーフ",
            "リーフブレード"
        ],
        "shiny": False
    },
    {
        "name": "ベイリーフ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/153.png",
        "base_stats": {
            "HP": 60,
            "攻撃": 62,
            "防御": 80,
            "特攻": 63,
            "特防": 80,
            "素早さ": 60
        },
        "rarity": 2,
        "evolve_level": 32,
        "evolves_to": "メガニウム",
        "appear": 1,
        "moves": [
            "マジカルリーフ",
            "リーフブレード"
        ],
        "shiny": True
    },
    {
        "name": "メガニウム",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/154.png",
        "base_stats": {
            "HP": 80,
            "攻撃": 82,
            "防御": 100,
            "特攻": 83,
            "特防": 100,
            "素早さ": 80
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 1,
        "moves": [
            "ソーラービーム",
            "ギガドレイン"
        ],
        "shiny": False
    },
    {
        "name": "メガニウム",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/154.png",
        "base_stats": {
            "HP": 80,
            "攻撃": 82,
            "防御": 100,
            "特攻": 83,
            "特防": 100,
            "素早さ": 80
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 1,
        "moves": [
            "ソーラービーム",
            "ギガドレイン"
        ],
        "shiny": True
    },
    {
        "name": "ヒノアラシ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/155.png",
        "base_stats": {
            "HP": 39,
            "攻撃": 52,
            "防御": 43,
            "特攻": 60,
            "特防": 50,
            "素早さ": 65
        },
        "rarity": 1,
        "evolve_level": 14,
        "evolves_to": "マグマラシ",
        "appear": 1,
        "moves": [
            "ひのこ",
            "かえんほうしゃ"
        ],
        "shiny": False
    },
    {
        "name": "ヒノアラシ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/155.png",
        "base_stats": {
            "HP": 39,
            "攻撃": 52,
            "防御": 43,
            "特攻": 60,
            "特防": 50,
            "素早さ": 65
        },
        "rarity": 1,
        "evolve_level": 14,
        "evolves_to": "マグマラシ",
        "appear": 1,
        "moves": [
            "ひのこ",
            "かえんほうしゃ"
        ],
        "shiny": True
    },
    {
        "name": "マグマラシ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/156.png",
        "base_stats": {
            "HP": 58,
            "攻撃": 64,
            "防御": 58,
            "特攻": 80,
            "特防": 65,
            "素早さ": 80
        },
        "rarity": 2,
        "evolve_level": 36,
        "evolves_to": "バクフーン",
        "appear": 1,
        "moves": [
            "かえんほうしゃ",
            "ころがる"
        ],
        "shiny": False
    },
    {
        "name": "マグマラシ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/156.png",
        "base_stats": {
            "HP": 58,
            "攻撃": 64,
            "防御": 58,
            "特攻": 80,
            "特防": 65,
            "素早さ": 80
        },
        "rarity": 2,
        "evolve_level": 36,
        "evolves_to": "バクフーン",
        "appear": 1,
        "moves": [
            "かえんほうしゃ",
            "ころがる"
        ],
        "shiny": True
    },
    {
        "name": "バクフーン",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/157.png",
        "base_stats": {
            "HP": 78,
            "攻撃": 84,
            "防御": 78,
            "特攻": 109,
            "特防": 85,
            "素早さ": 100
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 1,
        "moves": [
            "フレアドライブ",
            "かみなりパンチ"
        ],
        "shiny": False
    },
    {
        "name": "バクフーン",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/157.png",
        "base_stats": {
            "HP": 78,
            "攻撃": 84,
            "防御": 78,
            "特攻": 109,
            "特防": 85,
            "素早さ": 100
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 1,
        "moves": [
            "フレアドライブ",
            "かみなりパンチ"
        ],
        "shiny": True
    },
    {
        "name": "ワニノコ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/158.png",
        "base_stats": {
            "HP": 50,
            "攻撃": 65,
            "防御": 64,
            "特攻": 44,
            "特防": 48,
            "素早さ": 43
        },
        "rarity": 1,
        "evolve_level": 18,
        "evolves_to": "アリゲイツ",
        "appear": 1,
        "moves": [
            "みずでっぽう",
            "アクアテール"
        ],
        "shiny": False
    },
    {
        "name": "ワニノコ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/158.png",
        "base_stats": {
            "HP": 50,
            "攻撃": 65,
            "防御": 64,
            "特攻": 44,
            "特防": 48,
            "素早さ": 43
        },
        "rarity": 1,
        "evolve_level": 18,
        "evolves_to": "アリゲイツ",
        "appear": 1,
        "moves": [
            "みずでっぽう",
            "アクアテール"
        ],
        "shiny": True
    },
    {
        "name": "アリゲイツ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/159.png",
        "base_stats": {
            "HP": 65,
            "攻撃": 80,
            "防御": 80,
            "特攻": 59,
            "特防": 63,
            "素早さ": 58
        },
        "rarity": 2,
        "evolve_level": 30,
        "evolves_to": "オーダイル",
        "appear": 1,
        "moves": [
            "かみつく",
            "アクアテール"
        ],
        "shiny": False
    },
    {
        "name": "アリゲイツ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/159.png",
        "base_stats": {
            "HP": 65,
            "攻撃": 80,
            "防御": 80,
            "特攻": 59,
            "特防": 63,
            "素早さ": 58
        },
        "rarity": 2,
        "evolve_level": 30,
        "evolves_to": "オーダイル",
        "appear": 1,
        "moves": [
            "かみつく",
            "アクアテール"
        ],
        "shiny": True
    },
    {
        "name": "オーダイル",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/160.png",
        "base_stats": {
            "HP": 85,
            "攻撃": 105,
            "防御": 100,
            "特攻": 79,
            "特防": 83,
            "素早さ": 78
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 1,
        "moves": [
            "ハイドロポンプ",
            "かみくだく"
        ],
        "shiny": False
    },
    {
        "name": "オーダイル",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/160.png",
        "base_stats": {
            "HP": 85,
            "攻撃": 105,
            "防御": 100,
            "特攻": 79,
            "特防": 83,
            "素早さ": 78
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 1,
        "moves": [
            "ハイドロポンプ",
            "かみくだく"
        ],
        "shiny": True
    },
    {
        "name": "オタチ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/161.png",
        "base_stats": {
            "HP": 35,
            "攻撃": 46,
            "防御": 34,
            "特攻": 35,
            "特防": 45,
            "素早さ": 20
        },
        "rarity": 1,
        "evolve_level": 15,
        "evolves_to": "オオタチ",
        "appear": 0,
        "moves": [
            "たいあたり",
            "かみつく"
        ],
        "shiny": False
    },
    {
        "name": "オタチ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/161.png",
        "base_stats": {
            "HP": 35,
            "攻撃": 46,
            "防御": 34,
            "特攻": 35,
            "特防": 45,
            "素早さ": 20
        },
        "rarity": 1,
        "evolve_level": 15,
        "evolves_to": "オオタチ",
        "appear": 0,
        "moves": [
            "たいあたり",
            "かみつく"
        ],
        "shiny": True
    },
    {
        "name": "オオタチ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/162.png",
        "base_stats": {
            "HP": 85,
            "攻撃": 76,
            "防御": 64,
            "特攻": 45,
            "特防": 55,
            "素早さ": 90
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "かみつく",
            "とっしん"
        ],
        "shiny": False
    },
    {
        "name": "オオタチ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/162.png",
        "base_stats": {
            "HP": 85,
            "攻撃": 76,
            "防御": 64,
            "特攻": 45,
            "特防": 55,
            "素早さ": 90
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "かみつく",
            "とっしん"
        ],
        "shiny": True
    },
    {
        "name": "ホーホー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/163.png",
        "base_stats": {
            "HP": 60,
            "攻撃": 30,
            "防御": 30,
            "特攻": 36,
            "特防": 56,
            "素早さ": 50
        },
        "rarity": 1,
        "evolve_level": 20,
        "evolves_to": "ヨルノズク",
        "appear": 0,
        "moves": [
            "たいあたり",
            "エアスラッシュ"
        ],
        "shiny": False
    },
    {
        "name": "ホーホー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/163.png",
        "base_stats": {
            "HP": 60,
            "攻撃": 30,
            "防御": 30,
            "特攻": 36,
            "特防": 56,
            "素早さ": 50
        },
        "rarity": 1,
        "evolve_level": 20,
        "evolves_to": "ヨルノズク",
        "appear": 0,
        "moves": [
            "たいあたり",
            "エアスラッシュ"
        ],
        "shiny": True
    },
    {
        "name": "ヨルノズク",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/164.png",
        "base_stats": {
            "HP": 100,
            "攻撃": 50,
            "防御": 50,
            "特攻": 86,
            "特防": 96,
            "素早さ": 70
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "エアスラッシュ",
            "ねんりき"
        ],
        "shiny": False
    },
    {
        "name": "ヨルノズク",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/164.png",
        "base_stats": {
            "HP": 100,
            "攻撃": 50,
            "防御": 50,
            "特攻": 86,
            "特防": 96,
            "素早さ": 70
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "エアスラッシュ",
            "ねんりき"
        ],
        "shiny": True
    },
    {
        "name": "レディバ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/165.png",
        "base_stats": {
            "HP": 40,
            "攻撃": 20,
            "防御": 30,
            "特攻": 40,
            "特防": 80,
            "素早さ": 55
        },
        "rarity": 1,
        "evolve_level": 18,
        "evolves_to": "レディアン",
        "appear": 0,
        "moves": [
            "たいあたり",
            "ぎんいろのかぜ"
        ],
        "shiny": False
    },
    {
        "name": "レディバ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/165.png",
        "base_stats": {
            "HP": 40,
            "攻撃": 20,
            "防御": 30,
            "特攻": 40,
            "特防": 80,
            "素早さ": 55
        },
        "rarity": 1,
        "evolve_level": 18,
        "evolves_to": "レディアン",
        "appear": 0,
        "moves": [
            "たいあたり",
            "ぎんいろのかぜ"
        ],
        "shiny": True
    },
    {
        "name": "レディアン",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/166.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 35,
            "防御": 50,
            "特攻": 55,
            "特防": 110,
            "素早さ": 85
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "ぎんいろのかぜ",
            "バトンタッチ"
        ],
        "shiny": False
    },
    {
        "name": "レディアン",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/166.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 35,
            "防御": 50,
            "特攻": 55,
            "特防": 110,
            "素早さ": 85
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "ぎんいろのかぜ",
            "バトンタッチ"
        ],
        "shiny": True
    },
    {
        "name": "イトマル",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/167.png",
        "base_stats": {
            "HP": 40,
            "攻撃": 60,
            "防御": 40,
            "特攻": 40,
            "特防": 40,
            "素早さ": 30
        },
        "rarity": 1,
        "evolve_level": 22,
        "evolves_to": "アリアドス",
        "appear": 0,
        "moves": [
            "どくばり",
            "かげぶんしん"
        ],
        "shiny": False
    },
    {
        "name": "イトマル",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/167.png",
        "base_stats": {
            "HP": 40,
            "攻撃": 60,
            "防御": 40,
            "特攻": 40,
            "特防": 40,
            "素早さ": 30
        },
        "rarity": 1,
        "evolve_level": 22,
        "evolves_to": "アリアドス",
        "appear": 0,
        "moves": [
            "どくばり",
            "かげぶんしん"
        ],
        "shiny": True
    },
    {
        "name": "アリアドス",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/168.png",
        "base_stats": {
            "HP": 70,
            "攻撃": 90,
            "防御": 70,
            "特攻": 60,
            "特防": 60,
            "素早さ": 40
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "どくばり",
            "シザークロス"
        ],
        "shiny": False
    },
    {
        "name": "アリアドス",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/168.png",
        "base_stats": {
            "HP": 70,
            "攻撃": 90,
            "防御": 70,
            "特攻": 60,
            "特防": 60,
            "素早さ": 40
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "どくばり",
            "シザークロス"
        ],
        "shiny": True
    },
    {
        "name": "クロバット",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/169.png",
        "base_stats": {
            "HP": 85,
            "攻撃": 90,
            "防御": 80,
            "特攻": 70,
            "特防": 80,
            "素早さ": 130
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "どくどく",
            "ブレイブバード"
        ],
        "shiny": False
    },
    {
        "name": "クロバット",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/169.png",
        "base_stats": {
            "HP": 85,
            "攻撃": 90,
            "防御": 80,
            "特攻": 70,
            "特防": 80,
            "素早さ": 130
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "どくどく",
            "ブレイブバード"
        ],
        "shiny": True
    },
    {
        "name": "チョンチー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/170.png",
        "base_stats": {
            "HP": 75,
            "攻撃": 38,
            "防御": 38,
            "特攻": 56,
            "特防": 56,
            "素早さ": 67
        },
        "rarity": 1,
        "evolve_level": 27,
        "evolves_to": "ランターン",
        "appear": 0,
        "moves": [
            "でんきショック",
            "あわ"
        ],
        "shiny": False
    },
    {
        "name": "チョンチー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/170.png",
        "base_stats": {
            "HP": 75,
            "攻撃": 38,
            "防御": 38,
            "特攻": 56,
            "特防": 56,
            "素早さ": 67
        },
        "rarity": 1,
        "evolve_level": 27,
        "evolves_to": "ランターン",
        "appear": 0,
        "moves": [
            "でんきショック",
            "あわ"
        ],
        "shiny": True
    },
    {
        "name": "ランターン",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/171.png",
        "base_stats": {
            "HP": 125,
            "攻撃": 58,
            "防御": 58,
            "特攻": 76,
            "特防": 76,
            "素早さ": 67
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "10まんボルト",
            "バブルこうせん"
        ],
        "shiny": False
    },
    {
        "name": "ランターン",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/171.png",
        "base_stats": {
            "HP": 125,
            "攻撃": 58,
            "防御": 58,
            "特攻": 76,
            "特防": 76,
            "素早さ": 67
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "10まんボルト",
            "バブルこうせん"
        ],
        "shiny": True
    },
    {
        "name": "ピチュー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/172.png",
        "base_stats": {
            "HP": 20,
            "攻撃": 40,
            "防御": 15,
            "特攻": 35,
            "特防": 35,
            "素早さ": 60
        },
        "rarity": 1,
        "evolve_level": None,
        "evolves_to": "ピカチュウ",
        "appear": 0,
        "moves": [
            "でんきショック",
            "てんしのキッス"
        ],
        "shiny": False
    },
    {
        "name": "ピチュー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/172.png",
        "base_stats": {
            "HP": 20,
            "攻撃": 40,
            "防御": 15,
            "特攻": 35,
            "特防": 35,
            "素早さ": 60
        },
        "rarity": 1,
        "evolve_level": None,
        "evolves_to": "ピカチュウ",
        "appear": 0,
        "moves": [
            "でんきショック",
            "てんしのキッス"
        ],
        "shiny": True
    },
    {
        "name": "ピィ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/173.png",
        "base_stats": {
            "HP": 50,
            "攻撃": 25,
            "防御": 28,
            "特攻": 45,
            "特防": 55,
            "素早さ": 15
        },
        "rarity": 1,
        "evolve_level": None,
        "evolves_to": "ピッピ",
        "appear": 0,
        "moves": [
            "ゆびをふる"
        ],
        "shiny": False
    },
    {
        "name": "ピィ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/173.png",
        "base_stats": {
            "HP": 50,
            "攻撃": 25,
            "防御": 28,
            "特攻": 45,
            "特防": 55,
            "素早さ": 15
        },
        "rarity": 1,
        "evolve_level": None,
        "evolves_to": "ピッピ",
        "appear": 0,
        "moves": [
            "ゆびをふる"
        ],
        "shiny": True
    },
    {
        "name": "ププリン",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/174.png",
        "base_stats": {
            "HP": 90,
            "攻撃": 30,
            "防御": 15,
            "特攻": 40,
            "特防": 20,
            "素早さ": 15
        },
        "rarity": 1,
        "evolve_level": None,
        "evolves_to": "プリン",
        "appear": 0,
        "moves": [
            "はたく",
            "うたう"
        ],
        "shiny": False
    },
    {
        "name": "ププリン",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/174.png",
        "base_stats": {
            "HP": 90,
            "攻撃": 30,
            "防御": 15,
            "特攻": 40,
            "特防": 20,
            "素早さ": 15
        },
        "rarity": 1,
        "evolve_level": None,
        "evolves_to": "プリン",
        "appear": 0,
        "moves": [
            "はたく",
            "うたう"
        ],
        "shiny": True
    },
    {
        "name": "トゲピー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png",
        "base_stats": {
            "HP": 35,
            "攻撃": 20,
            "防御": 65,
            "特攻": 40,
            "特防": 65,
            "素早さ": 20
        },
        "rarity": 1,
        "evolve_level": None,
        "evolves_to": "トゲチック",
        "appear": 0,
        "moves": [
            "はねる",
            "ゆびをふる"
        ],
        "shiny": False
    },
    {
        "name": "トゲピー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/175.png",
        "base_stats": {
            "HP": 35,
            "攻撃": 20,
            "防御": 65,
            "特攻": 40,
            "特防": 65,
            "素早さ": 20
        },
        "rarity": 1,
        "evolve_level": None,
        "evolves_to": "トゲチック",
        "appear": 0,
        "moves": [
            "はねる",
            "ゆびをふる"
        ],
        "shiny": True
    },
    {
        "name": "トゲチック",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/176.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 40,
            "防御": 85,
            "特攻": 80,
            "特防": 105,
            "素早さ": 40
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": "トゲキッス",
        "appear": 0,
        "moves": [
            "ゆびをふる",
            "エアスラッシュ"
        ],
        "shiny": False
    },
    {
        "name": "トゲチック",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/176.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 40,
            "防御": 85,
            "特攻": 80,
            "特防": 105,
            "素早さ": 40
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": "トゲキッス",
        "appear": 0,
        "moves": [
            "ゆびをふる",
            "エアスラッシュ"
        ],
        "shiny": True
    },
    {
        "name": "ネイティ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/177.png",
        "base_stats": {
            "HP": 40,
            "攻撃": 50,
            "防御": 45,
            "特攻": 70,
            "特防": 45,
            "素早さ": 70
        },
        "rarity": 1,
        "evolve_level": 25,
        "evolves_to": "ネイティオ",
        "appear": 0,
        "moves": [
            "サイケこうせん",
            "つばめがえし"
        ],
        "shiny": False
    },
    {
        "name": "ネイティ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/177.png",
        "base_stats": {
            "HP": 40,
            "攻撃": 50,
            "防御": 45,
            "特攻": 70,
            "特防": 45,
            "素早さ": 70
        },
        "rarity": 1,
        "evolve_level": 25,
        "evolves_to": "ネイティオ",
        "appear": 0,
        "moves": [
            "サイケこうせん",
            "つばめがえし"
        ],
        "shiny": True
    },
    {
        "name": "ネイティオ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/178.png",
        "base_stats": {
            "HP": 65,
            "攻撃": 75,
            "防御": 70,
            "特攻": 95,
            "特防": 70,
            "素早さ": 95
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "サイコキネシス",
            "エアスラッシュ"
        ],
        "shiny": False
    },
    {
        "name": "ネイティオ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/178.png",
        "base_stats": {
            "HP": 65,
            "攻撃": 75,
            "防御": 70,
            "特攻": 95,
            "特防": 70,
            "素早さ": 95
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "サイコキネシス",
            "エアスラッシュ"
        ],
        "shiny": True
    },
    {
        "name": "メリープ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/179.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 40,
            "防御": 40,
            "特攻": 65,
            "特防": 45,
            "素早さ": 35
        },
        "rarity": 1,
        "evolve_level": 15,
        "evolves_to": "モココ",
        "appear": 0,
        "moves": [
            "でんきショック",
            "ひかりのかべ"
        ],
        "shiny": False
    },
    {
        "name": "メリープ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/179.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 40,
            "防御": 40,
            "特攻": 65,
            "特防": 45,
            "素早さ": 35
        },
        "rarity": 1,
        "evolve_level": 15,
        "evolves_to": "モココ",
        "appear": 0,
        "moves": [
            "でんきショック",
            "ひかりのかべ"
        ],
        "shiny": True
    },
    {
        "name": "モココ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/180.png",
        "base_stats": {
            "HP": 70,
            "攻撃": 55,
            "防御": 55,
            "特攻": 80,
            "特防": 60,
            "素早さ": 45
        },
        "rarity": 2,
        "evolve_level": 30,
        "evolves_to": "デンリュウ",
        "appear": 0,
        "moves": [
            "でんきショック",
            "かみなりパンチ"
        ],
        "shiny": False
    },
    {
        "name": "モココ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/180.png",
        "base_stats": {
            "HP": 70,
            "攻撃": 55,
            "防御": 55,
            "特攻": 80,
            "特防": 60,
            "素早さ": 45
        },
        "rarity": 2,
        "evolve_level": 30,
        "evolves_to": "デンリュウ",
        "appear": 0,
        "moves": [
            "でんきショック",
            "かみなりパンチ"
        ],
        "shiny": True
    },
    {
        "name": "デンリュウ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/181.png",
        "base_stats": {
            "HP": 90,
            "攻撃": 75,
            "防御": 85,
            "特攻": 115,
            "特防": 90,
            "素早さ": 55
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "かみなりパンチ",
            "かみなり"
        ],
        "shiny": False
    },
    {
        "name": "デンリュウ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/181.png",
        "base_stats": {
            "HP": 90,
            "攻撃": 75,
            "防御": 85,
            "特攻": 115,
            "特防": 90,
            "素早さ": 55
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "かみなりパンチ",
            "かみなり"
        ],
        "shiny": True
    },
    {
        "name": "キレイハナ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/182.png",
        "base_stats": {
            "HP": 75,
            "攻撃": 80,
            "防御": 95,
            "特攻": 90,
            "特防": 100,
            "素早さ": 50
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "ソーラービーム",
            "マジカルリーフ"
        ],
        "shiny": False
    },
    {
        "name": "キレイハナ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/182.png",
        "base_stats": {
            "HP": 75,
            "攻撃": 80,
            "防御": 95,
            "特攻": 90,
            "特防": 100,
            "素早さ": 50
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "ソーラービーム",
            "マジカルリーフ"
        ],
        "shiny": True
    },
    {
        "name": "マリル",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/183.png",
        "base_stats": {
            "HP": 70,
            "攻撃": 20,
            "防御": 50,
            "特攻": 20,
            "特防": 50,
            "素早さ": 40
        },
        "rarity": 1,
        "evolve_level": 18,
        "evolves_to": "マリルリ",
        "appear": 0,
        "moves": [
            "あわ",
            "たいあたり"
        ],
        "shiny": False
    },
    {
        "name": "マリル",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/183.png",
        "base_stats": {
            "HP": 70,
            "攻撃": 20,
            "防御": 50,
            "特攻": 20,
            "特防": 50,
            "素早さ": 40
        },
        "rarity": 1,
        "evolve_level": 18,
        "evolves_to": "マリルリ",
        "appear": 0,
        "moves": [
            "あわ",
            "たいあたり"
        ],
        "shiny": True
    },
    {
        "name": "マリルリ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/184.png",
        "base_stats": {
            "HP": 100,
            "攻撃": 50,
            "防御": 80,
            "特攻": 60,
            "特防": 80,
            "素早さ": 50
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "たきのぼり",
            "はたく"
        ],
        "shiny": False
    },
    {
        "name": "マリルリ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/184.png",
        "base_stats": {
            "HP": 100,
            "攻撃": 50,
            "防御": 80,
            "特攻": 60,
            "特防": 80,
            "素早さ": 50
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "たきのぼり",
            "はたく"
        ],
        "shiny": True
    },
    {
        "name": "ウソッキー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/185.png",
        "base_stats": {
            "HP": 70,
            "攻撃": 100,
            "防御": 115,
            "特攻": 30,
            "特防": 65,
            "素早さ": 30
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "タネマシンガン",
            "いわおとし"
        ],
        "shiny": False
    },
    {
        "name": "ウソッキー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/185.png",
        "base_stats": {
            "HP": 70,
            "攻撃": 100,
            "防御": 115,
            "特攻": 30,
            "特防": 65,
            "素早さ": 30
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "タネマシンガン",
            "いわおとし"
        ],
        "shiny": True
    },
    {
        "name": "ニョロトノ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/186.png",
        "base_stats": {
            "HP": 90,
            "攻撃": 75,
            "防御": 75,
            "特攻": 90,
            "特防": 100,
            "素早さ": 70
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "ハイドロポンプ",
            "かげぶんしん"
        ],
        "shiny": False
    },
    {
        "name": "ニョロトノ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/186.png",
        "base_stats": {
            "HP": 90,
            "攻撃": 75,
            "防御": 75,
            "特攻": 90,
            "特防": 100,
            "素早さ": 70
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "ハイドロポンプ",
            "かげぶんしん"
        ],
        "shiny": True
    },
    {
        "name": "ハネッコ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/187.png",
        "base_stats": {
            "HP": 35,
            "攻撃": 35,
            "防御": 40,
            "特攻": 35,
            "特防": 55,
            "素早さ": 50
        },
        "rarity": 1,
        "evolve_level": 18,
        "evolves_to": "ポポッコ",
        "appear": 0,
        "moves": [
            "タネマシンガン",
            "たいあたり"
        ],
        "shiny": False
    },
    {
        "name": "ハネッコ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/187.png",
        "base_stats": {
            "HP": 35,
            "攻撃": 35,
            "防御": 40,
            "特攻": 35,
            "特防": 55,
            "素早さ": 50
        },
        "rarity": 1,
        "evolve_level": 18,
        "evolves_to": "ポポッコ",
        "appear": 0,
        "moves": [
            "タネマシンガン",
            "たいあたり"
        ],
        "shiny": True
    },
    {
        "name": "ポポッコ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/188.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 45,
            "防御": 50,
            "特攻": 45,
            "特防": 65,
            "素早さ": 80
        },
        "rarity": 2,
        "evolve_level": 27,
        "evolves_to": "ワタッコ",
        "appear": 0,
        "moves": [
            "はっぱカッター",
            "たいあたり"
        ],
        "shiny": False
    },
    {
        "name": "ポポッコ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/188.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 45,
            "防御": 50,
            "特攻": 45,
            "特防": 65,
            "素早さ": 80
        },
        "rarity": 2,
        "evolve_level": 27,
        "evolves_to": "ワタッコ",
        "appear": 0,
        "moves": [
            "はっぱカッター",
            "たいあたり"
        ],
        "shiny": True
    },
    {
        "name": "ワタッコ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/189.png",
        "base_stats": {
            "HP": 75,
            "攻撃": 55,
            "防御": 70,
            "特攻": 55,
            "特防": 95,
            "素早さ": 110
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "はっぱカッター",
            "ソーラービーム"
        ],
        "shiny": False
    },
    {
        "name": "ワタッコ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/189.png",
        "base_stats": {
            "HP": 75,
            "攻撃": 55,
            "防御": 70,
            "特攻": 55,
            "特防": 95,
            "素早さ": 110
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "はっぱカッター",
            "ソーラービーム"
        ],
        "shiny": True
    },
    {
        "name": "エイパム",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/190.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 70,
            "防御": 55,
            "特攻": 40,
            "特防": 55,
            "素早さ": 85
        },
        "rarity": 1,
        "evolve_level": 32,
        "evolves_to": "エテボース",
        "appear": 0,
        "moves": [
            "ひっかく",
            "はたく"
        ],
        "shiny": False
    },
    {
        "name": "エイパム",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/190.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 70,
            "防御": 55,
            "特攻": 40,
            "特防": 55,
            "素早さ": 85
        },
        "rarity": 1,
        "evolve_level": 32,
        "evolves_to": "エテボース",
        "appear": 0,
        "moves": [
            "ひっかく",
            "はたく"
        ],
        "shiny": True
    },
    {
        "name": "ヒマナッツ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/191.png",
        "base_stats": {
            "HP": 30,
            "攻撃": 30,
            "防御": 30,
            "特攻": 30,
            "特防": 30,
            "素早さ": 30
        },
        "rarity": 1,
        "evolve_level": 25,
        "evolves_to": "キマワリ",
        "appear": 0,
        "moves": [
            "たいあたり",
            "タネマシンガン"
        ],
        "shiny": False
    },
    {
        "name": "ヒマナッツ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/191.png",
        "base_stats": {
            "HP": 30,
            "攻撃": 30,
            "防御": 30,
            "特攻": 30,
            "特防": 30,
            "素早さ": 30
        },
        "rarity": 1,
        "evolve_level": 25,
        "evolves_to": "キマワリ",
        "appear": 0,
        "moves": [
            "たいあたり",
            "タネマシンガン"
        ],
        "shiny": True
    },
    {
        "name": "キマワリ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/192.png",
        "base_stats": {
            "HP": 75,
            "攻撃": 75,
            "防御": 55,
            "特攻": 105,
            "特防": 85,
            "素早さ": 30
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "ソーラービーム",
            "タネマシンガン"
        ],
        "shiny": False
    },
    {
        "name": "キマワリ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/192.png",
        "base_stats": {
            "HP": 75,
            "攻撃": 75,
            "防御": 55,
            "特攻": 105,
            "特防": 85,
            "素早さ": 30
        },
        "rarity": 2,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "ソーラービーム",
            "タネマシンガン"
        ],
        "shiny": True
    },
    {
        "name": "ヤンヤンマ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/193.png",
        "base_stats": {
            "HP": 65,
            "攻撃": 65,
            "防御": 45,
            "特攻": 75,
            "特防": 45,
            "素早さ": 95
        },
        "rarity": 1,
        "evolve_level": 33,
        "evolves_to": "メガヤンマ",
        "appear": 0,
        "moves": [
            "エアスラッシュ",
            "かげぶんしん"
        ],
        "shiny": False
    },
    {
        "name": "ヤンヤンマ",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/193.png",
        "base_stats": {
            "HP": 65,
            "攻撃": 65,
            "防御": 45,
            "特攻": 75,
            "特防": 45,
            "素早さ": 95
        },
        "rarity": 1,
        "evolve_level": 33,
        "evolves_to": "メガヤンマ",
        "appear": 0,
        "moves": [
            "エアスラッシュ",
            "かげぶんしん"
        ],
        "shiny": True
    },
    {
        "name": "ウパー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/194.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 45,
            "防御": 45,
            "特攻": 25,
            "特防": 25,
            "素早さ": 15
        },
        "rarity": 1,
        "evolve_level": 20,
        "evolves_to": "ヌオー",
        "appear": 0,
        "moves": [
            "みずでっぽう",
            "あわ"
        ],
        "shiny": False
    },
    {
        "name": "ウパー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/194.png",
        "base_stats": {
            "HP": 55,
            "攻撃": 45,
            "防御": 45,
            "特攻": 25,
            "特防": 25,
            "素早さ": 15
        },
        "rarity": 1,
        "evolve_level": 20,
        "evolves_to": "ヌオー",
        "appear": 0,
        "moves": [
            "みずでっぽう",
            "あわ"
        ],
        "shiny": True
    },
    {
        "name": "ヌオー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/195.png",
        "base_stats": {
            "HP": 95,
            "攻撃": 85,
            "防御": 85,
            "特攻": 65,
            "特防": 65,
            "素早さ": 35
        },
        "rarity": 3,
        "evolve_level": None,
        "evolves_to": None,
        "appear": 0,
        "moves": [
            "みずでっぽう",
            "じしん"
        ],
        "shiny": False
    },
    {
        "name": "ヌオー",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/195.png",
        "base_stats": {
            "HP": 95,
            "攻撃": 85,
            "防御": 85,
            "特攻": 65,
            "特防": 65,
            "素早さ": 35
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "みずでっぽう",
            "じしん"
            ],
            "shiny": True
            },
            {
            "name": "エーフィ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/196.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 65,
            "防御": 60,
            "特攻": 130,
            "特防": 95,
            "素早さ": 110
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "サイコキネシス",
            "ねんりき"
            ],
            "shiny": False
            },
            {
            "name": "エーフィ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/196.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 65,
            "防御": 60,
            "特攻": 130,
            "特防": 95,
            "素早さ": 110
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "サイコキネシス",
            "ねんりき"
            ],
            "shiny": True
            },
            {
            "name": "ブラッキー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/197.png",
            "base_stats": {
            "HP": 95,
            "攻撃": 65,
            "防御": 110,
            "特攻": 60,
            "特防": 130,
            "素早さ": 65
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "イカサマ",
            "かみくだく"
            ],
            "shiny": False
            },
            {
            "name": "ブラッキー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/197.png",
            "base_stats": {
            "HP": 95,
            "攻撃": 65,
            "防御": 110,
            "特攻": 60,
            "特防": 130,
            "素早さ": 65
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "イカサマ",
            "かみくだく"
            ],
            "shiny": True
            },
            {
            "name": "ヤミカラス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/198.png",
            "base_stats": {
            "HP": 60,
            "攻撃": 85,
            "防御": 42,
            "特攻": 85,
            "特防": 42,
            "素早さ": 91
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "ドンカラス",
            "appear": 0,
            "moves": [
            "つじぎり",
            "つばめがえし"
            ],
            "shiny": False
            },
            {
            "name": "ヤミカラス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/198.png",
            "base_stats": {
            "HP": 60,
            "攻撃": 85,
            "防御": 42,
            "特攻": 85,
            "特防": 42,
            "素早さ": 91
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "ドンカラス",
            "appear": 0,
            "moves": [
            "つじぎり",
            "つばめがえし"
            ],
            "shiny": True
            },
            {
            "name": "ヤドキング",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/199.png",
            "base_stats": {
            "HP": 95,
            "攻撃": 75,
            "防御": 80,
            "特攻": 100,
            "特防": 110,
            "素早さ": 30
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "サイコキネシス",
            "なみのり"
            ],
            "shiny": False
            },
            {
            "name": "ヤドキング",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/199.png",
            "base_stats": {
            "HP": 95,
            "攻撃": 75,
            "防御": 80,
            "特攻": 100,
            "特防": 110,
            "素早さ": 30
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "サイコキネシス",
            "なみのり"
            ],
            "shiny": True
            },
            {
            "name": "ムウマ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/200.png",
            "base_stats": {
            "HP": 60,
            "攻撃": 60,
            "防御": 60,
            "特攻": 85,
            "特防": 85,
            "素早さ": 85
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "ムウマージ",
            "appear": 0,
            "moves": [
            "シャドーボール",
            "おにび"
            ],
            "shiny": False
            },
            {
            "name": "ムウマ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/200.png",
            "base_stats": {
            "HP": 60,
            "攻撃": 60,
            "防御": 60,
            "特攻": 85,
            "特防": 85,
            "素早さ": 85
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "ムウマージ",
            "appear": 0,
            "moves": [
            "シャドーボール",
            "おにび"
            ],
            "shiny": True
            },
            {
            "name": "アンノーン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/201.png",
            "base_stats": {
            "HP": 48,
            "攻撃": 72,
            "防御": 48,
            "特攻": 72,
            "特防": 48,
            "素早さ": 48
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "めざめるパワー"
            ],
            "shiny": False
            },
            {
            "name": "アンノーン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/201.png",
            "base_stats": {
            "HP": 48,
            "攻撃": 72,
            "防御": 48,
            "特攻": 72,
            "特防": 48,
            "素早さ": 48
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "めざめるパワー"
            ],
            "shiny": True
            },
            {
            "name": "ソーナンス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/202.png",
            "base_stats": {
            "HP": 190,
            "攻撃": 33,
            "防御": 58,
            "特攻": 33,
            "特防": 58,
            "素早さ": 33
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "カウンター",
            "ミラーコート"
            ],
            "shiny": False
            },
            {
            "name": "ソーナンス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/202.png",
            "base_stats": {
            "HP": 190,
            "攻撃": 33,
            "防御": 58,
            "特攻": 33,
            "特防": 58,
            "素早さ": 33
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "カウンター",
            "ミラーコート"
            ],
            "shiny": True
            },
            {
            "name": "キリンリキ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/203.png",
            "base_stats": {
            "HP": 70,
            "攻撃": 80,
            "防御": 65,
            "特攻": 90,
            "特防": 65,
            "素早さ": 85
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "リキキリン",
            "appear": 0,
            "moves": [
            "ねんりき",
            "かみつく"
            ],
            "shiny": False
            },
            {
            "name": "キリンリキ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/203.png",
            "base_stats": {
            "HP": 70,
            "攻撃": 80,
            "防御": 65,
            "特攻": 90,
            "特防": 65,
            "素早さ": 85
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "リキキリン",
            "appear": 0,
            "moves": [
            "ねんりき",
            "かみつく"
            ],
            "shiny": True
            },
            {
            "name": "クヌギダマ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/204.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 65,
            "防御": 90,
            "特攻": 35,
            "特防": 35,
            "素早さ": 15
            },
            "rarity": 1,
            "evolve_level": 31,
            "evolves_to": "フォレトス",
            "appear": 0,
            "moves": [
            "とっしん",
            "てっぺき"
            ],
            "shiny": False
            },
            {
            "name": "クヌギダマ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/204.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 65,
            "防御": 90,
            "特攻": 35,
            "特防": 35,
            "素早さ": 15
            },
            "rarity": 1,
            "evolve_level": 31,
            "evolves_to": "フォレトス",
            "appear": 0,
            "moves": [
            "とっしん",
            "てっぺき"
            ],
            "shiny": True
            },
            {
            "name": "フォレトス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/205.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 90,
            "防御": 140,
            "特攻": 60,
            "特防": 60,
            "素早さ": 40
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "だいばくはつ",
            "ミラーショット"
            ],
            "shiny": False
            },
            {
            "name": "フォレトス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/205.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 90,
            "防御": 140,
            "特攻": 60,
            "特防": 60,
            "素早さ": 40
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "だいばくはつ",
            "ミラーショット"
            ],
            "shiny": True
            },
            {
            "name": "ノコッチ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/206.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 70,
            "防御": 70,
            "特攻": 65,
            "特防": 65,
            "素早さ": 45
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": "ノココッチ",
            "appear": 0,
            "moves": [
            "のしかかり",
            "とっしん"
            ],
            "shiny": False
            },
            {
            "name": "ノコッチ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/206.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 70,
            "防御": 70,
            "特攻": 65,
            "特防": 65,
            "素早さ": 45
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": "ノココッチ",
            "appear": 0,
            "moves": [
            "のしかかり",
            "とっしん"
            ],
            "shiny": True
            },
            {
            "name": "グライガー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/207.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 75,
            "防御": 105,
            "特攻": 35,
            "特防": 65,
            "素早さ": 85
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "グライオン",
            "appear": 0,
            "moves": [
            "どくばり",
            "つばめがえし"
            ],
            "shiny": False
            },
            {
            "name": "グライガー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/207.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 75,
            "防御": 105,
            "特攻": 35,
            "特防": 65,
            "素早さ": 85
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "グライオン",
            "appear": 0,
            "moves": [
            "どくばり",
            "つばめがえし"
            ],
            "shiny": True
            },
            {
            "name": "ハガネール",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/208.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 85,
            "防御": 200,
            "特攻": 55,
            "特防": 65,
            "素早さ": 30
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "アイアンテール",
            "ストーンエッジ"
            ],
            "shiny": False
            },
            {
            "name": "ハガネール",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/208.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 85,
            "防御": 200,
            "特攻": 55,
            "特防": 65,
            "素早さ": 30
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "アイアンテール",
            "ストーンエッジ"
            ],
            "shiny": True
            },
            {
            "name": "ブルー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/209.png",
            "base_stats": {
            "HP": 60,
            "攻撃": 80,
            "防御": 50,
            "特攻": 40,
            "特防": 40,
            "素早さ": 30
            },
            "rarity": 1,
            "evolve_level": 23,
            "evolves_to": "グランブル",
            "appear": 0,
            "moves": [
            "かみつく",
            "はたく"
            ],
            "shiny": False
            },
            {
            "name": "ブルー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/209.png",
            "base_stats": {
            "HP": 60,
            "攻撃": 80,
            "防御": 50,
            "特攻": 40,
            "特防": 40,
            "素早さ": 30
            },
            "rarity": 1,
            "evolve_level": 23,
            "evolves_to": "グランブル",
            "appear": 0,
            "moves": [
            "かみつく",
            "はたく"
            ],
            "shiny": True
            },
            {
            "name": "グランブル",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/210.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 120,
            "防御": 75,
            "特攻": 60,
            "特防": 60,
            "素早さ": 45
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かみくだく",
            "はたく"
            ],
            "shiny": False
            },
            {
            "name": "グランブル",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/210.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 120,
            "防御": 75,
            "特攻": 60,
            "特防": 60,
            "素早さ": 45
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かみくだく",
            "はたく"
            ],
            "shiny": True
            },
            {
            "name": "ハリーセン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/211.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 95,
            "防御": 85,
            "特攻": 55,
            "特防": 55,
            "素早さ": 85
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "ハリーマン",
            "appear": 0,
            "moves": [
            "どくばり",
            "アクアジェット"
            ],
            "shiny": False
            },
            {
            "name": "ハリーセン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/211.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 95,
            "防御": 85,
            "特攻": 55,
            "特防": 55,
            "素早さ": 85
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "ハリーマン",
            "appear": 0,
            "moves": [
            "どくばり",
            "アクアジェット"
            ],
            "shiny": True
            },
            {
            "name": "ハッサム",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/212.png",
            "base_stats": {
            "HP": 70,
            "攻撃": 130,
            "防御": 100,
            "特攻": 55,
            "特防": 80,
            "素早さ": 65
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "バレットパンチ",
            "シザークロス"
            ],
            "shiny": False
            },
            {
            "name": "ハッサム",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/212.png",
            "base_stats": {
            "HP": 70,
            "攻撃": 130,
            "防御": 100,
            "特攻": 55,
            "特防": 80,
            "素早さ": 65
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "バレットパンチ",
            "シザークロス"
            ],
            "shiny": True
            },
            {
            "name": "ツボツボ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/213.png",
            "base_stats": {
            "HP": 20,
            "攻撃": 10,
            "防御": 230,
            "特攻": 10,
            "特防": 230,
            "素早さ": 5
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "ころがる",
            "しっぽをふる"
            ],
            "shiny": False
            },
            {
            "name": "ツボツボ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/213.png",
            "base_stats": {
            "HP": 20,
            "攻撃": 10,
            "防御": 230,
            "特攻": 10,
            "特防": 230,
            "素早さ": 5
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "ころがる",
            "しっぽをふる"
            ],
            "shiny": True
            },
            {
            "name": "ヘラクロス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/214.png",
            "base_stats": {
            "HP": 80,
            "攻撃": 125,
            "防御": 75,
            "特攻": 40,
            "特防": 95,
            "素早さ": 85
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "インファイト",
            "メガホーン"
            ],
            "shiny": False
            },
            {
            "name": "ヘラクロス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/214.png",
            "base_stats": {
            "HP": 80,
            "攻撃": 125,
            "防御": 75,
            "特攻": 40,
            "特防": 95,
            "素早さ": 85
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "インファイト",
            "メガホーン"
            ],
            "shiny": True
            },
            {
            "name": "ニューラ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/215.png",
            "base_stats": {
            "HP": 55,
            "攻撃": 95,
            "防御": 55,
            "特攻": 35,
            "特防": 75,
            "素早さ": 115
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": "マニューラ",
            "appear": 0,
            "moves": [
            "つじぎり",
            "こおりのつぶて"
            ],
            "shiny": False
            },
            {
            "name": "ニューラ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/215.png",
            "base_stats": {
            "HP": 55,
            "攻撃": 95,
            "防御": 55,
            "特攻": 35,
            "特防": 75,
            "素早さ": 115
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": "マニューラ",
            "appear": 0,
            "moves": [
            "つじぎり",
            "こおりのつぶて"
            ],
            "shiny": True
            },
            {
            "name": "ヒメグマ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/216.png",
            "base_stats": {
            "HP": 60,
            "攻撃": 80,
            "防御": 50,
            "特攻": 50,
            "特防": 50,
            "素早さ": 40
            },
            "rarity": 1,
            "evolve_level": 30,
            "evolves_to": "リングマ",
            "appear": 0,
            "moves": [
            "はたく",
            "なきごえ"
            ],
            "shiny": False
            },
            {
            "name": "ヒメグマ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/216.png",
            "base_stats": {
            "HP": 60,
            "攻撃": 80,
            "防御": 50,
            "特攻": 50,
            "特防": 50,
            "素早さ": 40
            },
            "rarity": 1,
            "evolve_level": 30,
            "evolves_to": "リングマ",
            "appear": 0,
            "moves": [
            "はたく",
            "なきごえ"
            ],
            "shiny": True
            },
            {
            "name": "リングマ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/217.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 130,
            "防御": 75,
            "特攻": 75,
            "特防": 75,
            "素早さ": 55
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 1,
            "moves": [
            "じしん",
            "きあいだま"
            ],
            "shiny": False
            },
            {
            "name": "リングマ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/217.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 130,
            "防御": 75,
            "特攻": 75,
            "特防": 75,
            "素早さ": 55
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 1,
            "moves": [
            "じしん",
            "きあいだま"
            ],
            "shiny": True
            },
            {
            "name": "マグマッグ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/218.png",
            "base_stats": {
            "HP": 40,
            "攻撃": 40,
            "防御": 40,
            "特攻": 70,
            "特防": 40,
            "素早さ": 20
            },
            "rarity": 1,
            "evolve_level": 38,
            "evolves_to": "マグカルゴ",
            "appear": 0,
            "moves": [
            "ひのこ",
            "いわおとし"
            ],
            "shiny": False
            },
            {
            "name": "マグマッグ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/218.png",
            "base_stats": {
            "HP": 40,
            "攻撃": 40,
            "防御": 40,
            "特攻": 70,
            "特防": 40,
            "素早さ": 20
            },
            "rarity": 1,
            "evolve_level": 38,
            "evolves_to": "マグカルゴ",
            "appear": 0,
            "moves": [
            "ひのこ",
            "いわおとし"
            ],
            "shiny": True
            },
            {
            "name": "マグカルゴ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/219.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 50,
            "防御": 120,
            "特攻": 80,
            "特防": 80,
            "素早さ": 30
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かえんほうしゃ",
            "ストーンエッジ"
            ],
            "shiny": False
            },
            {
            "name": "マグカルゴ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/219.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 50,
            "防御": 120,
            "特攻": 80,
            "特防": 80,
            "素早さ": 30
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かえんほうしゃ",
            "ストーンエッジ"
            ],
            "shiny": True
            },
            {
            "name": "ウリムー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/220.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 50,
            "防御": 40,
            "特攻": 30,
            "特防": 30,
            "素早さ": 50
            },
            "rarity": 1,
            "evolve_level": 33,
            "evolves_to": "イノムー",
            "appear": 0,
            "moves": [
            "こなゆき",
            "いわおとし"
            ],
            "shiny": False
            },
            {
            "name": "ウリムー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/220.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 50,
            "防御": 40,
            "特攻": 30,
            "特防": 30,
            "素早さ": 50
            },
            "rarity": 1,
            "evolve_level": 33,
            "evolves_to": "イノムー",
            "appear": 0,
            "moves": [
            "こなゆき",
            "いわおとし"
            ],
            "shiny": True
            },
            {
            "name": "イノムー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/221.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 100,
            "防御": 80,
            "特攻": 60,
            "特防": 60,
            "素早さ": 50
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": "マンムー",
            "appear": 0,
            "moves": [
            "こなゆき",
            "じしん"
            ],
            "shiny": False
            },
            {
            "name": "イノムー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/221.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 100,
            "防御": 80,
            "特攻": 60,
            "特防": 60,
            "素早さ": 50
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": "マンムー",
            "appear": 0,
            "moves": [
            "こなゆき",
            "じしん"
            ],
            "shiny": True
            },
            {
            "name": "サニーゴ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/222.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 55,
            "防御": 95,
            "特攻": 65,
            "特防": 95,
            "素早さ": 35
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "サニゴーン",
            "appear": 0,
            "moves": [
            "バブルこうせん",
            "あわ"
            ],
            "shiny": False
            },
            {
            "name": "サニーゴ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/222.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 55,
            "防御": 95,
            "特攻": 65,
            "特防": 95,
            "素早さ": 35
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": "サニゴーン",
            "appear": 0,
            "moves": [
            "バブルこうせん",
            "あわ"
            ],
            "shiny": True
            },
            {
            "name": "テッポウオ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/223.png",
            "base_stats": {
            "HP": 35,
            "攻撃": 65,
            "防御": 35,
            "特攻": 65,
            "特防": 35,
            "素早さ": 65
            },
            "rarity": 1,
            "evolve_level": 25,
            "evolves_to": "オクタン",
            "appear": 0,
            "moves": [
            "みずでっぽう",
            "あわ"
            ],
            "shiny": False
            },
            {
            "name": "テッポウオ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/223.png",
            "base_stats": {
            "HP": 35,
            "攻撃": 65,
            "防御": 35,
            "特攻": 65,
            "特防": 35,
            "素早さ": 65
            },
            "rarity": 1,
            "evolve_level": 25,
            "evolves_to": "オクタン",
            "appear": 0,
            "moves": [
            "みずでっぽう",
            "あわ"
            ],
            "shiny": True
            },
            {
            "name": "オクタン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/224.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 105,
            "防御": 75,
            "特攻": 105,
            "特防": 75,
            "素早さ": 45
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "オクタンほう",
            "れいとうビーム"
            ],
            "shiny": False
            },
            {
            "name": "オクタン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/224.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 105,
            "防御": 75,
            "特攻": 105,
            "特防": 75,
            "素早さ": 45
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "オクタンほう",
            "れいとうビーム"
            ],
            "shiny": True
            },
            {
            "name": "デリバード",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/225.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 55,
            "防御": 45,
            "特攻": 65,
            "特防": 45,
            "素早さ": 75
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "プレゼント",
            "れいとうビーム"
            ],
            "shiny": False
            },
            {
            "name": "デリバード",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/225.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 55,
            "防御": 45,
            "特攻": 65,
            "特防": 45,
            "素早さ": 75
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "プレゼント",
            "れいとうビーム"
            ],
            "shiny": True
            },
            {
            "name": "マンタイン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/226.png",
            "base_stats": {
            "HP": 85,
            "攻撃": 40,
            "防御": 70,
            "特攻": 80,
            "特防": 140,
            "素早さ": 70
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "エアスラッシュ",
            "れいとうビーム"
            ],
            "shiny": False
            },
            {
            "name": "マンタイン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/226.png",
            "base_stats": {
            "HP": 85,
            "攻撃": 40,
            "防御": 70,
            "特攻": 80,
            "特防": 140,
            "素早さ": 70
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "エアスラッシュ",
            "れいとうビーム"
            ],
            "shiny": True
            },
            {
            "name": "エアームド",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/227.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 80,
            "防御": 140,
            "特攻": 40,
            "特防": 70,
            "素早さ": 70
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "つばめがえし",
            "アイアンヘッド"
            ],
            "shiny": False
            },
            {
            "name": "エアームド",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/227.png",
            "base_stats": {
            "HP": 65,
            "攻撃": 80,
            "防御": 140,
            "特攻": 40,
            "特防": 70,
            "素早さ": 70
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "つばめがえし",
            "アイアンヘッド"
            ],
            "shiny": True
            },
            {
            "name": "デルビル",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/228.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 60,
            "防御": 30,
            "特攻": 80,
            "特防": 50,
            "素早さ": 65
            },
            "rarity": 1,
            "evolve_level": 24,
            "evolves_to": "ヘルガー",
            "appear": 0,
            "moves": [
            "ひのこ",
            "かみつく"
            ],
            "shiny": False
            },
            {
            "name": "デルビル",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/228.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 60,
            "防御": 30,
            "特攻": 80,
            "特防": 50,
            "素早さ": 65
            },
            "rarity": 1,
            "evolve_level": 24,
            "evolves_to": "ヘルガー",
            "appear": 0,
            "moves": [
            "ひのこ",
            "かみつく"
            ],
            "shiny": True
            },
            {
            "name": "ヘルガー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/229.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 90,
            "防御": 50,
            "特攻": 110,
            "特防": 80,
            "素早さ": 95
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かえんほうしゃ",
            "かみくだく"
            ],
            "shiny": False
            },
            {
            "name": "ヘルガー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/229.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 90,
            "防御": 50,
            "特攻": 110,
            "特防": 80,
            "素早さ": 95
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かえんほうしゃ",
            "かみくだく"
            ],
            "shiny": True
            },
            {
            "name": "キングドラ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/230.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 95,
            "防御": 95,
            "特攻": 95,
            "特防": 95,
            "素早さ": 85
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "ハイドロポンプ",
            "りゅうのはどう"
            ],
            "shiny": False
            },
            {
            "name": "キングドラ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/230.png",
            "base_stats": {
            "HP": 75,
            "攻撃": 95,
            "防御": 95,
            "特攻": 95,
            "特防": 95,
            "素早さ": 85
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "ハイドロポンプ",
            "りゅうのはどう"
            ],
            "shiny": True
            },
            {
            "name": "ゴマゾウ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/231.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 60,
            "防御": 60,
            "特攻": 40,
            "特防": 40,
            "素早さ": 40
            },
            "rarity": 1,
            "evolve_level": 25,
            "evolves_to": "ドンファン",
            "appear": 0,
            "moves": [
            "ころがる",
            "なきごえ"
            ],
            "shiny": False
            },
            {
            "name": "ゴマゾウ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/231.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 60,
            "防御": 60,
            "特攻": 40,
            "特防": 40,
            "素早さ": 40
            },
            "rarity": 1,
            "evolve_level": 25,
            "evolves_to": "ドンファン",
            "appear": 0,
            "moves": [
            "ころがる",
            "なきごえ"
            ],
            "shiny": True
            },
            {
            "name": "ドンファン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/232.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 120,
            "防御": 120,
            "特攻": 60,
            "特防": 60,
            "素早さ": 50
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "ころがる",
            "じしん"
            ],
            "shiny": False
            },
            {
            "name": "ドンファン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/232.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 120,
            "防御": 120,
            "特攻": 60,
            "特防": 60,
            "素早さ": 50
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "ころがる",
            "じしん"
            ],
            "shiny": True
            },
            {
            "name": "ポリゴン２",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/233.png",
            "base_stats": {
            "HP": 85,
            "攻撃": 80,
            "防御": 90,
            "特攻": 105,
            "特防": 95,
            "素早さ": 60
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": "ポリゴンＺ",
            "appear": 0,
            "moves": [
            "10まんボルト",
            "トライアタック"
            ],
            "shiny": False
            },
            {
            "name": "ポリゴン２",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/233.png",
            "base_stats": {
            "HP": 85,
            "攻撃": 80,
            "防御": 90,
            "特攻": 105,
            "特防": 95,
            "素早さ": 60
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": "ポリゴンＺ",
            "appear": 0,
            "moves": [
            "10まんボルト",
            "トライアタック"
            ],
            "shiny": True
            },
            {
            "name": "オドシシ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/234.png",
            "base_stats": {
            "HP": 73,
            "攻撃": 95,
            "防御": 62,
            "特攻": 85,
            "特防": 65,
            "素早さ": 85
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": "アヤシシ",
            "appear": 0,
            "moves": [
            "たいあたり",
            "とっしん"
            ],
            "shiny": False
            },
            {
            "name": "オドシシ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/234.png",
            "base_stats": {
            "HP": 73,
            "攻撃": 95,
            "防御": 62,
            "特攻": 85,
            "特防": 65,
            "素早さ": 85
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": "アヤシシ",
            "appear": 0,
            "moves": [
            "たいあたり",
            "とっしん"
            ],
            "shiny": True
            },
            {
            "name": "ドーブル",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/235.png",
            "base_stats": {
            "HP": 55,
            "攻撃": 20,
            "防御": 35,
            "特攻": 20,
            "特防": 45,
            "素早さ": 75
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "スケッチ"
            ],
            "shiny": False
            },
            {
            "name": "ドーブル",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/235.png",
            "base_stats": {
            "HP": 55,
            "攻撃": 20,
            "防御": 35,
            "特攻": 20,
            "特防": 45,
            "素早さ": 75
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "スケッチ"
            ],
            "shiny": True
            },
            {
            "name": "バルキー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/236.png",
            "base_stats": {
            "HP": 35,
            "攻撃": 35,
            "防御": 35,
            "特攻": 35,
            "特防": 35,
            "素早さ": 35
            },
            "rarity": 1,
            "evolve_level": 20,
            "evolves_to": ["サワムラー", "エビワラー", "カポエラー"],
            "appear": 0,
            "moves": [
            "とっしん",
            "まわしげり"
            ],
            "shiny": False
            },
            {
            "name": "バルキー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/236.png",
            "base_stats": {
            "HP": 35,
            "攻撃": 35,
            "防御": 35,
            "特攻": 35,
            "特防": 35,
            "素早さ": 35
            },
            "rarity": 1,
            "evolve_level": 20,
            "evolves_to": ["サワムラー", "エビワラー", "カポエラー"],
            "appear": 0,
            "moves": [
            "とっしん",
            "まわしげり"
            ],
            "shiny": True
            },
            {
            "name": "カポエラー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/237.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 95,
            "防御": 95,
            "特攻": 35,
            "特防": 110,
            "素早さ": 70
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "きあいパンチ",
            "じごくぐるま"
            ],
            "shiny": False
            },
            {
            "name": "カポエラー",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/237.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 95,
            "防御": 95,
            "特攻": 35,
            "特防": 110,
            "素早さ": 70
            },
            "rarity": 1,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "きあいパンチ",
            "じごくぐるま"
            ],
            "shiny": True
            },
            {
            "name": "ムチュール",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/238.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 30,
            "防御": 15,
            "特攻": 85,
            "特防": 65,
            "素早さ": 65
            },
            "rarity": 1,
            "evolve_level": 30,
            "evolves_to": "ルージュラ",
            "appear": 0,
            "moves": [
            "れいとうビーム",
            "こなゆき"
            ],
            "shiny": False
            },
            {
            "name": "ムチュール",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/238.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 30,
            "防御": 15,
            "特攻": 85,
            "特防": 65,
            "素早さ": 65
            },
            "rarity": 1,
            "evolve_level": 30,
            "evolves_to": "ルージュラ",
            "appear": 0,
            "moves": [
            "れいとうビーム",
            "こなゆき"
            ],
            "shiny": True
            },
            {
            "name": "エレキッド",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/239.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 63,
            "防御": 37,
            "特攻": 65,
            "特防": 55,
            "素早さ": 95
            },
            "rarity": 1,
            "evolve_level": 30,
            "evolves_to": "エレブー",
            "appear": 0,
            "moves": [
            "でんきショック",
            "かみなりパンチ"
            ],
            "shiny": False
            },
            {
            "name": "エレキッド",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/239.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 63,
            "防御": 37,
            "特攻": 65,
            "特防": 55,
            "素早さ": 95
            },
            "rarity": 1,
            "evolve_level": 30,
            "evolves_to": "エレブー",
            "appear": 0,
            "moves": [
            "でんきショック",
            "かみなりパンチ"
            ],
            "shiny": True
            },
            {
            "name": "ブビィ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/240.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 75,
            "防御": 37,
            "特攻": 70,
            "特防": 55,
            "素早さ": 83
            },
            "rarity": 1,
            "evolve_level": 30,
            "evolves_to": "ブーバー",
            "appear": 0,
            "moves": [
            "ひのこ",
            "かえんほうしゃ"
            ],
            "shiny": False
            },
            {
            "name": "ブビィ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/240.png",
            "base_stats": {
            "HP": 45,
            "攻撃": 75,
            "防御": 37,
            "特攻": 70,
            "特防": 55,
            "素早さ": 83
            },
            "rarity": 1,
            "evolve_level": 30,
            "evolves_to": "ブーバー",
            "appear": 0,
            "moves": [
            "ひのこ",
            "かえんほうしゃ"
            ],
            "shiny": True
            },
            {
            "name": "ミルタンク",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/241.png",
            "base_stats": {
            "HP": 95,
            "攻撃": 80,
            "防御": 105,
            "特攻": 40,
            "特防": 70,
            "素早さ": 100
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "のしかかり",
            "ころがる"
            ],
            "shiny": False
            },
            {
            "name": "ミルタンク",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/241.png",
            "base_stats": {
            "HP": 95,
            "攻撃": 80,
            "防御": 105,
            "特攻": 40,
            "特防": 70,
            "素早さ": 100
            },
            "rarity": 2,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "のしかかり",
            "ころがる"
            ],
            "shiny": True
            },
            {
            "name": "ハピナス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
            "base_stats": {
            "HP": 255,
            "攻撃": 10,
            "防御": 10,
            "特攻": 75,
            "特防": 135,
            "素早さ": 55
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "はたく",
            "ゆびをふる"
            ],
            "shiny": False
            },
            {
            "name": "ハピナス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/242.png",
            "base_stats": {
            "HP": 255,
            "攻撃": 10,
            "防御": 10,
            "特攻": 75,
            "特防": 135,
            "素早さ": 55
            },
            "rarity": 3,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "はたく",
            "ゆびをふる"
            ],
            "shiny": True
            },
            {
            "name": "ライコウ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/243.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 85,
            "防御": 75,
            "特攻": 115,
            "特防": 100,
            "素早さ": 115
            },
            "rarity": 4,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かみなり",
            "かみくだく"
            ],
            "shiny": False
            },
            {
            "name": "ライコウ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/243.png",
            "base_stats": {
            "HP": 90,
            "攻撃": 85,
            "防御": 75,
            "特攻": 115,
            "特防": 100,
            "素早さ": 115
            },
            "rarity": 4,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かみなり",
            "かみくだく"
            ],
            "shiny": True
            },
            {
            "name": "エンテイ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/244.png",
            "base_stats": {
            "HP": 115,
            "攻撃": 115,
            "防御": 85,
            "特攻": 90,
            "特防": 75,
            "素早さ": 100
            },
            "rarity": 4,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かえんほうしゃ",
            "かみくだく"
            ],
            "shiny": False
            },
            {
            "name": "エンテイ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/244.png",
            "base_stats": {
            "HP": 115,
            "攻撃": 115,
            "防御": 85,
            "特攻": 90,
            "特防": 75,
            "素早さ": 100
            },
            "rarity": 4,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "かえんほうしゃ",
            "かみくだく"
            ],
            "shiny": True
            },
            {
            "name": "スイクン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/245.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 75,
            "防御": 115,
            "特攻": 90,
            "特防": 115,
            "素早さ": 85
            },
            "rarity": 4,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "ハイドロポンプ",
            "れいとうビーム"
            ],
            "shiny": False
            },
            {
            "name": "スイクン",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/245.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 75,
            "防御": 115,
            "特攻": 90,
            "特防": 115,
            "素早さ": 85
            },
            "rarity": 4,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "ハイドロポンプ",
            "れいとうビーム"
            ],
            "shiny": True
            },
            {
            "name": "ヨーギラス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/246.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 64,
            "防御": 50,
            "特攻": 45,
            "特防": 50,
            "素早さ": 41
            },
            "rarity": 2,
            "evolve_level": 30,
            "evolves_to": "サナギラス",
            "appear": 0,
            "moves": [
            "いわおとし",
            "かみつく"
            ],
            "shiny": False
            },
            {
            "name": "ヨーギラス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/246.png",
            "base_stats": {
            "HP": 50,
            "攻撃": 64,
            "防御": 50,
            "特攻": 45,
            "特防": 50,
            "素早さ": 41
            },
            "rarity": 2,
            "evolve_level": 30,
            "evolves_to": "サナギラス",
            "appear": 0,
            "moves": [
            "いわおとし",
            "かみつく"
            ],
            "shiny": True
            },
            {
            "name": "サナギラス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/247.png",
            "base_stats": {
            "HP": 70,
            "攻撃": 84,
            "防御": 70,
            "特攻": 65,
            "特防": 70,
            "素早さ": 51
            },
            "rarity": 3,
            "evolve_level": 55,
            "evolves_to": "バンギラス",
            "appear": 0,
            "moves": [
            "いわなだれ",
            "かみくだく"
            ],
            "shiny": False
            },
            {
            "name": "サナギラス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/247.png",
            "base_stats": {
            "HP": 70,
            "攻撃": 84,
            "防御": 70,
            "特攻": 65,
            "特防": 70,
            "素早さ": 51
            },
            "rarity": 3,
            "evolve_level": 55,
            "evolves_to": "バンギラス",
            "appear": 0,
            "moves": [
            "いわなだれ",
            "かみくだく"
            ],
            "shiny": True
            },
            {
            "name": "バンギラス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/248.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 134,
            "防御": 110,
            "特攻": 95,
            "特防": 100,
            "素早さ": 61
            },
            "rarity": 4,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 1,
            "moves": [
            "ストーンエッジ",
            "かみくだく"
            ],
            "shiny": False
            },
            {
            "name": "バンギラス",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/248.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 134,
            "防御": 110,
            "特攻": 95,
            "特防": 100,
            "素早さ": 61
            },
            "rarity": 4,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 1,
            "moves": [
            "ストーンエッジ",
            "かみくだく"
            ],
            "shiny": True
            },
            {
            "name": "ルギア",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
            "base_stats": {
            "HP": 106,
            "攻撃": 90,
            "防御": 130,
            "特攻": 90,
            "特防": 154,
            "素早さ": 110
            },
            "rarity": 6,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "エアロブラスト",
            "サイコキネシス"
            ],
            "shiny": False
            },
            {
            "name": "ルギア",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/249.png",
            "base_stats": {
            "HP": 106,
            "攻撃": 90,
            "防御": 130,
            "特攻": 90,
            "特防": 154,
            "素早さ": 110
            },
            "rarity": 6,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "エアロブラスト",
            "サイコキネシス"
            ],
            "shiny": True
            },
            {
            "name": "ホウオウ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/250.png",
            "base_stats": {
            "HP": 106,
            "攻撃": 130,
            "防御": 90,
            "特攻": 110,
            "特防": 154,
            "素早さ": 90
            },
            "rarity": 6,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "せいなるほのお",
            "ゴッドバード"
            ],
            "shiny": False
            },
            {
            "name": "ホウオウ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/250.png",
            "base_stats": {
            "HP": 106,
            "攻撃": 130,
            "防御": 90,
            "特攻": 110,
            "特防": 154,
            "素早さ": 90
            },
            "rarity": 6,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "せいなるほのお",
            "ゴッドバード"
            ],
            "shiny": True
            },
            {
            "name": "セレビィ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/251.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 100,
            "防御": 100,
            "特攻": 100,
            "特防": 100,
            "素早さ": 100
            },
            "rarity": 5,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "マジカルリーフ",
            "サイコキネシス"
            ],
            "shiny": False
            },
            {
            "name": "セレビィ",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/251.png",
            "base_stats": {
            "HP": 100,
            "攻撃": 100,
            "防御": 100,
            "特攻": 100,
            "特防": 100,
            "素早さ": 100
            },
            "rarity": 5,
            "evolve_level": None,
            "evolves_to": None,
            "appear": 0,
            "moves": [
            "マジカルリーフ",
            "サイコキネシス"
            ],
            "shiny": True
        }
]
