import keyboard
from config_control import ConfigControl
from system_control import SystemControl
from datetime import datetime


class HotkeyManager:

    registered_keys = []

    @staticmethod
    def register_keys():
        data = ConfigControl.load_data()
        for hk in data.get("hotkeys", []):
            key = hk.get("key")
            action = hk.get("action")
            keyboard.add_hotkey(key, lambda a=action: (SystemControl.execute(a), HotkeyManager.create_log(key, a)))
            HotkeyManager.registered_keys.append(key)
        print("All hotkeys registered.")

    @staticmethod
    def unregister_keys():
        for key in HotkeyManager.registered_keys:
            keyboard.remove_hotkey(key)
        HotkeyManager.registered_keys.clear()
        print("Hotkeys unregistered.")

    @staticmethod
    def create_log(key, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("hotkey_logs.txt", "a") as f:
            f.write(f"[{timestamp}] Hotkey '{key}' triggered -> Action: '{action}'\n")

    @staticmethod
    def run():
        HotkeyManager.register_keys()
        print("Listening for hotkeys. Press END to stop.")
        keyboard.wait('end')
        HotkeyManager.unregister_keys()
