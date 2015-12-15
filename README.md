# subredditdaemon
A bot that will post images and albums to a subreddit (or set of subreddits).


* Periodically post images from a file
* Automatically upload images/albums to imgur
* Checks images for reposts before posting


```
|subredditname
|-|topost
|-|-|posttitle.png
|-|-|posttitle.jpg
|-|-|albumtitle
|-|-|-|image1.png
|-|-|-|image2.png
|-|posted
```

Requires praw and imgurpython
