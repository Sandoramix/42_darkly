# Cookie Privilege Escalation

The site sets a cookie `I_am_admin` to the MD5 of `false`. Changing it to the MD5 of `true`
grants admin access and renders the flag on page refresh.

| Value   | MD5                                |
|---------|------------------------------------|
| `false` | `68934a3e9455fa72420237eb05902327` |
| `true`  | `b326b5062b2f0e69046810717534cb09` |

## Exploit

In browser DevTools (Application → Cookies), set `I_am_admin` to `b326b5062b2f0e69046810717534cb09`
and refresh the page.

## How to prevent

- Never encode authorization state in a client-side cookie without a server-side signature
- Use signed/encrypted session tokens (e.g. HMAC-signed JWT or server-side sessions) so
  clients cannot forge their own role
