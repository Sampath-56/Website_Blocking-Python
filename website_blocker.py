import platform
import os

if platform.system() == "Windows":
    pathToHosts = r"C:\Windows\System32\drivers\etc\hosts"
else:
    pathToHosts = r"/etc/hosts"

redirect = "127.0.0.1"
websites = ["www.facebook.com", "www.instagram.com", "www.indiabix.com", "www.youtube.com", "www.xvideos.com", "www.pornhub.com"]

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        # os.getuid() not available on Windows, check for admin rights using os.system
        return os.system("net session >nul 2>&1") == 0

if not is_admin():
    print("You need to run this script with administrative privileges.")
    exit()

with open(pathToHosts, 'r+') as file:
    content = file.read()
    for site in websites:
        if site in content:
            continue
        else:
            file.write(f"{redirect} {site}\n")

print("Websites have been blocked.")
