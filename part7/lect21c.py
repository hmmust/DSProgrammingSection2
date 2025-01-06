import requests

get_result = requests.post("http://httpbin.org/post",
                           params={"key":"Ahmad"})
if get_result:
    print(get_result.url)
    print(get_result.json())
else:
    print("URL not found (Error)")