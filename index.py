import sys
import DiscordRPC
import pystray
import PIL.Image
import getpass
import os
import platform
from datetime import datetime
import calendar
import time
from threading import Thread

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_file_path_of_current():
    file_path = os.path.dirname(os.path.realpath(__file__))
    return file_path

USER_NAME = getpass.getuser()
BASE_PATH = os.path.dirname(os.path.realpath(__file__))
STARTUP_PATH = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

def windows_auto_start(remove = False):
    with open(STARTUP_PATH + '\\' + 'discord_mafia_open.bat', "w+") as bat_file:
        if (remove):
            bat_file.write("")
        else: 
            full_path = BASE_PATH + "\\Discord Mafia Advertising.exe"
            bat_file.write(r'start "" "%s' % full_path)

class RPC_Class(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start_timestamp = self.get_current_time()
        self.start()

    def get_current_time(self):
        date = datetime.utcnow()
        unixtime = calendar.timegm(date.utctimetuple())
        return unixtime

    def initialize_rpc(self):
        try:
            self.rpc = DiscordRPC.RPC.Set_ID(app_id=1046423943352942693)
        except:
            print("Temporarily unable to start RPC (is Discord loading?)")

    def run(self):
        break_loop = False
        while (not break_loop):
            
            if (self.rpc == None):
                self.initialize_rpc()

            try:
                button = DiscordRPC.button(
                    button_one_label="Join Discord Mafia",
                    button_one_url="https://discord.gg/social-deduction",
                    button_two_label="Show Your Pride",
                    button_two_url="https://jacksonvirgo.itch.io/discord-mafia"
                    )
                
                self.rpc.set_activity(
                    state="https://discord.gg/social-deduction", 
                    details="Wanna play all things mafia?", 
                    timestamp=self.start_timestamp, 
                    large_image='servericon', 
                    small_image='boticon', 
                    large_text='Join Discord Mafia', 
                    small_text='We have our own bot!', 
                    buttons=[button[0]]
                )
            except:
                self.initialize_rpc()
            time.sleep(2)

class DiscordMafia():
    def __init__(self):
        self.icon_image = PIL.Image.open(resource_path("icon.jpeg"))
        self.state = False
        self.attach_menu()
        self.rpc = RPC_Class()
        self.icon.run()

    
    def attach_menu(self):
        self.icon = pystray.Icon("icon", self.icon_image, "Discord Mafia", pystray.Menu(
            pystray.MenuItem("Run at Start", self.toggle_run_on_start, checked=lambda item: self.state),
            pystray.MenuItem("Quit", self.quit_app)
        ))

    def toggle_run_on_start(self):
        self.state = not self.state
        os_system = platform.system()
        if (os_system == "Windows"):
            windows_auto_start(self.state)
        else:
            print("Toggle Run On Start")
        

    def quit_app(self):
        self.icon.stop()


if __name__ == "__main__":
    DiscordMafia()
