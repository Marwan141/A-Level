import re
liststr = ["a" , "bcaa", "bca", "bcbca", "bcabca"]

statement = "^[bc]*[a]$"

for i in liststr:
    result = bool(re.match(statement, i))
    print(result)