import requests, re, urllib.request
from bs4 import BeautifulSoup

def addTitles(doc,s,dic,l):
    for i in doc.findAll(s,dic):
        l.append(i.text[1:-1])
    return l
# A function for appending all titles in a webpage into a list.

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
# Finds all links with prefixes. Then, creates keys/values for genre and links to that genre

boo = True # Loopy doo
topchart = [] # Initializing a list to store all top titles

while boo:
    inp = int(input('1 for Top Chart\n2 for Top Chart in specific Genre\nEnter Here: '))
    # User input to choose between broad or narrow
    if inp == 1:
        usern = int(input("Enter up to how many songs you want to see (Up to 100): "))
        topchart = addTitles(chartdoc,'p',{'class':'title'},topchart)[0:usern]
        print('Here are the',usern,'most popular songs')
    elif inp == 2:
        for genres in kpoptitles:
            print(genres.upper())
        # Prints out all the genres available for users
        print('RNH = rock&hiphop | RNS = r&bsoul') # Just in case for users
        userin = input("What are you feeling?\n\nEnter a genre from above: ")
        usern = int(input("Enter up to how many songs you want to see (Up to 100): "))
        userpick = BeautifulSoup(requests.get(kpoptitles[userin]).text,'html.parser')
        topchart = addTitles(userpick,'p',{'class':'title'},topchart)[0:usern]
        print('Here are the',usern,'most popular songs in the',userin,'genre.')
    else:
        print('You may only enter 1 or 2')
        continue
    
    
    for n, i in enumerate(topchart):
        print(n+1,'. ',i,sep='')
    redo = input('y to startover\nn to exit')
    if redo == 'y':
        continue
    elif redo =='n':
        print('Have a great day :)')
        break
    else:
        print('y or n please')
    


# Ask for genre


# Render the website the user chose to webscrape


# Searches for the top {usern} songs and appends to topn


# prints the songs out




