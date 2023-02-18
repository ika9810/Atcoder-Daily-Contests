import requests
from operator import itemgetter
import csv

url = 'https://kenkoooo.com/atcoder/resources/problem-models.json'
session_obj = requests.Session()
response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})

data = requests.get(url).json()

def kyu(difficulty):
    if difficulty <= 399:
        return {"Kyu" : "9 Kyu", "Color" : "grey"}
    elif difficulty >= 400 and difficulty <= 799:
        if difficulty <= 599:
            return {"Kyu" : "8 Kyu", "Color" : "brown"}
        else:
            return {"Kyu" : "7 Kyu", "Color" : "brown"}
    elif difficulty >= 800 and difficulty <= 1199:
        if difficulty <= 999:
            return {"Kyu" : "6 Kyu", "Color" : "green"}
        else:
            return {"Kyu" : "5 Kyu", "Color" : "green"}
    elif difficulty >= 1200 and difficulty <= 1599:
        if difficulty <= 1399:
            return {"Kyu" : "4 Kyu", "Color" : "mint"}
        else:
            return {"Kyu" : "3 Kyu", "Color" : "mint"}
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
    
def make_table():
    data = dict()
    with open('./scripts/picked.json', 'r') as f:
        data = json.load(f)
        f.close()

    saveline = []
    keys = data.keys()
    for key in keys:
        saveline.append(f"## {key} \n")
        saveline.append('\n')
        saveline.append("| 난이도 | 번호 | 문제 이름 |\n")
        saveline.append("|:------:|:----:|:---------:|\n")
        for problem in data[key]:
            problemInfo = api.request(problem)
            problemName = problemInfo.get('problemName')
            problemLevel = problemInfo.get('problemLevel')
            imageurl = f"<img height=\"25px\" width=\"25px\" src=\"https://static.solved.ac/tier_small/{problemLevel}.svg\"/>"
            line = f"| {imageurl} | [{problem}](https://www.acmicpc.net/problem/{problem}) | [{problemName}](https://www.acmicpc.net/problem/{problem}) |\n"
            saveline.append(line)

        saveline.append('\n')

    with open('./picked.md', 'w') as f:
        f.writelines(saveline)
        f.close()
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
wr.writerow(["Number",'Problem', 'Difficulty', "Grade", "Link", "Contest"])
for i in range(len(data)):
    key = data[i]['Problem']
    value = data[i]["Difficulty"]
    link = data[i]['Link']
    contest = data[i]["Contest"]
    rate = kyu(value)
    
    wr.writerow([i+1,key,value,rate,link,contest])
f.close()

#Atcoder Problem List
# I used This Link "https://kenkoooo.com/atcoder/resources/problem-models.json"
# I referred to "https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md"