from flask import Flask
from flask_frozen import Freezer

from flask.ext.gravatar import Gravatar

website = Flask(__name__)
freezer = Freezer(website)

from website import views

# initialize gravatar defaults
gravatar = Gravatar(website,
                    size = 80,
                    rating='g',
                    default='mm',
                    force_default=False,
                    use_ssl=False,
                    base_url=None)
