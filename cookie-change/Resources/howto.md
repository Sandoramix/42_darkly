# Cookie Change

The website enforces for each user a cookie called `I_am_admin` with value `68934a3e9455fa72420237eb05902327`, which is the MD5 hash of the string `false`.
By changing the value of this cookie to `true` converted to MD5 hash (`b326b5062b2f0e69046810717534cb09`), the website will show the flag with an alert popup on the page refresh.

## Hot to prevent this

The purpose of the cookie is not quite clear, it seems to be used for some kind of autorization (becoming an admin) without a proper authentication.

The best approach is to use a proper authentication, also with a cookie which will be used to identify the user and not its role.