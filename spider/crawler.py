import requests
import time
import pandas as pd
from parse import *
from savedb import DbSaver


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS  10_11_4) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0/2743.116 Safari/537.36'
}


class Crawler:
    def __init__(self):
        self.url = [
            'https://ncov.dxy.cn/ncovh5/view/pneumonia',
            'https://covidtracking.com/data/state/',
            'https://www.who.int/news-room/releases'
        ]
        self.session = requests.Session()
        self.session.headers.update(headers)
        self.db_saver = DbSaver()

    def run(self):
        response = self.session.get(self.url[0])
        response.encoding = 'utf-8'
        res_country = parse_country(response.text)
        res_china = parse_china(response.text)
        # self.db_saver.save_countries(res_country)
        self.db_saver.save_data(res_country, 2)
        self.db_saver.save_data(res_china, 2)

        usa_state_list = [
            'alabama', 'alaska', 'american-samoa', 'arizona',
            'arkansas', 'california', 'colorado', 'connecticut',
            'delaware', 'district-of-columbia', 'florida', 'georgia',
            'guam', 'hawaii', 'idaho', 'illinois',
            'indiana', 'iowa', 'kansas', 'kentucky',
            'louisiana', 'maine', 'maryland', 'massachusetts',
            'michigan', 'minnesota', 'mississippi', 'missouri',
            'montana', 'nebraska', 'nevada', 'new-hampshire',
            'new-jersey', 'new-mexico', 'new-york', 'north-carolina',
            'north-dakota', 'northern-mariana-islands', 'ohio', 'oklahoma',
            'oregon', 'pennsylvania', 'puerto-rico', 'rhode-island',
            'south-carolina', 'south-dakota', 'tennessee', 'texas',
            'us-virgin-islands', 'utah', 'vermont', 'virginia',
            'washington', 'west-virginia', 'wisconsin', 'Wyoming'
        ]
        res_usa = []
        for state in usa_state_list:
            print('***** visiting state %s *****' % state)
            response = self.session.get(self.url[1] + state)
            res_usa.append(parse_usa(response.text, state))
        # self.db_saver.save_provinces(res_china, res_usa)
        self.db_saver.save_data(res_usa, 3)

        url_prefix = 'https://www.who.int'
        pages = ['', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9', '/10']
        for i, page in enumerate(pages):
            print('***** visiting page %s *****' % str(i + 1))
            response = self.session.get(self.url[2] + page)
            news_url_list = parse_news_index(response.text)
            for news_url in news_url_list:
                response = self.session.get(url_prefix + news_url)
                news_dict = parse_news_content(response.text)
                news_dict['link'] = news_url
                self.db_saver.save_news(news_dict)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
    crawler.db_saver.close()
