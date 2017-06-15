import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.eltiempo.es/granada/polen"

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, "html.parser")

table=soup.find('table', class_='m_table-basic m_pollen-data')


names = []
levels = []

for row in table.findAll("tr"):
    cells=row.findAll("td")

    if(len(cells) != 0):
        names.append(cells[0].find(text=True))
        levels.append(cells[1].find("i").attrs["class"][0][-1])


PolenDataSet = list(zip(names, levels))


df = pd.DataFrame(data= PolenDataSet, columns=["Names", "Levels"])

date = time.strftime("%d-%m-%Y")


df.to_csv("polen-"+date+".csv",index=False,header=False)
