#!flask/bin/python
import sys
from website import website
from website import freezer

if __name__ == '__main__':	## This is for debugging use only.
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    website.run(debug=True)

## This is for execution via gunicorn.
# gunicorn command
# gunicorn srctweb:website -b 127.0.0.1:8001
