from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Discord Invite Bot To Id")

try:
    try:
        IdBot = int(input(f"\n{red}{INPUT} ID bot -> {reset}"))
    except:
        ErrorId()

    URLBot = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'

    print(f"{INFO} URL bot: \"{color.WHITE}{URLBot}{color.RED}\"{color.RESET}")

    choice = input(f"{INPUT} Open the Internet ? (y/n) -> {color.RESET}")
    if choice in ['y', 'Y', 'Yes', 'yes']:
        webbrowser.open_new_tab(URLBot)
        Continue()
        Reset()
    else:
        Continue()
        Reset()
except Exception as e:
    Error(e)
