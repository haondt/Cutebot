# downloads an image from queue.txt to /temp/nextimage.jpg
# tweets the image, then deletes it
# to be run once every 15 minutes or so?
import tweepy, time, sys, urllib.request, os

captions = [
    "#cute",
    "OMG, soc cute 😍😍😍",
    "so #adorable!!",
    "awwwww",
    "👅",
    "❤❤❤",
    "Need this in my life ❤❤",
    ""
]
# choose a caption
caption = captions[random.randint(0,7)]

queue_file = open("cutebot/queue.txt", "r")
queue_list = []
for line in queue_file:
    line = line.strip()
    if len(line) > 1:
        queue_list.append(line.strip())

queue_file.close()
if len(queue_list) > 0:
    image_link = queue_list[0]
    queue_list = queue_list[1:]

    queue_file = open("cutebot/queue.txt", "w")
    for line in queue_list:

        queue_file.write("\n")
        queue_file.write(line)

    # download the image
    if image_link.split("/")[2] == "imgur.com":
        image_link_list = image_link.split("/")
        image_link = image_link_list[0] + "//i.imgur.com/" + image_link_list[3] + ".jpg"
    urllib.request.urlretrieve(image_link, "cutebot/temp/nextimage.jpg")


    # enter the corresponding information from your Twitter application:
    CONSUMER_KEY = 'YOUR_CONSUMER_KEY'  # keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'  # keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = 'YOUR_ACCESS_KEY'  # keep the quotes, replace this with your access token
    ACCESS_SECRET = 'YOUR_ACCESS_SECRET'  # keep the quotes, replace this with your access token secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    # tweet the image
    try:
        api.update_with_media("cutebot/temp/nextimage.jpg", status=caption)
        # delete the image
        os.remove("cutebot/temp/nextimage.jpg")
    except Exception:
        print("Failed to tweet:", end=" ")
        print(image_link)

else:
    print("The queue is empty")


