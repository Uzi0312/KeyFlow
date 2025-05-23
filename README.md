# KeyFlow
Keyflow is a productivity-enhancing application that allows users to create custom hotkeys for automating and streamlining tasks. With Keyflow, users can assign specific actions to hotkeys, making repetitive tasks faster and more efficient.

Features
1. List Hotkeys: View all currently configured hotkeys.

2. Add Hotkey: Bind a hotkey to custom text you want to type.

3. Delete Hotkey: Remove a previously configured hotkey.

4. Hotkey Listener: Continuously listen for hotkey presses and perform the assigned action.

5. Persistent Configuration: Saves your hotkeys for future use.

Usage
Running KeyFlow
You can run KeyFlow in two ways:

1. Python Script:

    bash
    Copy
    Edit
    python KeyFlow.py

2. Executable (for non-Python users): Run the provided KeyFlow.exe file (no Python installation needed).

Menu Options
List Hotkeys – Shows all configured hotkeys with their actions.

Add Hotkey – Lets you define a new hotkey and its corresponding text action.

Delete Hotkey – Removes a selected hotkey from your configuration.

Activate HK Listener – Starts listening for hotkeys to trigger actions.

Exit – Quits the program.

What can be assigned to a hotkey?
A hotkey can be assigned to paste texts (eg: emails, addresses, phone numbers) & to open applications (.exe files on PATH). For opening applications: create hotkey -> choose hotkey -> action: open [application name] -> save. eg: key: ctrl+shift+1 action: open notepad. 

DEPENDENCIES
Python 3.x

keyboard library (for hotkey listening)

json (built-in, for saving config)


NOTE: KeyFlow.exe displays 'Hello Uzair' as I used an older file for creating .exe file. Download the .py scripts & create .exe file using pyinstaller after making necessary changes.
Make sure to run -onefile command using pyinstaller.
