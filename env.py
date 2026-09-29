import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
app_name = os.getenv("APP_NAME")

print(f"Hello {username}")
print(f"the app is called {app_name}")


