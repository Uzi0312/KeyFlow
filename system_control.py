import time
import keyboard
import subprocess

class SystemControl:

    @staticmethod
    def execute(action):
        if 'open' in action:
            app = action.split(' ')[1]
            SystemControl.open_app(app)
        else:
            SystemControl.write(action)

    @staticmethod
    def write(content):
        time.sleep(0.5) #minimal delay necessary, 0.5 works best for consistent output
        keyboard.write(content)

    @staticmethod
    def open_app(app):
        try:
            subprocess.Popen(f'{app}.exe')
        except Exception as e:
            print(f'An error occured while opening {app}: {e}')
