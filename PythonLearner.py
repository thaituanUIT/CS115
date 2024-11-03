import operator
import math

_dict = {
    0 : 10,
    1 : 40,
    2 : 30,
    3 : 0,
    4 : 10
 }

dict_2 = {
    6 : 70,
    7 : 90,
    8 : 60,
    9 : 80
}

dict_3 = {}

def updateDict():
    for d in (_dict, dict_2):
        dict_3.update(d)
    dict_3.update({5 : 50})
    print(dict_3)
    
def sortedItems():
    _sorted= sorted(dict_3.items(), key = operator.itemgetter(1))
    rev_sorted = sorted(dict_3.items(), key = operator.itemgetter(1), reverse = True)
    print(_sorted, rev_sorted)
    
def Iterate():
    for dict_3_key, dict_3_value in dict_3.items():
        print(dict_3_key, "-->", dict_3_value)
    
def createDict():
    n = int(input("Input a number: "))
    dictionary = {}
    for i in range(1, n + 1):
        dictionary[i] = i * i
    print(dictionary)

def conditionalFind():
   contain = {}
   for x in range (1, 16):
       contain[x] = x ** 2
   print(contain)
   
def mergeDict(dict_1, dict_2):
    res = {**dict_1, **dict_2}
    return res

def findMaximum(_dict):
    max_value = max(_dict.values())
    max_key = max(_dict.keys())
    print(max_value, max_key)
    
def NestedDict():
    sampleDict = {
        "Student" : {
            "name" : "Mike",
            "mark" : {
                "history" : 80,
                "physics" : 90
                }
            }
        }
    print(sampleDict.get("Student").get("mark").get("history"))
    
def fromKeys():
    employee = {"Tran", "Tu"}
    job = {"Salary" : 800, "Profile" : "none"}
    
    new_dict = dict.fromkeys(employee, job)
    print(str(new_dict))
    
def ExtractKeys():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

    keys = ["name", "salary"]
    
    res = dict(filter(lambda item: item[0] in keys, sample_dict.items()))
    
    print(str(res))
    
    

def main():
    updateDict()
    sortedItems()
    Iterate()
    createDict()
    conditionalFind()
    findMaximum(dict_2)
    merge = mergeDict(_dict, dict_2)
    print(merge)
    NestedDict()
    fromKeys()
    ExtractKeys()
    
if __name__ == "__main__":
    main()




