# Login

http://10.12.250.191/whatever/
The application allows authentication using a valid password regardless of the username. By discovering a password (in this case the password is “shadow”) in /whatever/, an attacker can log in as any user without needing a valid username.
The backend may be performing a query similar to:
SELECT * FROM users WHERE password = 'shadow';

## How to prevent

- Authentication must always check credentials as a pair.

- Remove passwords or secrets from public endpoints.