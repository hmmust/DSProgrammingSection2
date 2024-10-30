from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("NAME"),os.getenv("PASSWORD"))
print(os.getenv("TEMP"))
print(os.getenv("JAVA_HOME"))