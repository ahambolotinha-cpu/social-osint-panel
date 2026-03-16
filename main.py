import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor

headers = {
"User-Agent":"Mozilla/5.0"
}

def banner():
    os.system("clear")
    print("""
█████╗ ███████╗██╗███╗   ██╗████████╗
██╔══██╗██╔════╝██║████╗  ██║╚══██╔══╝
███████║███████╗██║██╔██╗ ██║   ██║
██╔══██║╚════██║██║██║╚██╗██║   ██║
██║  ██║███████║██║██║ ╚████║   ██║
╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝

        ADVANCED OSINT PANEL
""")

def load_sites():
    with open("sites.json") as f:
        return json.load(f)

def check_site(site,username):

    url = site["url"].replace("{}",username)

    try:

        r = requests.get(url,headers=headers,timeout=10)

        if r.status_code == 200:

            if "not found" in r.text.lower():
                return None

            return url

    except:
        pass

    return None


def scan(username):

    sites = load_sites()

    results = {}

    def task(site):

        res = check_site(site,username)

        if res:
            print(f"[FOUND] {site['name']} -> {res}")
            results[site["name"]] = res
        else:
            print(f"[----] {site['name']}")

    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(task,sites)

    return results


def save(username,data):

    file = f"{username}_osint.json"

    with open(file,"w") as f:
        json.dump(data,f,indent=4)

    print("\nReport saved:",file)


def main():

    banner()

    username = input("Username: ")

    print("\nScanning...\n")

    data = scan(username)

    save(username,data)


if __name__ == "__main__":
    main()
