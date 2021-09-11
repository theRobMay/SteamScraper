class Game:
    def __init__(self, store_page_url, name, release_date, price):
        self.storePageUrl = store_page_url
        self.name = name
        self.releaseDate = release_date
        self.price = price

        self.description = None
