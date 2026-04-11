from bs4 import BeautifulSoup
import requests
import time
from requests.adapters import Retry, HTTPAdapter

url = 'http://10.12.250.191/.hidden'

def listFD(url):
    try :
        retry = Retry(total=10, connect=5, read=5, allowed_methods=['GET'], backoff_factor=10)
        session = requests.Session()
        session.mount("http://", HTTPAdapter(max_retries=retry))
        page = session.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href')]
    except :
        return []

files = listFD(url)
f = open("demofile.txt", "w")
index = 0
for file in files:
    #print(file)
    if index == 100:
        time.sleep(1)
        index = 0
    if file.endswith('/') and not file.endswith('/../') :
        files.extend(listFD(file[:len(file) - 1]))
    elif file.endswith('/../') :
        continue
    else :
        try :
            page = requests.get(file).text
            exclude = [
                "Tu veux de l'aide ? Moi aussi !",
                "Non ce n'est toujours pas bon ...",
                "Demande",
                #"Demande Ã  ton voisin du dessous",
                #"Demande Ã  ton voisin de gauche",
                "Toujours pas tu vas craquer non ?"
            ]
            skip = False
            for word in exclude:
                if page.startswith(word) :
                    skip = True
                    break
            if skip == False :
                f.write(f"{file} : {page}")
        except :
            continue
f.close()

