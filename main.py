import random
from instagrapi import Client

with open("credentials.txt", "r") as f:
    username, password = f.read().splitlines()
Client = Client()
Client.login(username, password)

hashtag = "programming"
comments = ["Awesome", "Great", "Nice"]
medias = Client.hashtag_medias_recent(hashtag, 20)

for i, media in enumerate(medias):
    Client.media_like(media.id)
    print(f"Liked post numer {i+1} of hashtag {hashtag}")
    if i % 5 == 0:
        Client.user_follow(media.user.pk)
        print(f"Followed user {media.user.username}")
        Client.media_comment(media.id, "Awesome posr")
        comment = random.choice(comments)
        print(f"Commented {comment} under post number {i+1}")