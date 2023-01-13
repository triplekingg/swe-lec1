import statistics
import re
import sys

def is_valid(text: str) -> bool:
    return not bool(re.search(r'[a-zA-Z]',text))

def findStat(item1):
   print("mean", statistics.mean(item1), "sid", statistics.stdev(item1), "min", min(item1), "max", max(item1)) 


def appendFile(filepath):
    item1 = []
    with open(filepath, 'r') as f:
        for text in f.readlines():
            if is_valid(text):
                item1.append(int(text))
    return item1
             
def stat(filepath):
    item1 = appendFile(filepath[1])
    item2 = appendFile(filepath[2])
    print('Statistics Summary')
    print(filepath[1])
    findStat(item1)
    print(filepath[2])
    findStat(item2)
    findStat(item1+item2)
    

def main():
    filepath = sys.argv
    if len(filepath) < 3:
        print("need 2 argument")
    else:
        stat(filepath)
main()
