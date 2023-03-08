from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup


def get_info(searchVar):
    searchVar = '_'.join([e.capitalize() for e in searchVar.strip().split(' ')])
    info = getLinks("/wiki/"+searchVar)
    return info


def getLinks(articleURL):
    try:
        html = urlopen("https://en.wikipedia.org"+articleURL)
        data = BeautifulSoup(html.read(),"html.parser")
        try:
            title = data.h1.get_text()
            paragraphs = data.find(id='mw-content-text').findAll('p')
            image = "https://en.wikipedia.org"+data.find(class_ ='image').attrs['href']
            imageHtml = urlopen(image)
            imgData = BeautifulSoup(imageHtml.read(),"html.parser")
            img_url = "https:"+imgData.find("div",{"class":"fullImageLink"}).find("a").attrs["href"]
            

            return {'title':title,'image':img_url,'paragraphs':paragraphs}

        except:
            print("page missing something")
            return 1
    
    except:
        return 1


