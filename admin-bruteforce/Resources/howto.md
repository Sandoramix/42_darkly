# Admin Credentials Exposure

`/robots.txt` exposes a `whatever` route containing an `htpasswd` file with a hashed `root`
password. The `/admin` route accepts these credentials to display the flag.

## Exploit

1. Fetch `/robots.txt` → find the `whatever` path
2. Fetch `/<whatever>/htpasswd` → copy the `root` hash
3. Crack the hash (MD5) with hashcat or an online tool → `qwerty123@`
4. Log in at `/admin` with `root` / `qwerty123@`

```bash
hashcat -m 0 -a 0 <hash> rockyou.txt
```

## How to prevent

- Never expose `htpasswd` or credential files via the web server
- Restrict access to sensitive paths by IP or require prior authentication
- Use a strong hashing algorithm (bcrypt, scrypt, PBKDF2) — MD5 is broken for passwords
