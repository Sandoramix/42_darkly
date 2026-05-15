# Survey Form Tampering

The survey form uses `<select>` dropdowns. The server accepts any value for the option,
including values not present in the original HTML. Submitting a tampered value triggers the flag.

## Exploit

In browser DevTools, edit any `<option>` value to an arbitrary number and submit the form.

## How to prevent

- Validate submitted values server-side against the set of allowed options
- Never trust client-supplied form data — the server must be the source of truth for valid choices
