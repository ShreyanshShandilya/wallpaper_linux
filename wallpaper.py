import os 
import praw
import wget

try:
    reddit = praw.Reddit(client_id = "your_client_id_here",client_secret = "your_secret_key_here" , user_agent = "Ninebit")
    subreddit = reddit.subreddit("wallpaper")
    for post in subreddit.hot(limit = 1):
        filename = wget.download(post.url)
        uri = "file:///"+str(os.path.abspath(filename))
        query = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+uri
        os.system(query)
except:
    print("Exception")    
