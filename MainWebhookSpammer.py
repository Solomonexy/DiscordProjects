from colorama import init, Fore, Back, Style
import requests
import os
import time
import json
import getpass
from threading import Thread, Lock, current_thread

username = getpass.getuser()
init()
os.system("title Discord Nuker")


# Define a lock to avoid race conditions
lock = Lock()

# Functions

def send_messages(message, webhooks):
    threads = []
    for i, webhook_url in enumerate(webhooks):
        message = message
        payload = {'content': message}
        json_payload = json.dumps(payload)
        thread = Thread(target=lambda: requests.post(webhook_url, data=json_payload, headers={'Content-Type': 'application/json'}))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def spam_webhooks(message, webhooks, num_messages):
    print(Fore.YELLOW + "[CONSOLE]: Starting webhook spam...")
    for i in range(num_messages):
        send_messages(message, webhooks)
        print(Fore.GREEN + "[NUKE]: Message Successfully Sent Without Any Issues!")
        time.sleep(5)




# Loading Phase

print(Fore.GREEN + "[CONSOLE]: Discord Nuker Has Loaded!")
time.sleep(.2)
print(Fore.GREEN + "[CONSOLE]: Welcome, ", username,"!")
time.sleep(.2)
print(Fore.BLUE + "[CONSOLE]: Command Prompt Loaded")
webhooks = []
for i in range(4):
    webhookforbot = input(f"Please insert the bot's webhook URL {i+1}: ")
    webhooks.append(webhookforbot)
os.system("cls")

# Debook - this section is not needed and causes errors since response is not defined

# Commands

print(Fore.BLUE + "LIST OF COMMANDS")
print(Fore.GREEN + "[1]: Delete 1 Or More Webhooks.")
print(Fore.GREEN + "[2]: Send A Message Through The Webhooks.")
print(Fore.GREEN + "[3] Spam All 4 Webhooks.")
code_exe = input("Input Command >>>")

# Exit loading phase and onto commands

if code_exe == "1":
    webhook_url = input("Please insert the webhook URL to delete or type 'all' to delete all of them: ")
    if webhook_url.lower() == 'all':
        for webhook in webhooks:
            response = requests.delete(webhook)
            if response.status_code == 204:
                print("Webhook deleted successfully.")
            else:
                print("Error deleting webhook. Status code:", response.status_code)
    else:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print("Webhook deleted successfully.")
        else:
            print("Error deleting webhook. Status code:", response.status_code)

elif code_exe == "2":
    message = input("Input Message >>>")
    send_messages(message, webhooks)

elif code_exe == "3":
    num_messages = int(input("Input Number of Messages >>>"))
    message = input("Input Message >>>")
    spam_webhooks(message, webhooks, num_messages)
