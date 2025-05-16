import json

file_path = 'config.json'

class ConfigControl:

    @staticmethod
    def load_data():
        try:
            with open(file_path, 'r') as f:
                data = f.read().strip()
                if not data:
                    return {"hotkeys": []}
                return json.loads(data)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"hotkeys": []}

    @staticmethod
    def save_data(data):
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    @staticmethod
    def add_hotkey(key, action):
        try:
            data = ConfigControl.load_data()
            if any(hk["key"] == key for hk in data["hotkeys"]): #check for duplicates
                print(f"Hotkey '{key}' already exists.")
                return
            new_hotkey = {"key": key, "action": action}
            data["hotkeys"].append(new_hotkey) #adding new hotkey
            ConfigControl.save_data(data)
            print(f"Hotkey '{key}' with action '{action}' added successfully!")
        except Exception as e:
            print(f"Error adding hotkey: {e}")

    @staticmethod
    def delete_hotkey(key_to_delete):
        try:
            data = ConfigControl.load_data()
            original_len = len(data["hotkeys"])
            data["hotkeys"] = [hk for hk in data["hotkeys"] if hk["key"] != key_to_delete] #attempt to delete hotkey
            if len(data["hotkeys"]) == original_len: #check if key found and deleted
                print(f"Hotkey '{key_to_delete}' not found.")
            else:
                ConfigControl.save_data(data)
                print(f"Hotkey '{key_to_delete}' removed successfully!")
        except Exception as e:
            print(f"Error deleting hotkey: {e}")

    @staticmethod
    def list_hotkeys():
        try:
            data = ConfigControl.load_data()
            hotkeys = data.get("hotkeys", [])
            if hotkeys:
                print("Current hotkeys:")
                for hk in hotkeys:
                    print(f"Key: {hk['key']}, Action: {hk['action']}")
            else:
                print("No hotkeys defined.")
        except Exception as e:
            print(f"Error listing hotkeys: {e}")




