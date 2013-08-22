# CraigShot #

Small python script to take a screenshot of a webpage and post it to tumblr.

## Usage ##

```
./post.py <<url>>
```

No validation of url at the moment!
The script creates a file called `screenie.png` that is being deleted once uploaded.

## Configuration ##

You need to create the file `config.ini` (a copy of config_sample.ini)

Where:
- `CONSUMER` values can be filled in using http://www.tumblr.com/oauth/apps
- `OAUTH` values can be filled in using https://gist.github.com/velocityzen/1242662

Don't use quotes for the values.

## Requeriments ##

Several...

```
sudo apt-get install python-pip xvfb xserver-xephyr
sudo pip install selenium
```

Any other dependency can be installed using `sudo pip install <<package>>`
