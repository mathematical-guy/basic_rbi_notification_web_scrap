from bs4 import BeautifulSoup
import requests
# import lxml
import pandas as pd

url = "https://www.rbi.org.in/Scripts/NotificationUser.aspx"

response = requests.get(url = url)
html_file = response.text

soup = BeautifulSoup(html_file, 'lxml')

table = soup.table

titles = []
links = []
dates = []

#-----------------------------------------------------------------------------------------

def scrapper(row):
    try:
        title = row.text
        link = str(row.find_all('a', target='_blank')).split(' ')[1]
        # print(link)
    except:
        link = None
        # print(f'TITLE: {title}')
        # print(f'LINK: {link}')
    return title, link


#-----------------------------------------------------------------------------------------

rows = soup.find_all('tr')

for row in rows:
    if "tableheader" in str(row):
        date = row.text

    if "<a class" in str(row):
        title, link = scrapper(row)
        titles.append(title)
        links.append(link)
        dates.append(date)


data = {'titles': titles, 'links': links, 'dates': dates}
data = pd.DataFrame(data)
data.to_csv('file1.csv', index=False)
