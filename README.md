# Instagram Automation Script using `instagrapi`

The code performs several actions using the Instagram API (via the `instagraapi` Python library) for interacting with posts under a specific hashtag, in this case, "programming." Here's a breakdown of what's happening:

## 1. **Login**
- The script reads Instagram login credentials from a file called `credentials.txt` and uses them to log into an Instagram account via the `Client.login()` method from the `instagrapi` library.

## 2. **Search  for Hashtag Posts**
- After logging in, the script searches for recent posts under the hashtag "programming" using the `Client.hashtag_medias_recent()` method, which retrives up to 20 recent media posts tagged with that hashtag.

## 3. **Like Posts**
- The script iterates over the retrived media posts, and for each post, it calls the `Client.media_like(media.id)` function, which likes the post.

## 4. **Follow User**
- Every 5th post (`if i%5==0`), the script also follows the user who posted the media. This is done by calling `Client.user_follow(media.user.pk)`.

## 5. **Comment on Post**
- Along with following the user, every 5th post also gets a comment. A predefined comment, "Awesome post", is posted under the media, followed by a random comment selected from the `comments` list. The comments include: "Awesome," "Great," and "Nice."

## 6. **Output Messages**
- Throughout the process, messages are printed to the console to inform the user of the actions being taken, such as "Liked post number X," "Followed user," and "Commented X under post number Y."

## Key Actions Happening:
- **Liking** Instagram Posts.
- **Following** the users who posted the media, selectively.
- **Commenting** on every 5th post.
- **Randomly selecting a comment** from a list to post under the selected media.

This automation script designed for engagement, increasing interactions on Instagram posts tagged with a specific hashtag. However, ensure that you follow Instagram's guidelines, as automated actions like this can sometimes lead to account restrictions if overused or detected as spammy behaviour.
