import json
import os

locales_folder = "project\\SPT.Launcher\\SPT_Data\\Launcher\\Locales"

new_keys_english = {
    "auto_launch_countdown": "Auto-launch in",
    "auto_launch_seconds": "seconds",
    "cancel_auto_launch": "Cancel Auto-launch"
}

new_keys_russian = {
    "auto_launch_countdown": "Автозапуск через",
    "auto_launch_seconds": "секунд",
    "cancel_auto_launch": "Отменить автозапуск"
}

print("🔍 Добавление ключей локализации для UI автозапуска...")

for filename in os.listdir(locales_folder):
    if filename.endswith(".json"):
        filepath = os.path.join(locales_folder, filename)
        
        try:
            with open(filepath, 'r+', encoding='utf-8') as f:
                data = json.load(f)
                
                keys_to_add = {}
                if filename == "Russian.json":
                    keys_to_add = new_keys_russian
                else:
                    keys_to_add = new_keys_english

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
                    json.dump(data, f, ensure_ascii=False, indent=2)
                    f.truncate()
                    print(f"💾 Обновлен файл: {filename}")
                else:
                    print(f"ℹ️ Файл {filename} не требует обновления")

        except Exception as e:
            print(f"❌ Ошибка при обработке {filename}: {e}")

print("\n🎯 Добавление ключей локализации завершено!")
