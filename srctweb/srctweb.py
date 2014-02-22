#!flask/bin/python
from website import website
#website.run(debug = True) ## This is for debugging use only.

if __name__ == 'main':	## This is for execution via gunicorn.
    website.run(debug=True)
