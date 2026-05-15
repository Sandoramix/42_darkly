# Page Param Path Traversal

The `?page=` parameter is used to include files dynamically without sanitization. By injecting
`../` sequences, an attacker can read arbitrary files on the server.

## Exploit

```
http://<IP>/?page=../../../../../../../../../../../etc/passwd
```

The server returns the contents of `/etc/passwd`.

## How to prevent

- Validate `page` against an explicit allowlist of known page names
- Reject any input containing `../`, `/`, or null bytes (`%00`)
- Resolve the full path and verify it stays within the intended base directory before including
