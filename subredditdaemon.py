import praw
import imgurpython
import time
import creds
import os, os.path
import random

r = praw.Reddit(user-agent=creds.user-agent)
r.login()

# FUTURE FEATURE
# def get_new_submissions
# grab any submissions from the past 24h?
# possibly filter by username to avoid grabbing ones WE post
# download pictures into the posted_images/ directory to help avoid reposts

# FUTURE FEATURE
# def check_repost
# Compares an image against the images in posted
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

    #print(response) #debug

    return response['link']


# FUTURE
# def imgur_album_upload
# if filename is a directory, call this function instead to upload the album
# upload all files in a folder to imgur


#def moveFile(filename)
# moves file to posted_images/
# called when already in subreddit folder, so relative path should be easy

# Go to a subreddit, pick a random picture, upload it, post it, and move it
def post(subreddit)
    os.chdir(subreddit)

    # Pick and upload image
    print("Running script for subreddit", subreddit)
    filename = random.choice(os.listdir('.'))
    print("File being uploaded is", filename)
    url = imgur_upload(client, subreddit, filename)

    # Post to subreddit

    # Move image


if __name__ == "__main__":

    client = imgurpython.ImgurClient(creds.client_id, creds.client_secret)

    # iterate through all subreddit folders
    for file in os.listdir('.'):
        # subreddit directories cannot start with '.' or '_'
        if file[0] == '.' or file[0] == '_' or not os.path.isdir(file):
            continue
        post(file)


# perhaps run this as a cron job? (aka systemd)
# and filter based on day of the week?

# while true?  something constantly running
# check time every ~hour?
# if a certain hour (0300) - check new submissions
# if a certain hour (1600?) - check for reposts and post new image
  # loop through subreddit folders to get subreddit name to check stuff
  # this will eventually be looking at a folder (or folders)
  #subreddit = r.get_subreddit('SUBREDDIT')
  #sleep(60*60)
