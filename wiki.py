# scrapping de https://en.wikipedia.org/wiki/Python_(programming_language)
import requests
r=requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
print("text "+r.text)
print("status code "+str(r.status_code))
print("headers "+str(r.headers))
print("encoding "+str(r.encoding))
print("cookies "+str(r.cookies))
print("history "+str(r.history))
print("url "+str(r.url))
print("elapsed "+str(r.elapsed))
print("request "+str(r.request))
print("connection "+str(r.connection))
print("content "+str(r.content))
print("raw "+str(r.raw))
# save as json
import json
#save in data.json file
with open("data.json","w") as file:
    json.dump(r.text,file)
