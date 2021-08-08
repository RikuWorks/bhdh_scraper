import os
import random
import requests
import markdown
import time
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
              "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
              "Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/52",
              "Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A345 Safari/525.20",
              "Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5B108 Safari/525.20",
              "Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F136 Safari/525.20",
              "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16",
              "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; ja-jp) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16", 
                "Mozilla/5.0 (Linux; U; Android 3.1; en-us; K1 Build/HMJ37) AppleWebKit/534.13(KHTML, like Gecko) Version/4.0 Safari/534.13",
                "Mozilla/5.0 (Linux; U; Android 3.1; ja-jp; AT100 Build/HMJ37) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
                "Mozilla/5.0 (Linux; U; Android 3.1; ja-jp; Sony Tablet S Build/THMAS10000) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
                "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; SC-01D Build/MASTER) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
                "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; AT1S0 Build/HTJ85B) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
                "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; F-01D Build/F0001) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
                "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; Sony Tablet S Build/THMAS11000) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
                "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; A01SH Build/HTJ85B) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
                "Mozilla/5.0 (Linux; U; Android 3.2.1; ja-jp; Transformer TF101 Build/HTK75) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13"
              ]
ut = int(time . time ( ))
print("Input Title")
title=input()
print("Input URL")
url=input()
print("Input Trying Range")
try_num=int(input())
savename="_thumb.jpg"
os.makedirs(str(ut)+"/files", exist_ok=True)
cnt=0
for i in range(1,try_num+1):
    temp=i
    sm=str(temp).zfill(3)
    name=str(ut)+"/files/"+sm+savename
    surl=url+sm+savename
    print(surl)
    headers = {"User-Agent": random.choice(user_agent)} 
    a = requests.get(surl,headers=headers)
    if a !=404 or 403:
        urlData = requests.get(surl,headers=headers).content
        with open(name ,mode="wb") as fm: # wb でバイト型を書き込める
            fm.write(urlData)
        cnt=cnt+1
    else:
        break
path=str(ut)+"/"+title+".html"
with open(path, mode='a',encoding='utf-8') as f:
    f.write('\n<!doctype html>')
    f.write('\n<html lang="ja">')
    f.write('\n<head>')
    f.write('\n  <meta charset="UTF-8">')
    f.write('\n<title>')
    f.write(title)
    f.write('\n</title>')
    f.write('\n<h1>')
    f.write(title)
    f.write('\n</h1>')
    f.write('\n<link rel="stylesheet" href="style.css">')
    f.write('\n</head>')
    f.write('\n<body>')
for i in range(1,cnt+1):
    temp=i
    sm=str(temp).zfill(3)
    name="files/"+sm+savename
    with open(path, mode='a',encoding='utf-8') as f:
        f.write('\n<div class="class1">')
        f.write('\n<img src="')
        f.write(name)
        f.write('">')

with open(path, mode='a',encoding='utf-8') as f:
    f.write('\n</body>')
    f.write('\n<html>')
path=str(ut)+"/style.css"
with open(path, mode='a',encoding='utf-8') as fc:
    fc.write('\n.class1 {')
    fc.write('\n  text-align: center;')
    fc.write('\n}')
    fc.write('\nh1 {')
    fc.write('\n    text-align:center')
    fc.write('\n}')