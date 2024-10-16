# Author:wjw
# Development date: 2024/10/13
import requests
from fake_useragent import UserAgent
from lxml import etree
from random import randint
from time import sleep
def get_html(url):
    headers = {
        "User-Agent":UserAgent().random
    }
    sleep(randint(3, 10))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None
def parse_index(html):
    e = etree.HTML(html)
    all_url = e.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
    return ['http://maoyan.com{}'.format(url) for url in all_url]

def parse_info(html):
    e = etree.HTML(html)
    name = e.xpath('//h1[@class="name"]/text()')[0]
    types = e.xpath('//li[@class="ellipsis"]/a/text()')[0]
    actors = e.xpath('//li[@class="celebrity actor"]/div[@class="info"]/div/text()')
    actors = format_actors(actors)
    return {
        "name":name,
        "types":types,
        "actors":actors
    }

def format_actors(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip())
    return actor_set


def main():
    index_url = 'https://www.maoyan.com/films?showType=2&offset=0'
    html = get_html(index_url)
    movie_urls = parse_index(html)
    for url in movie_urls:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie)

if __name__ == '__main__':
    main()