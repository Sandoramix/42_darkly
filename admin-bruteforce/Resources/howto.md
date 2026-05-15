# Page enumeration and password guessing

At /robots.txt there is a link to a `whatever` route which contains a `htpasswd` file. Inside this file there are credentials for the `root`:`<hash>`.

By enumerating (guessing) the available pages on the website, there's a `/admin` route with a login form. By using the username `root` and decrypted password (online) `qwerty123@`, we can access the flag.

## Hot to prevent this

Do not expose the `htpasswd` file, or at least do not allow access to it (auth by IP, auth by cookie, etc.).

<!-- TODO: add details on how to crack the hash with a command (bruteforce/wordlist with hashcat/john) -->