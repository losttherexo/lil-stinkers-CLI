class Artist:
    
    all = []

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        Artist.all.append(self)