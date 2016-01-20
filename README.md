# subredditdaemon
A bot that will post images to a subreddit (or set of subreddits).


* Picks a random file in the subreddit's directory
* Uploads that file to imgur and gets the url
* Posts that url to the given subreddit
* Moves file to folder of previously posted images

Possible future features:
* Check for certain time parameters when run (to avoid running on weekends for example)
* Periodically post images from a file based on certain parameters (basically replace the need for cron...but always running)
* Automatically upload albums to imgur
* Compares pictures against previously posted pictures to avoid reposts
* Downloads all images posted to the subreddit to help avoid reposts (filter by bot name to avoid duplicates)


```
|subredditname
|-|images_to_post
|-|-|posttitle1.png
|-|-|posttitle2.jpg
|-|posted_images
|-|-|oldimage.jpg
```

Requires praw and imgurpython

```
pip install praw
pip install imgurpython
```


Your creds.py file should not be shared or posted to any public place.  It should be placed in the same directory as subredditdaemon.py and it should look like this:
```
# praw user-agent
user-agent = ("python:subredditdaemon:0.1 (by /u/YOUR USERNAME)"
             ("github.com/thrasr/subredditdaemon")

# imgur client idenficiation
client_id = 'YOUR CLIENT ID'
client_secret = 'YOUR CLIENT SECRET'

```
