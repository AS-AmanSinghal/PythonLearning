import requests
from bs4 import BeautifulSoup
import pprint

pageNumber = int(input("Enter Page Number? \n"))
res = requests.get('https://news.ycombinator.com/news?p='+str(pageNumber))

soup = BeautifulSoup(res.text,'html.parser')
# print(soup.body.contents) #return content in list
# print(soup.find_all('div')) #return list of div
# print(soup.a) #return first a tag

# print(soup.select('.score'))


def createHackerNewsFilter(links,subtext) :
    newsList = []
    for index,link in enumerate(links):

        title = links[index].getText()
        href = links[index].get('href',None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points >99 :
                newsList.append({'title':title,'link':href,'point':points})
    return newsList

def sortStoriesBySort(list):
    return sorted(list,key= lambda key:key['point'],reverse=True)

links = soup.select('.storylink')
subtext = soup.select('.subtext')

filteredData = createHackerNewsFilter(links,subtext)

pprint.pprint(sortStoriesBySort(filteredData))