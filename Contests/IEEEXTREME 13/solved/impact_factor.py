import re, math, decimal, bisect
from json import loads
from functools import cmp_to_key
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
# code goes here
n = iread()
publications = loads(read())
articles = []
for i in range(n - 1):
    articles.append(loads(read()))

ans = []
for p in publications["publications"]:
    id = p["publicationNumber"]
    articleCount = sum([int(a["articleCount"]) for a in p["articleCounts"] if a["year"] == "2017" or a["year"] == "2018"])
    citationCount = 0
    for a in articles:
        for c in a["paperCitations"]["ieee"]:
            if id == c["publicationNumber"] and (c["year"] == "2017" or c["year"] == "2018"):
                citationCount += 1
    ans.append((p["publicationTitle"],citationCount / articleCount))

ans.sort(key=cmp_to_key(lambda A, B: -1 if A[1] > B[1] else 1 if B[1] > A[1] else 1 if A[0] > B[0] else -1))
for a in ans:
    print(f"{a[0]}: {a[1]:.02f}") 