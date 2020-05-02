
import requests
from bs4 import BeautifulSoup as bs

with open('mes_mots.txt') as f:
  lineList = f.readlines()
lineList = [line.rstrip('\n') for line in open('mes_mots.txt')]

#list = lineList[50:70]
url = "https://www.larousse.fr/dictionnaires/francais/"

for word in lineList:
    print('\n', word)

    r = requests.get(url + word)

    soup = bs(r.content , 'lxml')

    try:
        Definitions = soup.findAll("ul", {"class" : "Definitions"})

        meanings = Definitions[0].findChildren("li", recursive = False)


        for (i,meaning) in enumerate(meanings):
            print(str(i+1), meaning.text)

    except:
        print('mot non trouvé !')




