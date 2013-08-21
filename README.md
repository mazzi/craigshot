# CraigShot #

Small python script to take a screenshot of a webpage and post it to tumblr.

## Usage ##

```
./post.py <<url>>
```

No validation of url at the moment!
The size of the screenshot is 800x600 (nasty hardcode).
The script creates a file called `screenie.png` that is being deleted once uploaded.

## Configuration ##

You need to create the file `config\_craigshot.py` with the following variables

```
BLOG='yourblog.tumblr.com'
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
```
Where:
- `CONSUMER` values can be filled in using http://www.tumblr.com/oauth/apps
- `OAUTH` values can be filled in using https://gist.github.com/velocityzen/1242662

