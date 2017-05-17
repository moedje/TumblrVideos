import pytumblr
from .pytumblr import TumblrRestClient

TUMBLRAPI = {'site': 'http://www.tumblr.com', 'request_token_url': "/oauth/request_token",
             'authorize_url': "/oauth/authorize", 'token_url': "/oauth/access_token",
             'callback_url': 'https://127.0.0.1/callback'}

TUMBLRAUTH = {'consumer_key': '5wEwFCF0rbiHXYZQQeQnNetuwZMmIyrUxIePLqUMcZlheVXwc4',
          'consumer_secret': 'GCLMI2LnMZqO2b5QheRvUSYY51Ujk7nWG2sYroqozW06x4hWch',
          'oauth_token': '',
          'oauth_secret': ''}

# tclient = TumblrRestClient(**TUMBLRAUTH)
