from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
    ErrorModule(e)

Title("Rat Discord (Paid)")

try:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} The discord rat is a tool that allows you to control a victim's computer from discord.")
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The Rat is paid and can be purchased on discord.")
    webbrowser.open_new_tab(f"https://{discord_server}")
    Continue()
    Reset()
except Exception as e:
    Error(e)