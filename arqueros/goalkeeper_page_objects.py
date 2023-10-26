import bs4
import requests

from common import config

class GoalkeeperPage:

    def __init__(self, goalkeeper_site_uid, url):
        self._config = config()['goalkeeper_site'][goalkeeper_site_uid]
        self._queries = self._config['queries']
        self._html = None
        self._visit(url)

    def _select(self, query_string):
            return self._html.select(query_string)
        
    def _visit(self, url):
        response = requests.get(url)

        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')

class HomePage(GoalkeeperPage):

    def __init__(self, goalkeeper_site_uid, url):
        super().__init__(goalkeeper_site_uid, url)

    @property
    def game_links(self):
        link_list = []
        for link in self._select(self._queries['goalkeeper_game_links']):
            if link and link.has_attr('href'):
                link_list.append(link)
        print(link_list)
                

        return set(link['href'] for link in link_list)

class GamePage(GoalkeeperPage):
    
    def __init__(self, goalkeeper_site_uid, url):
        super().__init__(goalkeeper_site_uid, url)
    
    @property
    def player(self):
        results = self._select(self._queries['game_players'])
        player_list = []

        for result in results:
            player_list.append(result.text)
        
        return print("Esto es player list: ", player_list)
    
    @property
    def goalkeeper(self):
        results = self._select(self._queries['game_goalkeeper'])
        goalkeeper_list = []

        for result in results:
            # Seleccionar solo los spans con estilo exacto "color:#000"
            valid_spans = result.select('.samarreta-acta2 > span[style="color:#000;"]')
            for span in valid_spans:
                # Agregar el elemento hermano (la <td>) a goalkeeper_list
                td_sister = span.find_next('td')
                if td_sister:
                    goalkeeper_list.append(td_sister.text)


        return print("Esto es goalkeeper list: ", goalkeeper_list)




    @property
    def title(self):
        results = self._select(self._queries['article_title'])
        return [result.text for result in results]

    
