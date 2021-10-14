import json
from numpy import array, short
from numpy.lib.function_base import copy
from numpy.lib.index_tricks import index_exp
import pandas as pd
#from pandas._libs.tslibs.period import get_period_ordinal

#data = json.load(open('dictionary_compact.json'))





def main():
    runAnagrams()
    
    
#input of arr letters

def runAnagrams():
    global shortWordsSet
    global good 
    good = []
    shortWordsSet = set(pd.read_csv('short_sorted.csv').squeeze())
    letters = input("Enter the letters with no spaces all together as one word ie abcdef: ")
    anagrams(letters)
    good.sort(key=len)
    good.reverse()
    print(good)


def anagrams(letters):
    tried = set()
    for x in range(len(letters)):
        if letters[x] not in tried:
            searchAna(letters[x], letters[0:x]+letters[x+1:6])
        tried.add(letters[x])


def searchAna(cur, remaining):
    #print(cur)
    if cur in shortWordsSet:
        good.append(cur)
    for x in range(len(remaining)):
        searchAna(cur+remaining[x], remaining[0:x]+remaining[x+1:len(remaining)])


#covert the dictionary with definations in a json to just a csv of the words
def removeDefinition(jsonFile):
    data = json.load(open(jsonFile))
    tempList = array(data.keys)
    arr = []
    for x in data.keys():
        arr.append(x)
    pdArr = pd.array(arr, copy=False)
    df = pd.DataFrame(pdArr).sort_values(by=0, key= lambda x: x.str.len())
    df.to_csv("keys_by_len.csv", header=None, index=None)
    short = pd.read_csv('short_text.csv')
    print(short.columns)
    short.sort_values(by='0').to_csv("short_sorted.csv", header=None, index=None)
    pd.DataFrame(pdArr).sort_values(by=0).to_csv("keys.csv", header=None, index=None)
    



if __name__ == "__main__":
    main()