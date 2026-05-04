# Albatroz

In the page's sources there are a lot of comments. Two of them mention to use the "ft_bornToSec" browser (user agent) and the other one says to come from "https://ww.nsa.gov/" (referer)

curl --user-agent "ft_bornToSec" --referer "https://www.nsa.gov/" http://<ip>/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

The application restricts access to a resource based on HTTP headers such as User-Agent and Referer. By modifying these headers, an attacker can bypass the protection and access hidden functionality (e.g., the flag).


## How to prevent

- Do not trust client-side headers
Headers like User-Agent and Referer are fully controllable by the client
They must never be used for authentication or authorization.