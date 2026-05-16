import hashlib
import sys
import os

#   python3 bruteforcemd5.py <hash> <wordlist>

"""
Useful wordlists
https://github.com/danielmiessler/SecLists:
- https://github.com/danielmiessler/SecLists/blob/master/Passwords/Most-Popular-Letter-Passes.txt
- https://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt
- https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz
"""

if len(sys.argv) != 3:
    print("python3 bruteforcemd5.py <hash_md5> <wordlist>")
    sys.exit(1)

target_hash = sys.argv[1].lower()
wordlist_path = sys.argv[2]

if not os.path.exists(wordlist_path):
    print(f"Wordlist non trovata: {wordlist_path}")
    sys.exit(1)

print("Avvio dictionary attack...")
print(f"Hash target: {target_hash}")
print(f"Wordlist: {wordlist_path}")

found = False

with open(wordlist_path, "r", encoding="latin-1") as file:
    for line in file:
        password = line.strip()
        md5_hash = hashlib.md5(password.encode()).hexdigest()
        if md5_hash == target_hash:
            print("\nPASSWORD TROVATA!")
            print(f"Password: {password}")
            found = True
            break

if not found:
    print("\nPassword non trovata nella wordlist.")