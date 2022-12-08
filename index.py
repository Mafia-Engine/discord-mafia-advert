import tkinter as tk
from tkinter import ttk
from functools import partial
import tkinter.font as tkFont
import time
import DiscordRPC
from datetime import datetime
import calendar

def debug():
    print("Debug Function")

class DiscordMafia(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title("Discord Mafia Advertising")
        self.start_timestamp = self.get_current_time()
        self.rpc = DiscordRPC.RPC.Set_ID(app_id=1046423943352942693)
        self.set_activity()

        tk.Label(self, text = "Keep this window open").pack()
        # tk.Button(self, text = "Hide Window", command=self.hide_window).pack()


    def get_current_time(self):
        date = datetime.utcnow()
        unixtime = calendar.timegm(date.utctimetuple())
        return unixtime

    def hide_window(self):
        self.withdraw()

    def show_window(self):
        self.deiconify()
    
    def initialize_rpc(self):
        try:
            self.rpc = DiscordRPC.RPC.Set_ID(app_id=1046423943352942693)
        except:
            print("Temporarily unable to start RPC (is Discord loading?)")


    def set_activity(self):
        try:
            button = DiscordRPC.button(
                button_one_label="Join Discord Mafia",
                button_one_url="https://discord.gg/social-deduction",
                button_two_label="Show Your Pride",
                button_two_url="https://jacksonvirgo.itch.io/discord-mafia"
                )

            self.rpc.set_activity(state="https://discord.gg/social-deduction", details="Wanna play all things mafia?", timestamp=self.start_timestamp, large_image='servericon', small_image='boticon', large_text='Join Discord Mafia', small_text='We have our own bot!', buttons=button)
        except:
            self.initialize_rpc()
        self.after(2000, self.set_activity)


if __name__ == "__main__":
    discord_mafia = DiscordMafia()
    discord_mafia.mainloop()
