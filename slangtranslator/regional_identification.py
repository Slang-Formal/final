import requests
import re
from bs4 import BeautifulSoup

#Webscraping for NYC slang
URL = "https://www.berlitz.com/blog/new-york-nyc-slang"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="___gatsby")

#print(results.prettify())

#Parsing html code for NYC slang,then appending the words to a list
slang_words = results.find_all("tr") 
ny_list = []
for slang in slang_words:
    definitions = slang.find_all("td", limit=1)
    for word in definitions:
        ny_list.append((word.text.lower()).replace("’",""))

#print(ny_list)

#Webscraping for British slang
URL = "https://www.wix.com/wordsmatter/blog/2020/10/british-slang-words/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results1 = soup.find(id="SITE_CONTAINER")
#print(results1.prettify())

#Parsing html code for British slang,then appending the words to a list
british_words = results1.find_all('h2')
british_list = []
for slang in british_words:
  definitions = slang.find_all("span", limit = 1)
  for word in definitions:
    new_string = ''
    for characters in word:
      if characters == "’":
        new_chr = "'"
      else:
        new_chr = characters
      new_string += new_chr.text
    british_list.append((new_string[4:]).lower())

british_list

british_list

#Webscraping for california slang
URL = "https://www.berlitz.com/blog/california-slang-words"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="___gatsby")
#print(results.prettify())

#Parsing html code for California slang,then appending the words to a list
cali_words = results.find_all("tr") 
cali_list = []
for slang in cali_words:
    definitions = slang.find_all("td", limit=1)
    for word in definitions:
        #print(word.text)
        cali_list.append((word.text).lower())

#creating a function that identifies region based on amount of regional slang words used based on the webscraped lists
         
def parse(sentence):
  i = 0
  j = 0
  k = 0
  for word in cali_list:
    if re.findall(r'\W' + '(' + word + ')' + '\W', " " +  sentence + " ", re.IGNORECASE):
      i += len(re.findall(r'\W' + '(' + word + ')' + '\W', " " + sentence + " ", re.IGNORECASE))
  for word in ny_list:
    if re.findall(r'\W' + '(' + word + ')' + '\W', " " + sentence + " ", re.IGNORECASE):
      j += len(re.findall(r'\W' + '(' + word + ')' + '\W', " " +  sentence + " ", re.IGNORECASE))
  for word in british_list:
    if re.findall(r'\W' + '(' + word + ')' + '\W', " " + sentence + " ", re.IGNORECASE):
      k += len(re.findall(r'\W' + '(' + word + ')' + '\W', " " + sentence + " ", re.IGNORECASE))
  counter_list = [i,j,k]
  
  if((i == 0) & (j ==0) & (k == 0)):
    return('No Region Detected')
  elif max(counter_list) == i:
    return("California")
  elif max(counter_list) == j:
    return("New York")
  elif max(counter_list) == k:
    return("Britain")