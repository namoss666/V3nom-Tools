from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
    ErrorModule(e)

Title("Obfuscator Tool (Paid)")

try:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} It's a tool that makes any Python script undetectable by antivirus and makes the code unreadable.")
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} The tool is paid and can be purchased on discord.")
    webbrowser.open_new_tab(f"https://{discord_server}")
    Continue()
    Reset()
except Exception as e:
    Error(e)
