#!flask/bin/python
from website import srctweb

if __name__ == '__main__':	## This is for debugging use only.
    srctweb.run(debug=True, host="0.0.0.0")

## This is for execution via gunicorn.
# gunicorn command
# gunicorn srctweb:srctweb -b 127.0.0.1:8001
