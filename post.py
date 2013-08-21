#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
from photo2tumblr import TumblrAPIv2, APIError
import time
import os
import sys
import configparser

# Keys in http://www.tumblr.com/oauth/apps
config = configparser.Configparser()
config.read('config.ini')

print "Taking screenshot ..."
display = Display(visible=0, size=(config['SCREEN']['WIDTH'], config['SCREEN']['HEIGHT']))
display.start()

browser = webdriver.Firefox()
browser.get(sys.argv[1])
browser.save_screenshot('screenie.png')
browser.quit()

display.stop()

print "Done!"
print "Now posting to %s ..." % config['DEFAULT']['BLOG']

api = TumblrAPIv2(  config['DEFAULT']['CONSUMER_KEY'], \
                    config['DEFAULT']['CONSUMER_SECRET'], \
                    config['DEFAULT']['OAUTH_TOKEN'], \
                    config['DEFAULT']['OAUTH_TOKEN_SECRET'] )

date  = time.gmtime(os.path.getmtime('./screenie.png'))
post = {
    'type' : 'photo',
    'date' : time.strftime ("%Y-%m-%d %H:%M:%S", date),
    'data' : './screenie.png',
    'tags' : time.strftime ("%Y", date) + ", photo",
    'caption' : time.strftime ("%B %d / %Y", date)
}

try:
    response = api.createPhotoPost( config['DEFAULT']['BLOG'], post)
    if 'id' in response:
        print response['id']
        os.remove('./screenie.png')
    else:
        print response
except APIError:
    print "Error Uploading file!"

print "Done! "
