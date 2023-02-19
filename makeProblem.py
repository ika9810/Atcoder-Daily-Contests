import requests
from operator import itemgetter
import csv
import random

# specify the URL to retrieve the data from
url = 'https://kenkoooo.com/atcoder/resources/problem-models.json'

# create a session object to handle the HTTP requests
session_obj = requests.Session()

# send a GET request to the specified URL with the headers to mimic a web browser
response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})

# get the JSON data from the response
data = requests.get(url).json()

# define a function to calculate the Kyu rank of a problem based on its difficulty level
def kyu(difficulty):
    if difficulty <= 399:
        return {"Kyu" : "9 Kyu", "Color" : "lightgrey"}
    elif difficulty >= 400 and difficulty <= 799:
        if difficulty <= 599:
            return {"Kyu" : "8 Kyu", "Color" : "critical"}
        else:
            return {"Kyu" : "7 Kyu", "Color" : "critical"}
    elif difficulty >= 800 and difficulty <= 1199:
        if difficulty <= 999:
            return {"Kyu" : "6 Kyu", "Color" : "brightgreen"}
        else:
            return {"Kyu" : "5 Kyu", "Color" : "brightgreen"}
    elif difficulty >= 1200 and difficulty <= 1599:
        if difficulty <= 1399:
            return {"Kyu" : "4 Kyu", "Color" : "green"}
        else:
            return {"Kyu" : "3 Kyu", "Color" : "green"}
    elif difficulty >= 1600 and difficulty <= 1999:
        if difficulty <= 1799:
            return {"Kyu" : "2 Kyu", "Color" : "blue"}
        else:
            return {"Kyu" : "1 Kyu", "Color" : "blue"}
    elif difficulty >= 2000 and difficulty <= 2399:
        if difficulty <= 2199:
            return {"Kyu" : "1 Dan", "Color" : "yellow"}
        else:
            return {"Kyu" : "2 Dan", "Color" : "yellow"}
    elif difficulty >= 2400 and difficulty <= 2799:
        if difficulty <= 2599:
            return {"Kyu" : "3 Dan", "Color" : "orange"}
        else:
            return {"Kyu" : "4 Dan", "Color" : "orange"}
    elif difficulty >= 2800:
        return {"Kyu" : "5 Dan or higher", "Color" : "red"}
    else:
        return {"Kyu" : "Unknown", "Color" : "black"}
    
# Extract the list of problem ID
keys = [key for key in data]

res = []
print(sorted(keys))
for key in keys:
    try:
        con = ['abc','arc','agc']
        if key[:3] in con:
            pass
        else:
            continue
        res.append({'Problem': key, 'Difficulty': data[key]["difficulty"], 'Link' : "https://atcoder.jp/contests/" + key.split("_")[0] + "/tasks/" + key, 'Contest' : "https://atcoder.jp/contests/" + key.split("_")[0]})
    except:
        print("here",data[key])
data = sorted(res, key=itemgetter('Difficulty'))
f = open('Problem_List.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(["Number",'Problem', 'Difficulty', "Kyu", "Color", "Link", "Contest"])
for i in range(len(data)):
    key = data[i]['Problem'].upper()
    value = data[i]["Difficulty"]
    link = data[i]['Link']
    contest = data[i]["Contest"]
    Kyu = kyu(value)["Kyu"]
    Color = kyu(value)["Color"]

    wr.writerow([i+1,key,value,Kyu,Color,link,contest])
f.close()
kyu9 = []
kyu8 = []
kyu7 = []
kyu6 = []
kyu5 = []
kyu4 = []
kyu3 = []
kyu2 = [] 
kyu1 = [] 
dan1 = [] 
dan2 = [] 
dan3 = [] 
dan4 = [] 
dan5 = [] 
f = open('Problem_List.csv','r')
rdr = csv.reader(f)

for line in rdr:
    if line[3]  == "9 Kyu":
        kyu9.append(line)
    elif line[3]  == "8 Kyu":
        kyu8.append(line)
    elif line[3]  == "7 Kyu":
        kyu7.append(line)
    elif line[3]  == "6 Kyu":
        kyu6.append(line)
    elif line[3]  == "5 Kyu":
        kyu5.append(line)
    elif line[3]  == "4 Kyu":
        kyu4.append(line)
    elif line[3]  == "3 Kyu":
        kyu3.append(line)
    elif line[3]  == "2 Kyu":
        kyu2.append(line)
    elif line[3]  == "1 Kyu":
        kyu1.append(line)
    elif line[3]  == "1 Dan":
        dan1.append(line)
    elif line[3]  == "2 Dan":
        dan2.append(line)
    elif line[3]  == "3 Dan":
        dan3.append(line)
    elif line[3]  == "4 Dan":
        dan4.append(line)
    elif line[3]  == "5 Dan or higher":
        dan5.append(line)
    print(line)
f.close()
A = kyu9
B = kyu9
C = kyu9 + kyu8
D = kyu7 + kyu6
E = kyu5 + kyu4 + kyu3 + kyu2
F = kyu1 + dan1
G = dan2 + dan3
H = dan4 + dan5 
problemArr = [A,B,C,D,E,F,G,H]

import datetime
import pytz
timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
timeformat = f"{timeformat.strftime('(%Y-%m-%d)')}"
saveline = ["🌟Today's Virtual Atcoder Beginner Contest\n", '========\n', '[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fika9810%2FAtcoder%2Fblob%2Fmain%2FABC.md&count_bg=%23FFC8C8&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)\n', "[![오늘의 문제](https://img.shields.io/badge/Today's%20ABC-Link-lightpink)](https://github.com/ika9810/Atcoder/blob/main/ABC.md)  \n", '[![Email](https://img.shields.io/badge/Email-ika7204@naver.com-ff69b4)](mailTo:ika7204@naver.com)\n']
title = "### 🌟Today's Virtual Atcoder Beginner Contest "+timeformat
saveline.append(title + '\n')
saveline.append("(Notes: The problems in this contest were curated based on their level of difficulty and listed from Atcoder's existing problems)\n")
saveline.append("\n")
saveline.append("| # | Problem |Rate| Kyu | Difficulty | Contest |\n")
saveline.append("|---| ----- | :--------: | :----------: | :----------: | ---------- |\n")
plus = "-"
minus = "--"

["🌟Today's Virtual Atcoder Beginner Contest\n", '========\n', '[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fika9810%2FAtcoder%2Fblob%2Fmain%2FABC.md&count_bg=%23FFC8C8&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)\n', '[![오늘의 문제](https://img.shields.io/badge/오늘의%20문제%20%28BETA%29-바로가기-112051)](https://github.com/tony9402/baekjoon/blob/main/picked.md) \n', '[![Email](https://img.shields.io/badge/Email-ika7204@naver.com-ff69b4)](mailTo:ika7204@naver.com)\n', "### 🌟Today's Virtual Atcoder Beginner Contest (23-02-19)\n", "(Notes: The problems in this contest were curated based on their level of difficulty and listed from Atcoder's existing problems)\n", '\n', '| # | Problem |Rate| Kyu | Difficulty | Contest |\n', '|---| ----- | :--------: | :----------: | :----------: | ---------- |\n', '|A|[AGC010_A](https://atcoder.jp/contests/agc010/tasks/agc010_a)|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|9 Kyu|-1438|[https://atcoder.jp/contests/agc010](https://atcoder.jp/contests/agc010)|\n', '|B|[AGC010_A](https://atcoder.jp/contests/agc010/tasks/agc010_a)|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|9 Kyu|-1438|[https://atcoder.jp/contests/agc010](https://atcoder.jp/contests/agc010)|\n', '|C|[AGC010_A](https://atcoder.jp/contests/agc010/tasks/agc010_a)|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|9 Kyu|-1438|[https://atcoder.jp/contests/agc010](https://atcoder.jp/contests/agc010)|\n', '|D|[AGC010_A](https://atcoder.jp/contests/agc010/tasks/agc010_a)|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|9 Kyu|-1438|[https://atcoder.jp/contests/agc010](https://atcoder.jp/contests/agc010)|\n', '|E|[AGC010_A](https://atcoder.jp/contests/agc010/tasks/agc010_a)|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|9 Kyu|-1438|[https://atcoder.jp/contests/agc010](https://atcoder.jp/contests/agc010)|\n', '|F|[AGC010_A](https://atcoder.jp/contests/agc010/tasks/agc010_a)|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|9 Kyu|-1438|[https://atcoder.jp/contests/agc010](https://atcoder.jp/contests/agc010)|\n', '|G|[AGC010_A](https://atcoder.jp/contests/agc010/tasks/agc010_a)|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|9 Kyu|-1438|[https://atcoder.jp/contests/agc010](https://atcoder.jp/contests/agc010)|\n', '|H|[AGC010_A](https://atcoder.jp/contests/agc010/tasks/agc010_a)|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|9 Kyu|-1438|[https://atcoder.jp/contests/agc010](https://atcoder.jp/contests/agc010)|\n', '\n']
for i in range(65,73):
    "|A|[AGC010_A](https://atcoder.jp/contests/agc010/tasks/agc010_a)|![Rate](https://img.shields.io/badge/9%20Kyu---1438-lightgrey)|9 Kyu|-1438|[https://atcoder.jp/contests/agc010](https://atcoder.jp/contests/agc010)|\n"
    res = random.choice(problemArr[i-65])
    val = plus if int(res[2])>0 else minus
    msg = "|"+ chr(i)+"|["+res[1]+"]("+res[5]+")|![Rate](https://img.shields.io/badge/"+res[3].replace(" ","%20") + val + res[2]+ "-" + res[4] + ")|" + res[3].replace("%20", " ") + "|" + res[2] + "|[" + res[6] + "]("+ res[6] +")|\n"
    saveline.append(msg)
saveline.append("\n")

f = open('ABC.md')
lines = f.readlines()
f.close()
with open('./ABC.md', 'w') as f:
    f.writelines(saveline + lines[5:])
    f.close()
f = open('README.md')
lines = f.readlines()
f.close()
with open('./README.md', 'w') as f:
    f.writelines(lines[:-14] + saveline[5:])
    f.close()
#Atcoder Problem List
# I used This Link "https://kenkoooo.com/atcoder/resources/problem-models.json"
# I referred to "https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md"