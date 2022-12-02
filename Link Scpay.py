from csv import writer
from requests import get
from bs4 import BeautifulSoup as bs

file = open('Url data.csv')
url_list = file.readlines()
file.close()

for country in url_list:
    single_url = country.strip('\n')
    url = single_url
    res = get(url)
    soup = bs(res.text, 'html.parser')
    table_data = soup.find('div', {'id':'collapseCityCodes'})
    table_body = table_data.find('tbody')
    table_row = table_body.find_all('tr')

    def create_csv(list):
        file = open('All City Codes.csv', 'a+', newline='')
        write = writer(file)
        write.writerow(list)
        file.close()

    for row in table_row:
        td = row.find_all('td')
        data_list = []
        for data in td:
            data_list.append(data.text)
        create_csv(data_list)