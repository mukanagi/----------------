import logging
import collections


import requests
import bs4

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('oz')


# ParseResult = collections.namedtuple(
#     'ParseResult',
#     (
#         'model name'
#         'price'
#         'url',
#     ),
# )

class Client():
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
            'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
        }

        self.result = []

    def load_page(self):
        url = 'https://www.wildberries.ru/catalog/0/search.aspx?search=hobot'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text()

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('')

        for block in container:
            self.parse_block(block=block) 

    def parse_block(self, block):
        # logger.info(block)
        # logger.info('=' * 100)

        url_block = block.select_one('a.product-card__main.j-card-link')
        if not url_block:
            logger.error('no url_block')
            return
        
        url = url_block.get('href')
        if not url_block:
            logger.error('no href')
            return

    # def run(self):
    #     text = self.load_page()
    #     self.parse_page(text=text)

        logger.info('%s', url)
    
if __name__== '_main__':
    parser = Client()
    parser.run()

        
