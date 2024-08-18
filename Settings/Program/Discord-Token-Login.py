from Config.Util import *
from Config.Config import *
try:
    from selenium import webdriver
except Exception as e:
   ErrorModule(e)

Title("Discord Token Login")
try:      
    print()
    token = Choice1TokenDiscord()

    print(f"""
 {BEFORE}01{AFTER}{white} Chrome (Windows / Linux)
 {BEFORE}02{AFTER}{white} Edge (Windows)
 {BEFORE}03{AFTER}{white} Firefox (Windows)
    """)
    browser = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Browser -> {reset}")
 
    if browser in ['1', '01']:
        try:
            navigator = "Chrome"
            print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Chrome()
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()

    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Edge"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
                driver = webdriver.Edge()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
                Continue()
                Reset()

    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Firefox"
                print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} {navigator} Starting..{blue}")
                driver = webdriver.Firefox()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} {navigator} Ready !{blue}")
            except:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
                Continue()
                Reset()
    else:
        ErrorChoice()
    
    try:
        script = """
                function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 2500);
                }
                """
        
        driver.get("https://discord.com/login")
        print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Token Connection..{blue}")
        driver.execute_script(script + f'\nlogin("{token}")')
        time.sleep(4)
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Connected Token !{blue}")
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} If you leave the tool, edge will close!{blue}")
        Continue()
        Reset()
    except:
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {navigator} not installed or driver not up to date.")
        Continue()
        Reset()
except Exception as e:
    Error(e)
