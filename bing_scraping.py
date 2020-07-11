#pip install icrawler
#python bing_scraping.py filename keyword num
import os
import sys
from icrawler.builtin import BingImageCrawler

if __name__ == '__main__':
    path = 'root_dir' + 'bing'
    if not os.path.isdir(path):
        os.makedirs(path)

    args = sys.argv
    crawler = BingImageCrawler(storage={'root_dir': 'bing' + '/' + str(args[1])})
    filters = {
        'size': 'large',
        'type': 'photo'
        }
    crawler.crawl(keyword= str(args[2]), filters=filters, max_num= int(args[3])) #max_num: 1000
