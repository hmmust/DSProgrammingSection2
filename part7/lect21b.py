import requests

get_result = requests.get("https://www.google.com/search",
                          params={"q":"Sara"})
if get_result:
    print(get_result.url)
    print(get_result.text)
else:
    print("URL not found (Error)")