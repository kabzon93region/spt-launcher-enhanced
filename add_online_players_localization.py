#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def add_online_players_localization():
    """Добавляем ключи локализации для онлайн-игроков во все языки"""
    
    locales_path = "project\\SPT.Launcher\\SPT_Data\\Launcher\\Locales"
    
    # Новые ключи локализации с переводами для разных языков
    new_keys = {
        "English": {
            "player_name": "Player name",
            "current_activity": "Current activity:",
            "activity_in_menu": "in Menu",
            "activity_in_raid": "in Raid",
            "activity_in_stash": "in Stash",
            "activity_in_hideout": "in Hideout",
            "activity_is_trading": "is Trading",
            "activity_raid_format": "{0} on {1} as {2} for {3} mins",
            "map_factory4_day": "Factory",
            "map_factory4_night": "Factory",
            "map_bigmap": "Customs",
            "map_interchange": "Interchange",
            "map_rezervbase": "Reserve",
            "map_woods": "Woods",
            "map_shoreline": "Shoreline",
            "map_tarkovstreets": "Streets of Tarkov",
            "map_sandbox": "Ground Zero",
            "map_laboratory": "Laboratory",
            "map_lighthouse": "Lighthouse"
        },
        "Russian": {
            "player_name": "Имя игрока",
            "current_activity": "Текущая активность:",
            "activity_in_menu": "в меню",
            "activity_in_raid": "в рейде",
            "activity_in_stash": "в сташе",
            "activity_in_hideout": "в убежище",
            "activity_is_trading": "торгует",
            "activity_raid_format": "{0} на {1} за {2} в течение {3} мин",
            "map_factory4_day": "Завод",
            "map_factory4_night": "Завод",
            "map_bigmap": "Таможня",
            "map_interchange": "Интерчейндж",
            "map_rezervbase": "Резерв",
            "map_woods": "Лес",
            "map_shoreline": "Береговая линия",
            "map_tarkovstreets": "Улицы Таркова",
            "map_sandbox": "Нулевая точка",
            "map_laboratory": "Лаборатория",
            "map_lighthouse": "Маяк"
        },
        "German": {
            "player_name": "Spielername",
            "current_activity": "Aktuelle Aktivität:",
            "activity_in_menu": "im Menü",
            "activity_in_raid": "im Raid",
            "activity_in_stash": "im Stash",
            "activity_in_hideout": "im Versteck",
            "activity_is_trading": "handelt",
            "activity_raid_format": "{0} auf {1} als {2} für {3} Min",
            "map_factory4_day": "Fabrik",
            "map_factory4_night": "Fabrik",
            "map_bigmap": "Zoll",
            "map_interchange": "Interchange",
            "map_rezervbase": "Reserve",
            "map_woods": "Wald",
            "map_shoreline": "Küstenlinie",
            "map_tarkovstreets": "Tarkov Straßen",
            "map_sandbox": "Nullpunkt",
            "map_laboratory": "Labor",
            "map_lighthouse": "Leuchtturm"
        },
        "French": {
            "player_name": "Nom du joueur",
            "current_activity": "Activité actuelle:",
            "activity_in_menu": "dans le menu",
            "activity_in_raid": "en raid",
            "activity_in_stash": "dans le coffre",
            "activity_in_hideout": "dans la cachette",
            "activity_is_trading": "fait du commerce",
            "activity_raid_format": "{0} sur {1} en tant que {2} pendant {3} min",
            "map_factory4_day": "Usine",
            "map_factory4_night": "Usine",
            "map_bigmap": "Douanes",
            "map_interchange": "Interchange",
            "map_rezervbase": "Réserve",
            "map_woods": "Bois",
            "map_shoreline": "Littoral",
            "map_tarkovstreets": "Rues de Tarkov",
            "map_sandbox": "Point zéro",
            "map_laboratory": "Laboratoire",
            "map_lighthouse": "Phare"
        },
        "Spanish": {
            "player_name": "Nombre del jugador",
            "current_activity": "Actividad actual:",
            "activity_in_menu": "en el menú",
            "activity_in_raid": "en raid",
            "activity_in_stash": "en el almacén",
            "activity_in_hideout": "en el refugio",
            "activity_is_trading": "está comerciando",
            "activity_raid_format": "{0} en {1} como {2} durante {3} min",
            "map_factory4_day": "Fábrica",
            "map_factory4_night": "Fábrica",
            "map_bigmap": "Aduanas",
            "map_interchange": "Interchange",
            "map_rezervbase": "Reserva",
            "map_woods": "Bosque",
            "map_shoreline": "Costa",
            "map_tarkovstreets": "Calles de Tarkov",
            "map_sandbox": "Punto cero",
            "map_laboratory": "Laboratorio",
            "map_lighthouse": "Faro"
        },
        "Italian": {
            "player_name": "Nome del giocatore",
            "current_activity": "Attività attuale:",
            "activity_in_menu": "nel menu",
            "activity_in_raid": "in raid",
            "activity_in_stash": "nello stash",
            "activity_in_hideout": "nel nascondiglio",
            "activity_is_trading": "sta commerciando",
            "activity_raid_format": "{0} su {1} come {2} per {3} min",
            "map_factory4_day": "Fabbrica",
            "map_factory4_night": "Fabbrica",
            "map_bigmap": "Dogane",
            "map_interchange": "Interchange",
            "map_rezervbase": "Riserva",
            "map_woods": "Bosco",
            "map_shoreline": "Costa",
            "map_tarkovstreets": "Strade di Tarkov",
            "map_sandbox": "Punto zero",
            "map_laboratory": "Laboratorio",
            "map_lighthouse": "Faro"
        },
        "Polish": {
            "player_name": "Nazwa gracza",
            "current_activity": "Aktualna aktywność:",
            "activity_in_menu": "w menu",
            "activity_in_raid": "w rajdzie",
            "activity_in_stash": "w schowku",
            "activity_in_hideout": "w kryjówce",
            "activity_is_trading": "handluje",
            "activity_raid_format": "{0} na {1} jako {2} przez {3} min",
            "map_factory4_day": "Fabryka",
            "map_factory4_night": "Fabryka",
            "map_bigmap": "Celnica",
            "map_interchange": "Interchange",
            "map_rezervbase": "Rezerwat",
            "map_woods": "Las",
            "map_shoreline": "Wybrzeże",
            "map_tarkovstreets": "Ulice Tarkova",
            "map_sandbox": "Punkt zero",
            "map_laboratory": "Laboratorium",
            "map_lighthouse": "Latarnia"
        },
        "Chinese (Simplified)": {
            "player_name": "玩家名称",
            "current_activity": "当前活动：",
            "activity_in_menu": "在菜单中",
            "activity_in_raid": "在突袭中",
            "activity_in_stash": "在仓库中",
            "activity_in_hideout": "在藏身处",
            "activity_is_trading": "在交易",
            "activity_raid_format": "{0}在{1}作为{2}进行{3}分钟",
            "map_factory4_day": "工厂",
            "map_factory4_night": "工厂",
            "map_bigmap": "海关",
            "map_interchange": "立交桥",
            "map_rezervbase": "储备站",
            "map_woods": "森林",
            "map_shoreline": "海岸线",
            "map_tarkovstreets": "塔科夫街道",
            "map_sandbox": "零点",
            "map_laboratory": "实验室",
            "map_lighthouse": "灯塔"
        },
        "Chinese (Traditional)": {
            "player_name": "玩家名稱",
            "current_activity": "當前活動：",
            "activity_in_menu": "在選單中",
            "activity_in_raid": "在突襲中",
            "activity_in_stash": "在倉庫中",
            "activity_in_hideout": "在藏身處",
            "activity_is_trading": "在交易",
            "activity_raid_format": "{0}在{1}作為{2}進行{3}分鐘",
            "map_factory4_day": "工廠",
            "map_factory4_night": "工廠",
            "map_bigmap": "海關",
            "map_interchange": "立交橋",
            "map_rezervbase": "儲備站",
            "map_woods": "森林",
            "map_shoreline": "海岸線",
            "map_tarkovstreets": "塔科夫街道",
            "map_sandbox": "零點",
            "map_laboratory": "實驗室",
            "map_lighthouse": "燈塔"
        },
        "Japanese": {
            "player_name": "プレイヤー名",
            "current_activity": "現在の活動：",
            "activity_in_menu": "メニュー中",
            "activity_in_raid": "レイド中",
            "activity_in_stash": "スタッシュ中",
            "activity_in_hideout": "ハイドアウト中",
            "activity_is_trading": "取引中",
            "activity_raid_format": "{0}が{1}で{2}として{3}分間",
            "map_factory4_day": "工場",
            "map_factory4_night": "工場",
            "map_bigmap": "税関",
            "map_interchange": "インターチェンジ",
            "map_rezervbase": "リザーブ",
            "map_woods": "森",
            "map_shoreline": "海岸線",
            "map_tarkovstreets": "タルコフの街",
            "map_sandbox": "ゼロポイント",
            "map_laboratory": "研究所",
            "map_lighthouse": "灯台"
        },
        "Korean": {
            "player_name": "플레이어 이름",
            "current_activity": "현재 활동:",
            "activity_in_menu": "메뉴 중",
            "activity_in_raid": "레이드 중",
            "activity_in_stash": "스태시 중",
            "activity_in_hideout": "하이드아웃 중",
            "activity_is_trading": "거래 중",
            "activity_raid_format": "{0}이(가) {1}에서 {2}로 {3}분 동안",
            "map_factory4_day": "공장",
            "map_factory4_night": "공장",
            "map_bigmap": "세관",
            "map_interchange": "인터체인지",
            "map_rezervbase": "리저브",
            "map_woods": "숲",
            "map_shoreline": "해안선",
            "map_tarkovstreets": "타르코프 거리",
            "map_sandbox": "제로 포인트",
            "map_laboratory": "연구소",
            "map_lighthouse": "등대"
        },
        "Turkish": {
            "player_name": "Oyuncu adı",
            "current_activity": "Mevcut aktivite:",
            "activity_in_menu": "menüde",
            "activity_in_raid": "raidde",
            "activity_in_stash": "stash'te",
            "activity_in_hideout": "sığınakta",
            "activity_is_trading": "ticaret yapıyor",
            "activity_raid_format": "{0} {1}'de {2} olarak {3} dakika",
            "map_factory4_day": "Fabrika",
            "map_factory4_night": "Fabrika",
            "map_bigmap": "Gümrük",
            "map_interchange": "Interchange",
            "map_rezervbase": "Rezerv",
            "map_woods": "Orman",
            "map_shoreline": "Sahil",
            "map_tarkovstreets": "Tarkov Sokakları",
            "map_sandbox": "Sıfır Noktası",
            "map_laboratory": "Laboratuvar",
            "map_lighthouse": "Deniz Feneri"
        }
    }
    
    print("🔍 Добавление ключей локализации для онлайн-игроков...")
    
    for filename in os.listdir(locales_path):
        if filename.endswith('.json'):
            filepath = os.path.join(locales_path, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Определяем язык по имени файла
                language = filename.replace('.json', '')
                if language in new_keys:
                    keys_to_add = new_keys[language]
                else:
                    # Используем английские ключи как fallback
                    keys_to_add = new_keys["English"]
                
                updated = False
                for key, value in keys_to_add.items():
                    if key not in data:
                        data[key] = value
                        print(f"✅ Добавлен ключ '{key}' в {filename}")
                        updated = True
                    else:
                        print(f"☑️ Ключ '{key}' уже существует в {filename}")
                
                if updated:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    print(f"💾 Обновлен файл: {filename}")
                else:
                    print(f"ℹ️ Файл {filename} не требует обновления")
                    
            except Exception as e:
                print(f"❌ Ошибка при обработке {filename}: {e}")
    
    print("\n🎯 Добавление ключей локализации завершено!")

if __name__ == "__main__":
    add_online_players_localization()
