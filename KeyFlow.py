from config_control import ConfigControl
from hotkey_manager import HotkeyManager

class Main:
    def show_menu():
        print("\n--- KeyFlow Menu ---")
        print("1. List Hotkeys")
        print("2. Add Hotkey")
        print("3. Delete Hotkey")
        print("4. Activate HK Listener")
        print("5. Exit")

    def run():
        print('Hello User..')
        HotkeyManager.run()
        while True:
            Main.show_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                ConfigControl.list_hotkeys()
            elif choice == "2":
                key = input("Enter hotkey (e.g., ctrl+shift+h): ").strip()
                action = input("Enter text to type: ").strip()
                ConfigControl.add_hotkey(key, action)
            elif choice == "3":
                key = input("Enter hotkey to delete: ").strip()
                ConfigControl.delete_hotkey(key)
            elif choice == "4":
                HotkeyManager.run()
            elif choice == "5":
                print("Exiting KeyFlow.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Main.run()
