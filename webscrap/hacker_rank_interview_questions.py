import time
import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.hackerrank.com"


def get_full_url(relative_url):
    return f'{BASE_URL}/{relative_url}'


def get_links(relative_url, link_id_props, name_id_props):
    print('Scraping url: ', relative_url)
    page = requests.get(get_full_url(relative_url))
    soup = BeautifulSoup(page.text, 'html.parser')
    links = []
    for link in soup.find_all(link_id_props['tag'], link_id_props['id']):
        name = link.next.find(name_id_props['tag'], name_id_props['id']).contents[0]
        url = link.get('href')
        links.append({'name': name, 'url': url})

    return links


def get_data():
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

    # process the relative urls
    for category in categories:
        category['url'] = get_full_url(category['url'])
        for challenge in category['challenges']:
            challenge['url'] = get_full_url(challenge['url'])

    et = time.time()
    print('Time taken: ', et - st)
    return categories


def get_json_data():
    categories = get_data()
    json_str = json.dumps(categories, indent=4)
    return json_str


def print_csv_data():
    categories = get_data()
    rows = []
    for category in categories:
        category_name = category['name']
        for challenge in category['challenges']:
            rows.append(','.join([category_name, f'=HYPERLINK("{challenge["url"]}", "{challenge["name"]}")']))

    print('\n'.join(rows))


def main():
    # print_csv_data()
    json_str = get_json_data()
    print(json_str)


if __name__ == '__main__':
    main()
