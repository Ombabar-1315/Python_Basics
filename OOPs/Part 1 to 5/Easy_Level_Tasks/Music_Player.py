class MusicPlayer:

    def __init__(self,song,artist,volume):
        self.song = song
        self.artist = artist
        self.volume = volume

    def play_song(self):
        print("Song Is Playing..... of",self.song)

    def increase_volume(self,amount):
        self.volume += amount 

    def decrease_volume(self,amount):
            self.volume -= amount   

    def show_status(self):
         print("Song Playing: ",self.song)
         print("Artist: ",self.artist)
         print("Volume: ",self.volume)


print("=========================")
s1 = MusicPlayer("Ve Mahi","Arjit Singh",30)
s1.show_status()
print("-----------------------")
s2 = MusicPlayer("Sanjana","Rock",50)
s2.show_status()
print("--------------------------")

s1.increase_volume(40)
s1.play_song()
s1.show_status()
       