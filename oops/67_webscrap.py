import requests
from bs4 import BeautifulSoup

url = 'https://youtube.com'  
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# title = soup.title.string

# print(f'The title of the webpage is: {title}')




links = soup.find_all('a')

for link in links:
    href = link.get('href')
    if href:
        print("__________________________________")
        print(href)