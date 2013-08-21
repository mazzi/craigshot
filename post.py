#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
from photo2tumblr import TumblrAPIv2, APIError
import time
import os
import sys
import config_craigshot

# keys in your config_craigshot.py file @TODO write a conf.ini file.
#BLOG=''
#CONSUMER_KEY = ''
#CONSUMER_SECRET = ''
#OAUTH_TOKEN = ''
#OAUTH_TOKEN_SECRET = ''
# Keys in http://www.tumblr.com/oauth/apps

print "Taking screenshot ..."
display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
browser.get(sys.argv[1])
browser.save_screenshot('screenie.png')
browser.quit()

display.stop()

print "Done!"
print "Now posting to craigshot.tumblr.com ..."

api = TumblrAPIv2(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

date  = time.gmtime(os.path.getmtime('./screenie.png'))
post = {
    'type' : 'photo',
    'date' : time.strftime ("%Y-%m-%d %H:%M:%S", date),
    'data' : './screenie.png',
    'tags' : time.strftime ("%Y", date) + ", photo",
    'caption' : time.strftime ("%B %d / %Y", date)
}

try:
    response = api.createPhotoPost(BLOG,post)
    if 'id' in response:
        print response['id']
        os.remove('./screenie.png')
    else:
        print response
except APIError:
    print "Error Uploading file!"

print "Done! "
