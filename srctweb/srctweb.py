#!flask/bin/python
from website import website

if __name__ == '__main__':	## This is for debugging use only.
    website.run(debug=True)

## This is for execution via gunicorn.
# gunicorn command
# gunicorn srctweb:website -b 127.0.0.1:8001
