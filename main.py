import requests
import json
import os
import re

def banner():
    os.system("clear")
    print("""
███████╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔════╝██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
█████╗  ██║   ██║███████╗██║██╔██╗ ██║   ██║
██╔══╝  ██║   ██║╚════██║██║██║╚██╗██║   ██║
██║     ╚██████╔╝███████║██║██║ ╚████║   ██║
╚═╝      ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝

        SOCIAL OSINT PANEL
""")

def load_sites():
    with open("sites.json") as f:
        return json.load(f)

def check_user(username):

    sites = load_sites()

    results = {}

    print("\n[+] Checking platforms\n")

    for site in sites:

        name = site["name"]
        url = site["url"].replace("{}",username)

        try:

            r = requests.get(url,timeout=10)

            if r.status_code == 200:

                print(f"[FOUND] {name}: {url}")
                results[name] = url

            else:

                print(f"[----] {name}")

        except:

            print(f"[ERR ] {name}")

    return results


def main():

    banner()

    username = input("Username: ")

    data = check_user(username)

    with open("result.json","w") as f:
        json.dump(data,f,indent=4)

    print("\nSaved to result.json")

if __name__ == "__main__":
    main()
