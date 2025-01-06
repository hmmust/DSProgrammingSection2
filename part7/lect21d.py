import requests
import pandas as pd
get_result = requests.get("https://raw.githubusercontent.com/hmmust/DSProgrammingSection2/refs/heads/main/part6/students1.json")
if get_result:
    print(get_result.url)
    students1 = pd.DataFrame(get_result.json())
    print(students1)
else:
    print("URL not found (Error)")