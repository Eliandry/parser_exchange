import requests
from bs4 import BeautifulSoup

EURO = 'https://www.google.ru/search?newwindow=1&client=opera&sxsrf=ALeKk01z7Zv71DCVUExCLz-JPIXtDRGvvQ%3A1585302666167&ei=isx9XoDPCeGAk74Pi9-Q8Ag&q=курс+евро&oq=курс+евро&gs_l=psy-ab.1.0.0i131i70i258j0i131i20i263l2j0j0i131j0j0i67j0l3.1288827.1291879..1293667...1.3..0.220.1561.0j7j2......0....1..gws-wiz.....10..0i71j35i362i39j35i39j0i131i67j35i39i70i258j0i20i263.05SlAWaayuc'
DOLLAR = 'https://www.google.ru/search?newwindow=1&client=opera&hs=7Mo&sxsrf=ALeKk009g0zJ8nOlsPbtQCZb4XwvdSa2oQ%3A1585300321696&ei=YcN9XtCRKsHh6QTYwraYBQ&q=доллар+к+рублю&oq=доллар+к+рублю&gs_l=psy-ab.3..0i131i70i258j0j0i131l2j0l6.2325305.2342192..2342552...14.1..0.226.3774.0j24j1......0....1..gws-wiz.....10..0i71j35i362i39j0i10i1j0i10i1i42j0i10j0i13i30.jG-yUAz0h7s&ved=0ahUKEwiQxqX0p7roAhXBcJoKHVihDVMQ4dUDCAo&uact=5'
user = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97'}


fullPage_dollar = requests.get(DOLLAR, headers=user)
fullPage_euro = requests.get(EURO, headers=user)

soup_dollar = BeautifulSoup(fullPage_dollar.content, 'html.parser')
soup_euro = BeautifulSoup(fullPage_euro.content, 'html.parser')

convert_dollar = soup_dollar.findAll("span", {"class": "DFlfde", "class": "SwHCTb"})
convert_euro = soup_euro.findAll("span", {"class": "DFlfde", "class": "SwHCTb"})

print(str(convert_dollar[0].text) + "$")
print(str(convert_euro[0].text) + "€")