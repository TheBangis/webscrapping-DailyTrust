import requests
from bs4 import BeautifulSoup

url = 'https://dailytrust.com/87-days-to-go-buhari-races-to-complete-legacy-projects'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title.get_text())

paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.get_text())
