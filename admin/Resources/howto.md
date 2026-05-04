# Admin path

http://10.12.250.190/admin/#

The endpoint /admin/ is directly accessible without  authentication.
The backend does not verify whether the user is logged in and has authorization before directing to the /admin page.

## How to prevent this

Use proper authentication and handle login sessions (session management or token-based authentication).
Never rely on frontend logic for security.