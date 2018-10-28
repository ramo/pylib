import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.hackerrank.com"


def get_links(relative_url, link_id_props, name_id_props):
    print('Scraping url: ', relative_url)
    page = requests.get(f'{BASE_URL}/{relative_url}')
    soup = BeautifulSoup(page.text, 'html.parser')
    links = []
    for link in soup.find_all(link_id_props['tag'], link_id_props['id']):
        name = link.next.find(name_id_props['tag'], name_id_props['id']).contents[0]
        url = link.get('href')
        links.append({'name': name, 'url': url})

    return links


def main():
    print('============================Fetching all the interview questions============================')
    st = time.time()
    init_url = 'interview/interview-preparation-kit'
    categories = get_links(init_url, {'tag': 'a', 'id': {'class': 'base-card'}},
                           {'tag': 'div', 'id': {'class': 'LinesEllipsis'}})
    for category in categories:
        challenges = get_links(category['url'], {'tag': 'a', 'id': {'class': 'js-track-click challenge-list-item'}},
                               {'tag': 'h4', 'id': {'class': 'challengecard-title'}})
        category['challenges'] = challenges

    print('================Categories and challenges============')
    for category in categories:
        print('name = ', category['name'])
        print('url = ', category['url'])
        print('============================================================')
        for challenge in category['challenges']:
            print('name = ', challenge['name'])
            print('url = ', challenge['url'])
        print('============================================================')
    print('=======================Done==========================');
    et = time.time()
    print('Time taken: ', et - st)


if __name__ == '__main__':
    main()
