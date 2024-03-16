import lxml
from bs4 import BeautifulSoup
with open("index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, 'lxml')

title = soup.title
print(title.text)

page_h1 = soup.find("h1")
print(page_h1.text)

page_h1_all = soup.find_all("h1")
print(page_h1_all)

for title in page_h1_all:
    print(title.text)

links = soup.find_all("a")
for a in links:
    a_text = a.text
    a_url = a.get("href")
    print(a_text, a_url)

