import requests
res = requests.get("https://gutenberg.org/cache/epub/67630/pg67630.txt")
res.raise_for_status()
playFile= open("TheCopperEskimo.txt", "wb")
for chunk in res.iter_content(50000):
    playFile.write(chunk)
playFile.close()

# The text has a total of 310364 characters. I took the first 50000.