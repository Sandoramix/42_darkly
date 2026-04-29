# Feedback XSS

There is something wrong with the feedback form, it is not vulnerable to XSS but upon putting a specific single character in the `name` and `message` fields, the page will render the flag.

Possible set of single characters that can be entered are: `atcslerip<>`

So if the user enters inside `name` `a` or `t` in `message` field the page will render the flag.

<!-- <form method="post" name="guestform" onsubmit="return validate_form(this)">
modificare onsubmit -->


## Intended Vulnerability

This is a XSS vulnerability where you inject `<script>` JS code into the `name` or `message` fields. It doesn't work like this because on the server side the function used to check the input `strstr` has inverted the parameters and instead of checking if the string contains the substring (`<script>` is present inside the given input, e.g: `<script>alert(1)</script>`), it checks if the substring is contained in the string (if given input is present inside `<script>`, e.g. `s`).

## How to prevent this

Do not allow the user to enter `<script>` in the `name` or `message` fields. There are many ways to do this, for example, you can use a whitelist of allowed characters, or you can "strip" (remove) all html elements from the input before saving it in the database.
Or you can show the input as plaintext and not as html.