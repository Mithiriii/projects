from bs4 import BeautifulSoup
import requests
html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')
first_paragraph_text = soup.p.text
first_paragraph_word = soup.p.text.split()
first_paragraph_id = soup.p['id']           #generuje błą klucza KeyError w wypadku braku klucza
first_paragraph_id2 = soup.p.get('id')      #zwraca none w przypadku braku klucza
all_paragraphs = soup.find_all('p')
paragraph_with_ids = [p for p in soup('p') if p.get('id')]
#znaczniki o określonej klasie
important_paragraphs = soup('p', {'class': 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p') if 'important' in p.get('class', [])]

