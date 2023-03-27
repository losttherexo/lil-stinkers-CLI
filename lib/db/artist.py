class Artist:
    
    all_artists = []

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        Artist.all_artists.append(self)