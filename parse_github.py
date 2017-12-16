import requests
from bs4 import BeautifulSoup

GIT_BASE_URL = "https://github.com"


def _git_hit(username, tab_name, css_class, ccc):
    page = requests.get(f'{GIT_BASE_URL}/{username}?tab={tab_name}')
    soup = BeautifulSoup(page.text, 'html.parser')

    for link in soup.find_all('a', {'class', css_class}):
        if len(link.get('class')) == ccc:
            url = GIT_BASE_URL + link.get('href')
            print(url)


def git_forked_repos(username):
    print('git forked repositories for user - ' + username)
    _git_hit(username, 'repositories', 'muted-link', 1)


def git_following(username):
    print(f'git user = {username} is following below people')
    _git_hit(username, 'following', 'd-inline-block no-underline mb-1', 3)


username = input("Please enter the username: ")
git_forked_repos(username)
git_following(username)
