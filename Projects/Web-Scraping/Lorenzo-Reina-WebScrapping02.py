import requests
res = requests.get("https://gutenberg.org/cache/epub/67630/pg67630.txt")
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])
