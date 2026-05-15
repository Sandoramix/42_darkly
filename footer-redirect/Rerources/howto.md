# Open Redirect

The footer contains social media links that use `?redirect=<site>` to redirect users.
The `site` parameter is not validated, so any URL can be supplied, redirecting users to
arbitrary external sites. This enables phishing by abusing a trusted origin.

## Exploit

Navigate to:

```
http://<IP>/index.php?page=redirect&site=https://projects.intra.42.fr/42cursus-darkly/mine
```

The flag is rendered on that page.

## How to prevent

- Whitelist allowed redirect targets (e.g. only `instagram`, `facebook`, `twitter`)
- Reject or block any `site` value that is not in the whitelist
- Never pass raw user input directly to a redirect function
