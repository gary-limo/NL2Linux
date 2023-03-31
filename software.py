import os
import sys
import time
import math
import requests
import json
import subprocess
from getpass import getpass
import curses


HOST = "https://api.openai.com/v1/"
COMPLETIONS = "chat/completions"
MODEL = "gpt-3.5-turbo"
PROMPT = "I want you to reply with linux command and nothing else. Do not write explanations."
API_KEY_FILE = ".openai_api_key"

def init_key():
    if not os.path.isfile(API_KEY_FILE):
        api_key = getpass("Enter your OpenAI API key: ")
        with open(API_KEY_FILE, "w") as f:
            f.write(api_key)
    with open(API_KEY_FILE, "r") as f:
        api_key = f.read().strip()
    return api_key

def completions(api_key, prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "system", "content": PROMPT}, {"role": "user", "content": prompt}],
    }
response = requests.post(HOST + COMPLETIONS, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_json = response.json()
        reply = response_json["choices"][0]["message"]["content"]
        return reply.strip()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return ""

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}\n{e.output}")
"""

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
        print(f"Output:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}\n{e.output}")

"""

def print_blinking_command(command):
    separator = "*" * 20
    command_output = f"Linux command: {command:<16} "

    for i in range(1):  # Number of blinks
        print(separator)
        print(f"\033[31m{command_output}\033[0m")  # Print in red color
        print(separator)
        time.sleep(0.5)  # LED on time

def main():
    api_key = init_key()

    if len(sys.argv) < 2:
        print("Please provide a natural language instruction as an argument.")
        return

    user_input = " ".join(sys.argv[1:])

    result = completions(api_key, user_input)

    if result != "":
        #print(f"Natural language instruction: {user_input}")
        print("\n")
        print_blinking_command(result)
        #print(f"Linux command: {result}")
        execute_command(result)

if __name__ == "__main__":
    main()




