import requests, bs4
res = requests.get('https://www.sanignacio.pr/sobre-csi/historia-del-colegio')
res.raise_for_status()
SanIgnaciopr = bs4.BeautifulSoup(res.text, 'html.parser')
elems = SanIgnaciopr.select('p')
print(type(SanIgnaciopr))
print(len(elems))
# print(str(elems))
print(str(elems[2].getText))