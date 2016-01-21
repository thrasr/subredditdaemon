# subredditdaemon
A bot that will post images to a subreddit (or set of subreddits).

* Checks for any new reddit messages!
* Looks at all subreddit directories
* Picks a random file in the subreddit's directory
* Uploads that file to imgur and gets the url
* Posts that url to the given subreddit, using the filename as the post title
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
|-|-|posttitle1
|-|-|posttitle2
|-|posted_images
|-|-|oldimage
```

Requires praw and imgurpython

```
pip install praw
pip install imgurpython
```


Your creds.py file should not be shared or posted to any public place.  It should be placed in the same directory as subredditdaemon.py and it should look like the following.  Reddit and imgur client information can be obtained from the developer/API areas of those sites.
```
# praw user-agent
user-agent = ("python:subredditdaemon:0.1 (by /u/YOUR USERNAME)"
             ("github.com/thrasr/subredditdaemon")

# reddit client identification
reddit_client_id = "YOUR REDDIT CLIENT ID"
reddit_client_secret = "YOUR REDDIT CLIENT SECRET"
redirect_uri = 'http://127.0.0.1:65010/authorize_callback'

#access token = 'YOUR REDDIT ACCESS TOKEN'
refresh_token = 'YOUR REDDIT REFRESH TOKEN'

# imgur client identification
client_id = 'YOUR IMGUR CLIENT ID'
client_secret = 'YOUR IMGUR CLIENT SECRET'

```
