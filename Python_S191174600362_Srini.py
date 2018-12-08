##Web Scraping final
import requests
from bs4 import BeautifulSoup
num=0
r = requests.get('https://amazon.in')
word=str(input("Enter Word: "))
print("Response Code :", r) 
soup = BeautifulSoup(str(r.text), 'html.parser')
html_doc=str(r.text)
with open('count.txt','w')as files:
  files.write(html_doc)
with open('count.txt','r')as f:
  for line in f:
    words=line.split()
    for i in words:
      if(i==word):
        num=num+1
print('Word Count: ',num)
