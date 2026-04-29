# Upload content-type enforcement

There is a file upload form on the website, which allows the user to upload an image file.

By uploading a file that is not an image (e.g. .php file) but with a valid content-type of an image, the website will show the flag.

## Hot to prevent this

Make a server-side validation of the content-type by checking the mime type (binary) of the file.