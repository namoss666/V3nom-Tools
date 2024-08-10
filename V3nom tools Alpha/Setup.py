
try:
    import sys
    import os

    print("Installing the python modules required for the V3nom Tool:")

    if sys.platform.startswith("win"):
        os.system("pip install --upgrade pip")
        os.system("pip install -r requirements.txt")
        os.system("python V3nom.py")

    elif sys.platform.startswith("linux"):
        os.system("pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
        os.system("python3 V3nom.py")

except Exception as e:
    print(e)
    os.system("pause")
