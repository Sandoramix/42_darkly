# Directory enum

The script recursively scans the .hidden directory and discovers files containing the flag by parsing directory listings and following all links.
The web server exposes the contents of directories  instead of blocking access. This allows attackers to enumerate files and subdirectories.

## How to prevent this

- Disable directory listing

Configure the web server to prevent listing files, for example:
In Nginx:
autoindex off;
In Apache HTTP Server:
Options -Indexes

- Block access to .hidden entirely