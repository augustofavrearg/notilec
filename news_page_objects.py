import bs4
import requests
import os
import requests

from common import config

class NewsPage:

    def __init__(self, news_site_uid, url):
        self._config = config()['news_site'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None
        self._visit(url)

    def _select(self, query_string):
            return self._html.select(query_string)
        
    def _visit(self, url):
        response = requests.get(url)

        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')

class HomePage(NewsPage):

    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)

    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)
                

        return set(link['href'] for link in link_list)

class ArticlePage(NewsPage):
    
    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)
    
    @property
    def body(self):
        results = self._select(self._queries['article_body'])
        return [result.text for result in results]

    @property
    def title(self):
        results = self._select(self._queries['article_title'])
        return [result.text for result in results]
    
    @property
    def img(self):
        results = self._select(self._queries['article_img'])
        return [result['href'] for result in results]
    
    def download_images(self, output_folder='images'):
        img_urls = []

        # Buscar imágenes dentro de elementos <a> con la clase 'story-card-img-ctn'
        img_containers = self._select(self._queries['article_img'])
        for container in img_containers:
            img_tag = container.find('img')
            if img_tag and img_tag.has_attr('src'):
                img_urls.append(img_tag['src'])

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i, img_url in enumerate(img_urls):
            img_response = requests.get(img_url)

            if img_response.status_code == 200:
                img_filename = os.path.join(output_folder, f"image_{i + 1}.jpg")

                with open(img_filename, 'wb') as img_file:
                    img_file.write(img_response.content)

                print(f"Image {i + 1} downloaded: {img_filename}")
            else:
                print(f"Failed to download image {i + 1}: {img_url}")
