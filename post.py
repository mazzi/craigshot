#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
from photo2tumblr import TumblrAPIv2, APIError
import time
import os
import sys
import configparser


def screenshot( url, config ):
    display = Display( visible=0, size=( config['SCREEN']['WIDTH'], config['SCREEN']['HEIGHT'] ) )
    display.start()

    browser = webdriver.Firefox()
    browser.get( url )
    browser.save_screenshot( 'screenie.png' )
    browser.quit()

    display.stop()

def post ( config ):

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
        else:
            print response
    except APIError:
        print "Error Uploading file!"
    finally:
        os.remove('./screenie.png')

def main( url ):
    # Keys in http://www.tumblr.com/oauth/apps
    config = configparser.ConfigParser()
    config.read( 'config.ini' )

    print "Taking screenshot ..."

    screenshot ( url, config  )
    
    print "Done!"
    print "Now posting to %s ..." % config['DEFAULT']['BLOG']

    post ( config )

    print "Done! "


if __name__ == "__main__":
    if len (sys.argv) > 1 :
        main( sys.argv[1] )
    else:
        print "Usage: post.py <<url_to_fetch>>\n"