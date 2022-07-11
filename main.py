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
# Prints out all the genres available for users

print('rnh = rock&hiphop | rns = r&bsoul') # Just in case for users

userin = input("What are you feeling\nEnter a genre from above: ")
# Ask for genre

userpick = BeautifulSoup(requests.get(kpoptitles[userin]).text,'html.parser')
# Render the website the user chose to webscrape
topn = []
usern = int(input("Enter up to how many songs you want to see (Up to 100): "))

for titles in userpick.findAll('p',{'class':'title'}):
    if len(topn) == usern:
        break
    topn.append(titles.text[1:-1])
# Searches for the top {usern} songs and appends to topn

print('Here are the',usern,'most popular songs in the',userin,'genre.')
for n, i in enumerate(topn):
    print(n+1,'. ',i,sep='')
# prints the songs out




