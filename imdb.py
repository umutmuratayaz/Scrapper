# UmutMuratAyaz
import requests
from bs4 import BeautifulSoup

url = "https://www.idefix.com/Kategori_/Kirtasiye/Cok-Satanlar/11700/12?gclid=EAIaIQobChMI7Z_ZruOz9QIVVIXVCh0AdgMsEAAYASAAEgJTN_D_BwE&gclsrc=aw.ds"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("div", {"class":"no-margin productListNewBox boxes books clearfix"}).find_all("div",{"class":"col-12 col-xl-3 col-lg-4 col-md-6 col-sm-6 col-xs-6-product filterProductAsyncList itemlittleProduct"})
count = 1

for tr in list:
    title = tr.find("div",{"class":"product-info"}).find("div",{"class":"box-title"}).find("a").text
    yayınevi = tr.find("div",{"class":"product-info"}).find("div",{"class":"box-line-2 brandName"}).text
    fiyat = tr.find("div",{"class":"product-info"}).find("span",{"class":"price price"}).text
    print(f"{count}- Kitap: {title.ljust(70)} ...Yayınevi: {yayınevi.ljust(40)} ...Fiyat: {fiyat}")
    count+=1




