redditfetcher.py grabs the top (over x=800 karma) posts from the subreddits listed in subreddits.txt. Change the list of subs for different content.
redditfetcher.py keeps a log of fetched images in log.txt and sends new ones to queue.txt.
tweetbot.py grabs the newest image from queue.txt, saves it in temp/nextimage.jpg, tweets it with a caption from its captions list and deletes the temporary file. 
redditfetcher should be run once every hour and tweetbot should be run once every 15 minutes.
Feel free to change the subs in the list of subs.
Currently running @cuteanimalsb on twitter
