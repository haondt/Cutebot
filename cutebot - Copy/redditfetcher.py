# Browses all the listed subs for the top image posts
# Images that were posted between 22 and 24 hours ago with over x upvotes are added to the post queue
# DO NOT DELETE log.txt
# run this code once every hour
import datetime
import praw
def main():
    # how many upvotes each post should have (at least)
    upvote_threshold = 800

    # Subs to get pictures from
    subreddits = []
    subreddits_file = open("cutebot/subreddits.txt", "r")
    for line in subreddits_file:
        if len(line) >= 1:
            subreddits.append(line.strip())

    old_posts = []
    new_posts = []

    post_log = open("cutebot/log.txt", "r")
    for line in post_log:
        old_posts.append(line.strip())
    post_log.close()

    subreddit = ''
    for sub in subreddits:
        subreddit+= sub
        subreddit += "+"

    subreddit = subreddit[:len(subreddit)-1]

    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret="eYOUR_CLIENT_SECRET",
                     user_agent='Catbot 0.1')

    subreddit = reddit.subreddit(subreddit)

    # browse top posts from the last 24 hours
    for submission in subreddit.top(time_filter='day'):
        # parse the url and the age of the post in integer hours
        url = submission.url
        submissiontime = datetime.datetime.fromtimestamp(submission.created_utc)
        age = datetime.datetime.now() - submissiontime
        age = int(str(age).split(":")[0])

        # if the post is an image, has over 1k points and is 22-24 hours old,
        # check to see if its in the log, if not, add it to the to be posted log.
        if is_image(url) and submission.score > upvote_threshold and age >= 22:
            posted = False
            for post in old_posts:
                if post == url:
                    posted = True
                    break
            if not posted:
                old_posts.append(url)
                new_posts.append(url)

    # write the new posts to the log and queue
    post_log = open("cutebot/log.txt", "a")
    post_queue = open("cutebot/queue.txt", "a")
    for post in new_posts:
        post_queue.write(post)
        post_queue.write("\n")
        post_log.write(post)
        post_log.write("\n")
    post_log.close()


def is_image(url):
    image_suffixes = [
        ".jpg",
        ".png"
    ]
    image_prefixes = [
        "i.imgur",
        "i.redd.it",
        "imgur.com"
    ]
    image_suffixes = "\t".join(image_suffixes)
    image_prefixes = "\t".join(image_prefixes)

    return url[len(url) - 4:] in image_suffixes or url.split("/")[2] in image_prefixes

main()