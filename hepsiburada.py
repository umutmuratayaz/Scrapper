# UmutMuratAyaz
import requests
from bs4 import BeautifulSoup

kategori = input("Aramak isteğiniz kategori: ")
sayfa = input("Kaç sayfa aramak istiyorsunuz: ")
sıralama = input("Sıralama Ölçütü:\n1-En çok Satanlar\n2-Değerlendirme Sayısı\n3-Beğeni Sayısı\n4-Artan Fiyat\n5-Azalan Fiyat\n6-En Yeniler\n7-Ürün Puanı\nSeçiminiz: ")

if sıralama == 1:
    sıralama="coksatan"
elif sıralama==2:
    sıralama="yorumsayisi"
elif sıralama==3:
    sıralama="begenisayisi"
elif sıralama==4:
    sıralama="artanfiyat"
elif sıralama==5:
    sıralama="azalanfiyat"
elif sıralama==6:
    sıralama="enyeni"
elif sıralama==7:
    sıralama="degerlendirmepuani"
else:
    sıralama="coksatan"

url = "https://www.hepsiburada.com/ara?q="+kategori+"&sayfa="+sayfa+"&siralama="+sıralama

# url ="https://www.hepsiburada.com/nevresim-takimlari-c-510001"

# Response[403]  yanıtı vermemesi için
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

html=requests.get(url,headers=headers).content

soup=BeautifulSoup(html, "html.parser")

list = soup.find_all("li",{"class":"productListContent-item"})


for li in list:
    name = li.div.a.h3.text
    link = "www.hepsiburada.com"+li.div.a.get("href")
    try:
        oldprice = li.find("div",{"data-test-id":"price-prev-price"}).div.text.strip().strip("TL")
        discount = li.find("div",{"data-test-id":"price-prev-price-discount"}).text.strip()
    except AttributeError:
        oldprice = "--"
        discount = "--"
        
    currentprice = li.find("div",{"data-test-id":"price-current-price"}).text.strip().strip("TL")

    try:
        review = li.find("div",{"data-test-id":"review"}).div.text.strip()
    except AttributeError:
        review = "--"
    print(f"||name: {name}\n||old price: {oldprice.ljust(8)} ||discount: {discount.ljust(8)} ||new price: {currentprice.ljust(8)} ||review: {review.ljust(5)} ||link: {link} \n\n")
