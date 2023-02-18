#Testing Place while develop this repo
import datetime
import pytz
timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
timeformat = f"{timeformat.strftime('(%Y-%m-%d)')}"
def make_table():
    data = dict()
    f = open('README.md')
    lines = f.readlines()
    print(lines[:5])
make_table()