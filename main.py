import requests, re, urllib.request
from bs4 import BeautifulSoup

chart = 'https://music.bugs.co.kr/chart'
 # Start Website to webscrape from

chartdoc = BeautifulSoup(requests.get(chart).text, 'html.parser')
# Using bs4 to process the page 

temp = [] # temp list to find all links related to genre.

for link in chartdoc.findAll('a', {'class': 'hyrend'}): 
    temp.append(link.get('href'))
# Finds all the genre and appends them to temp

genredoc = BeautifulSoup(requests.get(temp[4]).text, 'html.parser')
 # Using bs4 again to process the webpage for genre. 

kpop = [] # List that will contain all the genres
kpoptitles = {} # Dictionary for userinput later on 

for link in genredoc.findAll('a',{'class': 'hyrend'}):
    kpop.append(link.get('href'))
# Finds all genres with links to each genre page

prefi = 'https://music.bugs.co.kr/genre/chart/kpop'
# Above link is used as prefix to find all links that has to do 
# with genre.

for links in kpop:
    if prefi in links:
        kpoptitles[(links[42:-10])] = links
# Finds all links with prefixes. Then, creates keys/values for genre
# and links to that genre

for genres in kpoptitles:
    print(genres)
# Prints out all the genres available


