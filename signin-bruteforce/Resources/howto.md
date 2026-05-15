# Login

http://10.12.250.191/whatever/
The application allows authentication using a valid password regardless of the username. By discovering the credentials from other vulnerability (sql injection on member page), we found that the password is `shadow` after decrypting it from md5.
The backend may be performing a query similar to:
SELECT * FROM users WHERE password = 'shadow';

## How to prevent

- Authentication must always check credentials as a pair.
- Use a strong hashing algorithm (bcrypt, scrypt, PBKDF2, etc.)
- Use a salt


## Intended way to exploit

This vulnerability is intended to be a brute force attack.
It can be done by using the most common usernames and passwords wordlists.
The best way to do it is to use:
- [Hydra](https://github.com/vanhauser-thc/thc-hydra) for the brute force attack
- [Most-Popular-Letter-Passes.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Most-Popular-Letter-Passes.txt) password list
- [top-usernames-shortlist.txt](https://github.com/danielmiessler/SecLists/blob/master/Usernames/top-usernames-shortlist.txt) username list

`Hydra` can use these wordlists to perform the wordlist attack and it can exclude results by filtering the content of the page. For this case when the password is wrong it shows an image sourced to `images/WrongAnswer.gif` and we can exclude it from the results.

When doing the login on the browser in network tab the request looks like this: `http://[ip]/?page=signin&username=<username>&password=<password>&Login=Login`

So we can use the following command to perform the attack:

```bash
hydra -L  top-usernames-shortlist.txt -P Most-Popular-Letter-Passes.txt -e images/WrongAnswer.gif [IP] http-post-form "/:page=signin:username=^USER^:password=^PASS^:Login=Login:Login=Login"
```

The `-e` option is used to exclude results from the page.