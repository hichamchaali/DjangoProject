from requests import session
import requests
import lxml.html as lh
import pandas as pdb 
from bs4 import BeautifulSoup
payload = {
    'appAction': 'login',
    'username': 'hichamchaalii@gmail.com',
    'password': '57Z66pQD7nSc'
}

with session() as c:
    c.post('https://app.factomos.com/connexion', data=payload)
    request = c.get('https://app.factomos.com/mes-factures')
   # print (request.headers)
    #print (request.text)
    #soup = BeautifulSoup(request.text, 'html.parser')
    #print(soup.prettify())
    #My_table = soup.find('td',{'class':'ITEM-CLIENT'})
    #print(My_table) 
    soup=BeautifulSoup(request.text,'html.parser')
    tbd = soup.find('tbody')
    tbd_rows = tbd.find_all('tr')
    for tr in tbd_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        print(row)
 
