from googlesearch import search
import requests
from bs4 import BeautifulSoup 

query = "weather"
url = ''
flag = True

for j in search(query,tld="com",num=10,stop=1,pause=2):
    
    if flag == True:
        url = j
        flag = False
    else:
        pass 

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
page = requests.get(url,headers=agent)
soup = BeautifulSoup(page.text,'html.parser')

city = soup.find_all("span",class_="current-city")
degree = soup.find_all("span",class_="large-temp")

print("The weather today in {0} is {1}C".format(city[0].text,degree[0].text))
