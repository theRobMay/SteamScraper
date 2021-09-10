from prettytable import PrettyTable

import scrape

URL = 'https://store.steampowered.com/search/?filter=topsellers'

if __name__ == '__main__':
    scraper = scrape.SteamScraper(URL)
    games = scraper.get_games()

    games_table = PrettyTable()
    games_table.field_names = ['Name', 'Release Date', 'Price', 'Description']
    for game in games:
        games_table.add_row([game.name, game.releaseDate, game.price, game.description])

    print(games_table)
