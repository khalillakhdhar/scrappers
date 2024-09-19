#scrap https://en.wikipedia.org/wiki/Python_(programming_language)
import requests
import bs4 
import html5lib
res=requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
# lire les titre h2 du site
soup=bs4.BeautifulSoup(res.text,"html5lib")
headers=soup.select("h2") # retour => tableau
blocs=soup.find("td",class_="infobox-data") # retour => objet

print("blocs "+str(blocs.getText()))
for header in headers:
    print(header.getText())
# récupérer les images 
imgs=soup.select("img")
imageList=[]
for img in imgs:
    #imageList.append(img["src"])
    src=img.get("src")
    alt=img.get("alt")
    imageList.append({"src":src,"alt":alt})
# save as json
import json
#save in data.json file
with open("data.json","w") as file:
    json.dump(imageList,file)