import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = input("Enter narou url: ")
name = input("name: ") + ".txt"

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

subtitle = soup.find(class_="novel_subtitle").get_text()
page = [ para.get_text() for para in soup.find(id="novel_honbun").find_all('p')]

with open(name, 'wb') as f:
    f.write(subtitle.encode())
    f.write("\n\n".encode())
    f.write("\n".join(page).encode())
