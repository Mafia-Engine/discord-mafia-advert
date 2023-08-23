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
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(os.path.realpath(sys.executable))
    elif __file__:
        application_path = os.path.dirname(__file__)
    return application_path

USER_NAME = getpass.getuser()
BASE_PATH = get_file_path_of_current()
STARTUP_PATH = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

def has_auto_start_file():
    os_system = platform.system()
    if (os_system == "Windows"):
        path = "%s\\discord_mafia_open.bat" % STARTUP_PATH
        isExist = os.path.exists(path)
        print(isExist)
        return isExist
    else:
        return False

def windows_auto_start():
    with open(STARTUP_PATH + '\\' + 'discord_mafia_open.bat', "w+") as bat_file:
        full_path = BASE_PATH + "\\Discord Mafia Advertising.exe"
        bat_file.write(r'start "" "%s' % full_path)

def remove_windows_auto_start():
    os.remove(r'%s\\discord_mafia_open.bat' % STARTUP_PATH)

class RPC_Class(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start_timestamp = self.get_current_time()
        self.rpc = None
        self.start()

    def get_current_time(self):
        date = datetime.utcnow()
        unixtime = calendar.timegm(date.utctimetuple())
        return unixtime

    def initialize_rpc(self):
        print("Initializing RPC")
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
                    large_image='discordmafia', 
                    large_text='Join Discord Mafia', 
                    buttons=[button[0]]
                )
            except:
                self.rpc = None
                self.rpc = DiscordRPC.RPC.Set_ID(app_id=1143833637767348304)
                print("Error updating RPC", self.get_current_time())
            time.sleep(2)

class DiscordMafia():
    def __init__(self):
        self.icon_image = PIL.Image.open(resource_path("icon.png"))
        self.state = has_auto_start_file()
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
            if (self.state == True):
                windows_auto_start()
            else:
                remove_windows_auto_start()
        else:
            if (self.state == True):
                print("Adding")
            else:
                print("Removing")
        

    def quit_app(self):
        self.icon.stop()

if __name__ == "__main__":
    DiscordMafia()
