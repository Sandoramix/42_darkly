# Feedback XSS

The feedback form has a broken `strstr` check intended to block `<script>` tags. The parameters
are swapped: instead of checking if `<script>` is present in the input, it checks if the input
is present inside the string `<script>`. Any single character from `atcslerip<>` satisfies this
check and causes the server to render the flag.

## Exploit

Enter any single character from `atcslerip<>` in the `name` or `message` field and submit.

## Intended Vulnerability

This is a stored XSS vulnerability. The intended exploit is to inject `<script>alert(1)</script>`
into `name` or `message`. It fails because `strstr($input, "<script>")` has its arguments
reversed — it tests whether the input exists inside the literal string `"<script>"`, not the
other way around.

## How to prevent

- Strip or escape HTML from user input before saving to the database
- Render user content as plaintext, not raw HTML
- Use a whitelist of allowed characters for form fields
