
import requests
from bs4 import BeautifulSoup

# open file with list of url
f = open("urlsurls_directories.txt", "r")
print(f.readline()) 

# loop reading the file lines
# get first url
url = f.readline()

# get html file
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

# extract the url and related content - html title and url link info
# instert the extracted url in urls.txt for futur run
# save to sql database the url and info for search functionnailty

print(output)
