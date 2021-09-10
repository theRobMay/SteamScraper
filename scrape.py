import requests
from bs4 import BeautifulSoup

from game import Game


class SteamScraper:
    def __init__(self, steam_search_url):
        self.steam_search_url = steam_search_url

    def get_games(self):
        page = requests.get(self.steam_search_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        search_results = soup.find(id='search_resultsRows')
        game_rows = search_results.find_all('a', class_='search_result_row')

        games = []
        for game_row in game_rows:
            title = game_row.find('span', class_='title').text.strip()

            release_date = game_row.find('div', class_='search_released').text.strip()

            price_div = game_row.find('div', class_='search_price')
            if any(price_div.find_all('span')):
                price_div.find('span').decompose()
            price = price_div.text.strip()

            game = Game(title, release_date, price)
            games.append(game)
        return games
