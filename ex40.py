class Song(object):

    def __init__(self, lyrics, words):
        self.lyrics = lyrics
        self.words = words


    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def print_words(self):
        for n in range(1,len(self.lyrics)):
            print n

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"],15)

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"],10)



take_me_to_your_heart = Song(["Handing from the rain and snow",
                        "Trying to forget but I won't let go",
                        "Looking at a crowded street",
                        "Listening to my own heart beat",
                        "so many people all around world.",
                        "Tell me where do I find someone like you girl"],41)


str = ["Handing from the rain and snow",
                        "Trying to forget but I won't let go",
                        "Looking at a crowded street",
                        "Listening to my own heart beat",
                        "so many people all around world.",
                        "Tell me where do I find someone like you girl"]
take2 = Song(str,41)

take2.print_words()

take2.sing_me_a_song()

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print '-' * 10
take_me_to_your_heart.sing_me_a_song()
print '-' * 10
