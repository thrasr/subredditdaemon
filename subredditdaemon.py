import praw
import imgurpython
import time
import creds
import os, os.path
import random


# FUTURE FEATURE
# def get_new_submissions
# grab any submissions from the past 24h?
# possibly filter by username to avoid grabbing ones WE post
# download pictures into the posted_images/ directory to help avoid reposts

# FUTURE FEATURE
# def check_repost
# Compares an image against the images in posted
# Easiest is a direct comparison (hash images and check for dups)
# Harder is to do a resize, grayscale, pixel comparison, but will find resized and watermarked images
# probably checks if image about to be posted has been posted before

# upload image to imgur
def imgur_upload(client, subreddit, filename):
    config = {
        'name':  filename,
        'description': 'Automatically uploaded.  Please message /u/??? them for any concerns.',
        'nsfw': False
    }

    print("Uploading image... ")
    response = client.upload_from_path(filename, config=config, anon=True)
    print("Done.  Image is uploaded at", response['link'])

    return response['link']


# FUTURE
# def imgur_album_upload
# if filename is a directory, call this function instead to upload the album
# upload all files in a folder to imgur

# Use praw to post the image
def post_to_subreddit(reddit, subredditname, filename, image_url):
    try:
        post_url = reddit.submit(subreddit=subredditname, title=filename, url=image_url)
        return post_url, True
    except:
        return '', False

# Do we have any unread messages?
def orangered(reddit):
    return sum(1 for _ in reddit.get_unread(limit=1))>0

# Move posted image into correct folder
def move_file(filename):
    os.rename(filename, "../posted_images/" + filename)

# Go to a subreddit, pick a random picture, upload it, post it, and move it
def post(imgur, reddit, subreddit):
    try:
        os.chdir(subreddit + "/images_to_post")
    except:
        print("Unable to find directory:", subreddit + "/images_to_post")
        return False

    # Pick and upload image
    print("Running script for subreddit", subreddit)
    files = os.listdir('.')
    if not files:
        return False
    filename = random.choice(files)
    print("File being uploaded is", filename)
    image_url = imgur_upload(imgur, subreddit, filename)

    # Post to subreddit
    print("Submitting...")
    post_url, success = post_to_subreddit(reddit, subreddit, filename, image_url)
    if not success:
        print("ERROR: image was not submitted properly")
        return False

    print("Image submitted successfully at:", post_url)

    # Move image
    print("Moving image...")
    move_file(filename)

    # Move back to original folder
    os.chdir("../..")
    print("Done with", subreddit + "!")
    return True

if __name__ == "__main__":

    #setup necessary clients
    imgur = imgurpython.ImgurClient( creds.imgur_client_id, creds.imgur_client_secret )
    reddit = praw.Reddit( creds.useragent )
    reddit.set_oauth_app_info( client_id=creds.reddit_client_id,
                               client_secret=creds.reddit_client_secret,
                               redirect_uri=creds.redirect_uri )
    reddit.refresh_access_information(creds.refresh_token)

    # Check for new messages
    if orangered(reddit):
        print("\033[0;33mNew message(s)!\033[0m")

    # iterate through all subreddit folders
    for file in os.listdir('.'):
        # subreddits and their directories cannot start with '.' or '_'
        if file[0] == '.' or file[0] == '_' or not os.path.isdir(file):
            continue
        if not post(imgur, reddit, file):
            print("Was unable to post for subreddit", file)

# perhaps run this as a cron job? (aka systemd)
# and filter based on day of the week?
# run everyday at 1700 - fri/sat/sun/mon/wed

# while true?  something constantly running
# check time every ~hour?
# if a certain hour (0300) - check new submissions
# if a certain hour (1600?) - check for reposts and post new image
  # loop through subreddit folders to get subreddit name to check stuff
  # this will eventually be looking at a folder (or folders)
  #subreddit = r.get_subreddit('SUBREDDIT')
  #sleep(60*60)
