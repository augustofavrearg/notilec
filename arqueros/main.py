import argparse
import logging
import goalkeeper_page_objects as game7
import re
import datetime
import csv
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

from common import config


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
is_well_formed_link = re.compile(r'^https?://.+/.+$') #https://example.com/hello
is_root_path = re.compile(r'^/.+$') #/some-text

def _goalkeeper_scraper(goalkeeper_site_uid):
    host = config()['goalkeeper_site'][goalkeeper_site_uid]['url']
    logging.info('Beggining scraper for {}'.format(host))
    homepage = game7.HomePage(goalkeeper_site_uid, host)

    players = []
    goalkeepers = []
    for link in homepage.game_links:
        player = _fetch_player(goalkeeper_site_uid, host, link)
        goalkeeper = _fetch_goalkeeper(goalkeeper_site_uid, host, link)

        if player:
            logger.info('Player fetched!')
            players.append(player)
        
        if goalkeeper:
            logger.info('Goalkeeper fetched!')
            goalkeepers.append(goalkeeper)
            
    print("Esto es players: ", players)
    print("Esto es goalkeeper: ", goalkeepers)
    #_save_goalkeeper(goalkeeper_site_uid, goalkeepers)

def _save_goalkeeper(goalkeeper_site_uid, articles):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = '{goalkeeper_site_uid}_{datetime}_articles.csv'.format(
        goalkeeper_site_uid = goalkeeper_site_uid,
        datetime = now
    )


    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))
    
    with open(out_file_name, mode='w+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)




def _fetch_player(goalkeeper_site_uid, host, link):
    logger.info('Start fetching article at {}'.format(link))

    player = None

    try: 
        player = game7.GamePage(goalkeeper_site_uid, _build_link(host, link))
        
        
    except(HTTPError, MaxRetryError) as e:
        logger.warning('Error while fetching the article', exc_info= False)
    
    if player and not player.player: 
        logger.warning('Invalid article. There is no body')
        return None

    return player

def _fetch_goalkeeper(goalkeeper_site_uid, host, link):
    logger.info('Start fetching article at {}'.format(link))

    goalkeeper = None

    try: 
        goalkeeper = game7.GamePage(goalkeeper_site_uid, _build_link(host, link))
        
        
    except(HTTPError, MaxRetryError) as e:
        logger.warning('Error while fetching the article', exc_info= False)
    
    if goalkeeper and not goalkeeper.goalkeeper: 
        logger.warning('Invalid article. There is no body')
        return None

    return goalkeeper

def _build_link(host, link):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host, link)
    else:
        return '{host}/{uri}'.format(host = host, uri = link)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    new_site_choices = list(config()['goalkeeper_site'].keys())
    parser.add_argument('goalkeeper_site',
                        help = 'The news site that you want to scrape',
                        type=str,
                        choices= new_site_choices)
    
    args = parser.parse_args()
    _goalkeeper_scraper(args.goalkeeper_site)