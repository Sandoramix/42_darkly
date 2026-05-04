# Survey Tampering

By changing any \<select\>'s \<option\> value and then submitting the form, you can change get the flag.

This means that the server is blindly trusting the client which is very dangerous.

## How to prevent

The solution is to have server-side validation of the form data.