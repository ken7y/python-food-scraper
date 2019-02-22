import re
import requests


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
        print(i)

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
list1.listsize()

# About to start the n-1 loops

#need to regex the ingredients to curl
#need to store recipes
#need to chop linkedlists
#need to loop through chopped linked list






# url = "https://www.food2fork.com/api/search?key=42c5f0fa1cf934475b5325034d15061f&q=TOBEREPLACED&page=1"
#
# newUrl = re.sub('TOBEREPLACED',ingredient,url)
#
# print(newUrl)
# r = requests.get(newUrl)
# # print(r.json())
#
# for recipe in r.json()['recipes']:
#     # print(recipe)
#     for title in recipe['title']:
#         print(title, end="")
#     print("")
