import re
import requests

print("Enter ingredients in this format aaaa,bbbb,cccc")

ingredient = input("Enter ingredients:")
print(ingredient)

url = "https://www.food2fork.com/api/search?key=42c5f0fa1cf934475b5325034d15061f&q=TOBEREPLACED&page=2"

newUrl = re.sub('TOBEREPLACED',ingredient,url)

print(newUrl)
r = requests.get(newUrl)
print(r.json())
