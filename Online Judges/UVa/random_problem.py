from random import randint
import requests
import json

response = requests.get("https://uhunt.onlinejudge.org/api/p")

if response.status_code == 200:
    problems = response.json()
    problem = problems[randint(0, len(problems) - 1)]
    print(f"{problem[1]}: {problem[2]}")
else:
    print("unable to connect to api endpoint")
