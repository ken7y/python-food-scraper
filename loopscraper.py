import re
import requests

def CallingFunction(ingreds):
    url = "https://www.food2fork.com/api/search?key=90913c69b33ea8fe0282a999efd60a44&q=TOBEREPLACED&page=1"
    newUrl = re.sub('TOBEREPLACED',ingreds,url)
    r = requests.get(newUrl)
    for recipe in r.json()['recipes']:
        # print(recipe)
        for title in recipe['title']:
            print(title, end="")
        print("")

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
        self.lastval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def listsize(self):
        i = 0
        printval = self.headval
        while printval is not None:
            i+=1
            printval = printval.nextval
        return i

print("Enter ingredients in this format aaaa,bbbb,cccc")
ingredient = input("Enter ingredients:")

# List of ingredients split into an array called arr
arr = re.split(',',ingredient)
print(arr)

# Start of linked list code. Converting array into linked list
# headval points to the head and lastval points to the last node
list1 = SLinkedList()
node1 =  Node(arr[0])
list1.headval = node1
for ingreds in arr:
    if(ingreds != arr[0]):
        node1.nextval = Node(ingreds)
        node1 = node1.nextval
        list1.lastval = node1


#All ingredients pull
print("All the ingredients\n")
CallingFunction(ingredient)
print("\n\n")



lenn = list1.listsize()

# About to start the n-1 loops
for x in range(list1.listsize()):
    str = ""
    listlength = lenn
    node2 = list1.headval
    while(listlength!=1):
        str=str+node2.dataval + ","
        listlength-=1;
        node2 = node2.nextval
    nodeTemp = list1.headval
    list1.headval = list1.headval.nextval
    list1.lastval.nextval = nodeTemp
    list1.lastval = list1.lastval.nextval
    str = str[:-1]
    print ("These ingredients:" + str + "\n")
    CallingFunction(str)
    print("\n\n")

#need to regex the ingredients to curl
#need to store recipes
#need to chop linkedlists
#need to loop through chopped linked list
