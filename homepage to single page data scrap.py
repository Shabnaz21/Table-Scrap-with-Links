from requests import get
from bs4 import BeautifulSoup as bs

url = 'https://www.countrycode.org'

res = get(url)
soup = bs(res.text, 'html.parser')
table_body = soup.find('tbody')
table_row = table_body.find_all('a')

file = open('Url data.csv', 'a+')
for link in table_row:
    data = link.get('href')
    Full_link = (url+data)
    file.write(Full_link)
    file.write('\n')
file.close()






