import requests
from bs4 import BeautifulSoup

from game import Game


class SteamScraper:
    def __init__(self, steam_search_url):
        self.steam_search_url = steam_search_url

    @staticmethod
    def _get_game_details(game_url):
        page = requests.get(game_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        glance = soup.find('div', class_='glance_ctn')

        if glance is not None:
            description = glance.find('div', class_='game_description_snippet')
            description = description.text.strip() if description is not None else ''
        else:
            description = ''
        return description

    def get_games(self, top_recs=10):
        page = requests.get(self.steam_search_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        search_results = soup.find(id='search_resultsRows')
        game_rows = search_results.find_all('a', class_='search_result_row')

        games = []
        loop_counter = 0
        for game_row in game_rows:
            if loop_counter >= top_recs:
                break
            loop_counter += 1

            title = game_row.find('span', class_='title').text.strip()

            release_date = game_row.find('div', class_='search_released').text.strip()

            price_div = game_row.find('div', class_='search_price')
            if any(price_div.find_all('span')):
                price_div.find('span').decompose()
            price = price_div.text.strip()

            game = Game(title, release_date, price)

            game_url = game_row.get('href')
            description = self._get_game_details(game_url)
            game.description = description

            games.append(game)
        return games
