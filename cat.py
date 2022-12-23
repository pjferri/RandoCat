import random
import webbrowser

cat_gifs = ["https://giphy.com/clips/bestfriends-cat-cats-kitty-IsDjNQPc4weWPEwhWm",
            "https://giphy.com/gifs/cat-moment-remember-8vQSQ3cNXuDGo",
            "https://giphy.com/gifs/cat-kisses-hugs-MDJ9IbxxvDUQM",
            "https://giphy.com/gifs/reaction-mood-Lq0h93752f6J9tijrh",
            "https://giphy.com/gifs/v6aOjy0Qo1fIA",
            "https://giphy.com/gifs/cat-funny-lol-CqVNwrLt9KEDK"]


def play():
    random_gif = random.choice(cat_gifs)
    webbrowser.open_new(random_gif)

play()