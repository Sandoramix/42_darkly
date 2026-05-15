# Directory Listing Enumeration

The web server exposes directory listings under `/.hidden/`. The script recursively follows
all links, reads every file, and reports those containing the flag.

## Exploit

```bash
python3 pwn.py
```

## How to prevent

Disable directory listing on the web server:

**Nginx:**
```nginx
autoindex off;
```

**Apache:**
```apache
Options -Indexes
```

Block access to `.hidden` entirely via server config or firewall rules.
