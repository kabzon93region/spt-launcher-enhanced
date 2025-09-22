#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def add_fika_localization():
    """Добавляем ключи локализации для функций Fika во все языки"""
    
    locales_path = "project\\SPT.Launcher\\SPT_Data\\Launcher\\Locales"
    
    # Новые ключи локализации с переводами для разных языков
    new_keys = {
        "English": {
            "players_online": "Online players",
            "dedicated_availability": "Dedicated Availability:",
            "dedicated_available": "Available",
            "dedicated_unavailable": "Unavailable",
            "no_players_online": "No players online",
            "players_online_count": "{0} {1} online",
            "player_singular": "player",
            "players_plural": "players",
            "dedicated_status_available": "Dedicated server is available",
            "dedicated_status_unavailable": "Dedicated server is unavailable"
        },
        "Russian": {
            "players_online": "Игроки онлайн",
            "dedicated_availability": "Доступность выделенного сервера:",
            "dedicated_available": "Доступен",
            "dedicated_unavailable": "Недоступен",
            "no_players_online": "Нет игроков онлайн",
            "players_online_count": "{0} {1} онлайн",
            "player_singular": "игрок",
            "players_plural": "игроков",
            "dedicated_status_available": "Выделенный сервер доступен",
            "dedicated_status_unavailable": "Выделенный сервер недоступен"
        },
        "German": {
            "players_online": "Spieler online",
            "dedicated_availability": "Dedizierte Verfügbarkeit:",
            "dedicated_available": "Verfügbar",
            "dedicated_unavailable": "Nicht verfügbar",
            "no_players_online": "Keine Spieler online",
            "players_online_count": "{0} {1} online",
            "player_singular": "Spieler",
            "players_plural": "Spieler",
            "dedicated_status_available": "Dedizierter Server ist verfügbar",
            "dedicated_status_unavailable": "Dedizierter Server ist nicht verfügbar"
        },
        "French": {
            "players_online": "Joueurs en ligne",
            "dedicated_availability": "Disponibilité dédiée:",
            "dedicated_available": "Disponible",
            "dedicated_unavailable": "Indisponible",
            "no_players_online": "Aucun joueur en ligne",
            "players_online_count": "{0} {1} en ligne",
            "player_singular": "joueur",
            "players_plural": "joueurs",
            "dedicated_status_available": "Le serveur dédié est disponible",
            "dedicated_status_unavailable": "Le serveur dédié est indisponible"
        },
        "Spanish": {
            "players_online": "Jugadores en línea",
            "dedicated_availability": "Disponibilidad dedicada:",
            "dedicated_available": "Disponible",
            "dedicated_unavailable": "No disponible",
            "no_players_online": "No hay jugadores en línea",
            "players_online_count": "{0} {1} en línea",
            "player_singular": "jugador",
            "players_plural": "jugadores",
            "dedicated_status_available": "El servidor dedicado está disponible",
            "dedicated_status_unavailable": "El servidor dedicado no está disponible"
        },
        "Italian": {
            "players_online": "Giocatori online",
            "dedicated_availability": "Disponibilità dedicata:",
            "dedicated_available": "Disponibile",
            "dedicated_unavailable": "Non disponibile",
            "no_players_online": "Nessun giocatore online",
            "players_online_count": "{0} {1} online",
            "player_singular": "giocatore",
            "players_plural": "giocatori",
            "dedicated_status_available": "Il server dedicato è disponibile",
            "dedicated_status_unavailable": "Il server dedicato non è disponibile"
        },
        "Polish": {
            "players_online": "Gracze online",
            "dedicated_availability": "Dostępność dedykowana:",
            "dedicated_available": "Dostępny",
            "dedicated_unavailable": "Niedostępny",
            "no_players_online": "Brak graczy online",
            "players_online_count": "{0} {1} online",
            "player_singular": "gracz",
            "players_plural": "graczy",
            "dedicated_status_available": "Serwer dedykowany jest dostępny",
            "dedicated_status_unavailable": "Serwer dedykowany jest niedostępny"
        },
        "Chinese (Simplified)": {
            "players_online": "在线玩家",
            "dedicated_availability": "专用服务器可用性：",
            "dedicated_available": "可用",
            "dedicated_unavailable": "不可用",
            "no_players_online": "没有在线玩家",
            "players_online_count": "{0} {1} 在线",
            "player_singular": "玩家",
            "players_plural": "玩家",
            "dedicated_status_available": "专用服务器可用",
            "dedicated_status_unavailable": "专用服务器不可用"
        },
        "Chinese (Traditional)": {
            "players_online": "線上玩家",
            "dedicated_availability": "專用伺服器可用性：",
            "dedicated_available": "可用",
            "dedicated_unavailable": "不可用",
            "no_players_online": "沒有線上玩家",
            "players_online_count": "{0} {1} 線上",
            "player_singular": "玩家",
            "players_plural": "玩家",
            "dedicated_status_available": "專用伺服器可用",
            "dedicated_status_unavailable": "專用伺服器不可用"
        },
        "Japanese": {
            "players_online": "オンラインプレイヤー",
            "dedicated_availability": "専用サーバー可用性：",
            "dedicated_available": "利用可能",
            "dedicated_unavailable": "利用不可",
            "no_players_online": "オンラインプレイヤーなし",
            "players_online_count": "{0} {1} オンライン",
            "player_singular": "プレイヤー",
            "players_plural": "プレイヤー",
            "dedicated_status_available": "専用サーバーが利用可能です",
            "dedicated_status_unavailable": "専用サーバーが利用不可です"
        },
        "Korean": {
            "players_online": "온라인 플레이어",
            "dedicated_availability": "전용 서버 가용성:",
            "dedicated_available": "사용 가능",
            "dedicated_unavailable": "사용 불가",
            "no_players_online": "온라인 플레이어 없음",
            "players_online_count": "{0} {1} 온라인",
            "player_singular": "플레이어",
            "players_plural": "플레이어",
            "dedicated_status_available": "전용 서버가 사용 가능합니다",
            "dedicated_status_unavailable": "전용 서버가 사용 불가능합니다"
        },
        "Turkish": {
            "players_online": "Çevrimiçi oyuncular",
            "dedicated_availability": "Özel sunucu kullanılabilirliği:",
            "dedicated_available": "Kullanılabilir",
            "dedicated_unavailable": "Kullanılamaz",
            "no_players_online": "Çevrimiçi oyuncu yok",
            "players_online_count": "{0} {1} çevrimiçi",
            "player_singular": "oyuncu",
            "players_plural": "oyuncu",
            "dedicated_status_available": "Özel sunucu kullanılabilir",
            "dedicated_status_unavailable": "Özel sunucu kullanılamaz"
        }
    }
    
    print("🔍 Добавление ключей локализации для функций Fika...")
    
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
                    f.seek(0)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    print(f"💾 Обновлен файл: {filename}")
                else:
                    print(f"ℹ️ Файл {filename} не требует обновления")
                    
            except Exception as e:
                print(f"❌ Ошибка при обработке {filename}: {e}")
    
    print("\n🎯 Добавление ключей локализации завершено!")

if __name__ == "__main__":
    add_fika_localization()
