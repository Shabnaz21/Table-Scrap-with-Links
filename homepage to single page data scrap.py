from requests import get
from bs4 import BeautifulSoup as bs
from csv import writer
url = 'https://www.countrycode.org'

res = get(url)
soup = bs(res.text, 'html.parser')
table_body = soup.find('tbody')
table_row = table_body.find

link_list = []
for row in table_body.find_all('a', href=True):
    link_list.append(url + row['href'])

file = open('countrydata2.csv', 'a+')
for link in link_list:
    file.write(f'{link}\n')
file.close()


# urls = []
# for url in urls:



