import csv
from . import graph


def load_map(filename):
    if DB not in filename:
        filename = DB+filename
        print(filename)
    with open(filename) as f:
        reader = csv.reader(f)
        cnt = 0
        for row in reader:
            print (row)
            cnt +=1
            if(cnt == 3):
                break

if __name__ == '__main__':
    load_map('israel.csv')
