from bs4 import BeautifulSoup
import requests
import lxml
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

def scraping(row):
    new_link = "https://www.rbi.org.in/Scripts/" + row.a['href']
    return row.text, new_link


#-----------------------------------------------------------------------------------------

rows = soup.find_all('tr')

for row in rows:
    if "tableheader" in str(row):
        date = row.text

    if "<a class" in str(row):
        title, link = scraping(row)
        titles.append(title)
        links.append(link)
        dates.append(date)



data = {'titles': titles, 'links': links, 'dates': dates}
data = pd.DataFrame(data)
data.to_csv('file1.csv', index=False)
