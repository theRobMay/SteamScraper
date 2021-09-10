import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


class Game:
    def __init__(self, name, release_date, price):
        self.name = name
        self.releaseDate = release_date
        self.price = price


def get_games(steam_search_url):
    page = requests.get(steam_search_url)
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


if __name__ == '__main__':
    url = 'https://store.steampowered.com/search/?filter=topsellers'
    games = get_games(url)

    games_table = PrettyTable()
    games_table.field_names = ['Name', 'Release Date', 'Price']
    for game in games:
        games_table.add_row([game.name, game.releaseDate, game.price])

    print(games_table)
