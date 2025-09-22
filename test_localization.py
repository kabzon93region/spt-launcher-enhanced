#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def test_localization_files():
    """Проверяем, что все файлы локализации содержат новые ключи"""
    
    locales_path = "X:\\EFT\\EscapeFromTarkov\\OneLaunch\\vo1ter-fork\\project\\SPT.Launcher\\SPT_Data\\Launcher\\Locales"
    
    required_keys = [
        "auto_launch_game",
        "auto_launch_delay", 
        "enable_retry_connection",
        "retry_attempts",
        "retry_delay"
    ]
    
    print("🔍 Проверка файлов локализации...")
    
    for filename in os.listdir(locales_path):
        if filename.endswith('.json'):
            filepath = os.path.join(locales_path, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                missing_keys = []
                for key in required_keys:
                    if key not in data:
                        missing_keys.append(key)
                
                if missing_keys:
                    print(f"❌ {filename}: отсутствуют ключи: {missing_keys}")
                else:
                    print(f"✅ {filename}: все ключи присутствуют")
                    
            except Exception as e:
                print(f"❌ {filename}: ошибка чтения - {e}")
    
    print("\n🎯 Проверка завершена!")

if __name__ == "__main__":
    test_localization_files()
