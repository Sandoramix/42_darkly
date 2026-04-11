# ?redirect

The website has a footer with a link to the `?redirect=<social>` page, which is used to redirect the user to a social media page.
The link is vulnerable to redirection, so if the user enters in `?redirect=<malicious_url>` the website will redirect the user to the malicious URL without any validation. This can cause a phishing attack (redirecting the user to a malicious website from a "trusted" origin).

So if the user enters in `<IP>/http://index.php?page=redirect&site=https://projects.intra.42.fr/42cursus-darkly/mine` th flag will be rendered.

## Hot to prevent this

Ideally the website should have a proper validation/whitelisting for authorized redirection URLs.