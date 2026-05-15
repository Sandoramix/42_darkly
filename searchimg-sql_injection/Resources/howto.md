# Search Image SQL Injection

The `/?page=searchimg` search field is vulnerable to SQL injection via `UNION SELECT`.
By injecting into the `id` parameter, an attacker can dump the `Member_images.list_images` table.

## Exploit

Run `pwn.py` to enumerate schemas → tables → columns → rows. The flag row (id=5) has:

> "If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46"

```bash
python3 pwn.py
```

1. Decode MD5 `1928e8083cf461a51303633093573c46` → `albatroz`
2. Lowercase: `albatroz`
3. SHA256 → flag

## How to prevent

- Use parameterized queries (prepared statements) — never interpolate user input into SQL
- Validate/whitelist input: `id` should be a positive integer only
- Least privilege: DB user should have `SELECT`-only access on needed tables
