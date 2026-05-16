# Member SQL Injection

The `/?page=member` search field is vulnerable to SQL injection via `UNION SELECT`.
By injecting into the `id` parameter, an attacker can dump the `Member_Sql_Injection.users` table.

## Exploit

Run `pwn.py` to enumerate schemas → tables → columns → rows. The flag row (user_id=5) hints:

> "Decrypt this password -> then lower all the char. Sh256 on it and it's good !"
> countersign: `5ff9d0165b4f92b14994e5c685cdce28`

```bash
python3 pwn.py
```

1. Decode MD5 `5ff9d0165b4f92b14994e5c685cdce28` → `FortyTwo`

   Use `bruteforcemd5.py` with a wordlist:

   ```bash
   python3 ../../bruteforcemd5.py 5ff9d0165b4f92b14994e5c685cdce28 rockyou.txt
   ```

   Recommended wordlists from [SecLists](https://github.com/danielmiessler/SecLists):
   - `Passwords/Leaked-Databases/rockyou.txt`
   - `Passwords/Most-Popular-Letter-Passes.txt`

2. Lowercase: `fortytwo`
3. SHA256 → flag

## How to prevent

- Use parameterized queries (prepared statements) — never interpolate user input into SQL
- Validate/whitelist input: `id` should be a positive integer only
- Least privilege: DB user should have `SELECT`-only access on needed tables
