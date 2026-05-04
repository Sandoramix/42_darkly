# Path traversal

http://10.12.250.190/?page=/../../../../../../../../../../../../../../etc/passwd

The application includes files dynamically based on the page parameter without proper validation. By manipulating this parameter with directory traversal sequences (../), an attacker can access sensitive files on the server, such as /etc/passwd.

The application does not block sequences like ../, allowing navigation outside the intended directory.
This works because the application blindly trusts user input when accessing the filesystem.

## How to prevent

- Validate and sanitize input
Reject any input containing:
../
/
null bytes (%00)

- Use a fixed base directory
Resolve paths safely and verify they stay within that directory