import requests

get_result = requests.get("https://www.uop.edu.jo")
if get_result:
    print(get_result.url)
    print(get_result.text)
else:
    print("URL not found (Error)")