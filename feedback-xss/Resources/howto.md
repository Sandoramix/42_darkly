# Feedback XSS

There is something wrong with the feedback form, it is not vulnerable to XSS but upon putting a specific single character in the `name` and `message` fields, the page will render the flag.

Possible set of single characters that can be entered are: `atcslerip<>`

So if the user enters inside `name` `a` or `t` in `message` field the page will render the flag.

<!-- <form method="post" name="guestform" onsubmit="return validate_form(this)">
modificare onsubmit -->

## Hot to prevent this

Use a proper server-side validation for the `name` and `message` fields.
