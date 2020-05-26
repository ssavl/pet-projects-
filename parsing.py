import requests as req
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from pprint import pprint


listlist = []
url = req.get('https://corner-stats.com/')
html = bs(url.content, 'html.parser')

def auth():
    s = req.Session()
    auth_html = s.get("https://corner-stats.com/index.php?route=account/logout")
    auth_BS = bs(auth_html.content, 'html.parser')

    # go login

    payload = {
        "email_login" : "get-moscow@yande.ru",
        "password_login" : "savelii13",
        "check" : 1
    }

    answ = s.post('https://corner-stats.com/index.php?route=account/logout', data=payload)
    answ_BS = bs(answ.content, 'html.parser')



def some_func():
    for items in html.select('.select-control_1'):   # нужно ввести class селектора
        title = items.select('option')
        for league in title:
            get_league = league.select('.Argentina')
            for team in get_league:
                get_team = team.select('.Primera División')
                for team_id in get_team:
                    get_team_id = team_id.select('.CA Sarmiento')
                    print(get_team_id)

def get_selenium():
    chromedriver = '/usr/local/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)


auth()
some_func()
pprint(listlist)
