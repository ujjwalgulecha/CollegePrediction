from bs4 import BeautifulSoup
import urllib
import re

#Open the edulix page for UCSD
data = open("Edulix.html",'r').read()
soup = BeautifulSoup(data)

#Links
links = []

#Storing all the links
for link in soup.find_all('a'):
    	links.append("http://www.edulix.com/unisearch/" + link['href'])

f = open('Quant.txt','w')
f2 = open('Verb.txt','w')
#Requesting data and printing it
for i in range(32,len(links)-17):
	page = urllib.urlopen(links[i])
	soup2 = BeautifulSoup(page.read())
	f.write(soup2.find(text="Quantitative:").findNext('td').contents[0])
	f2.write(soup2.find(text="Verbal:").findNext('td').contents[0])

f.close()
f2.close()
