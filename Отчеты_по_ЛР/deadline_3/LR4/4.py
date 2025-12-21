class song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
        print(f"песня {song.title} добавлена в плейлист {self.name}")
    
    def show_songs(self):
        print(f"плейлист {self.name}:")
        for song in self.songs:
            print(f"  {song.title} ({song.duration} сек)")

pesnia1 = song("песня1", 180)
pesnia2 = song("песня2", 2000)
moy_pleilist = playlist("любимые")
moy_pleilist.add_song(pesnia1)
moy_pleilist.add_song(pesnia2)
moy_pleilist.show_songs()