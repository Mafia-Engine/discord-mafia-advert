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


USER_NAME = getpass.getuser()
def set_auto_run_windows(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "discord_mafia_open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)

class RPC_Class(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start_timestamp = self.get_current_time()
        self.rpc = DiscordRPC.RPC.Set_ID(app_id=1046423943352942693)
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
        self.icon_image = PIL.Image.open("icon.png")
        self.state = True
        self.attach_menu()

        self.rpc = RPC_Class()

        self.icon.run()

    
    def attach_menu(self):
        self.icon = pystray.Icon("icon", self.icon_image, "Discord Mafia", pystray.Menu(
            # pystray.MenuItem("Run on Start", self.toggle_run_on_start, checked=lambda item: self.state),
            pystray.MenuItem("Quit", self.quit_app)
        ))

        print("Detached")

    def toggle_run_on_start(self):
        self.state = not self.state
        print("Toggle Run On Start")

    def quit_app(self):
        self.icon.stop()


if __name__ == "__main__":
    os_system = platform.system()
    if (os_system == 'Windows'):
        set_auto_run_windows()
    elif (os_system == 'Darwin'):
        print('Auto-Start Not Supported Yet')
    else:
        print('Auto-Start Not Supported Yet')
    
    DiscordMafia()
