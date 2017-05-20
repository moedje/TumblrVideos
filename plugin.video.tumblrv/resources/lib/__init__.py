import urllib, urllib2, time, random, hmac, base64, hashlib
from pytumblr import TumblrRestClient

TUMBLRAPI = {'site': 'http://www.tumblr.com', 'request_token_url': "http://www.tumblr.com/oauth/request_token",
             'authorize_url': "http://www.tumblr.com/oauth/authorize", 'token_url': "http://www.tumblr.com/oauth/access_token",
             'callback_url': 'https://127.0.0.1/callback'}

TUMBLRAUTH = {'consumer_key': '5wEwFCF0rbiHXYZQQeQnNetuwZMmIyrUxIePLqUMcZlheVXwc4',
          'consumer_secret': 'GCLMI2LnMZqO2b5QheRvUSYY51Ujk7nWG2sYroqozW06x4hWch',
          'oauth_token': '',
          'oauth_secret': ''}

def makenonce():
    random_number = ''.join( str( random.randint( 0, 9 ) ) for _ in range( 40 ) )
    m = hashlib.md5( str( time.time() ) + str( random_number ) )
    return m.hexdigest()

def encodeparams(s):
    return urllib.quote( str( s ), safe='~' )

def getoauth(consumer_key = "5wEwFCF0rbiHXYZQQeQnNetuwZMmIyrUxIePLqUMcZlheVXwc4", consumer_secret = "GCLMI2LnMZqO2b5QheRvUSYY51Ujk7nWG2sYroqozW06x4hWch"): # oauth_consumer_secret
    request_tokenURL = 'http://www.tumblr.com/oauth/request_token'
    oauth_parameters = {
                'oauth_consumer_key'     : consumer_key,
                'oauth_nonce'            : makenonce(),
                'oauth_timestamp'        : str(int(time.time())),
                'oauth_signature_method' : "HMAC-SHA1",
                'oauth_version'          : "1.0"
                }
    normalized_parameters = encodeparams( '&'.join( ['%s=%s' % ( encodeparams( str( k ) ), encodeparams( str( oauth_parameters[k] ) ) ) for k in sorted( oauth_parameters )] ) )
    normalized_http_method = 'GET'
    normalized_http_url = encodeparams( request_tokenURL )
    signature_base_string = '&'.join( [normalized_http_method, normalized_http_url, normalized_parameters] )
    oauth_key = consumer_secret + '&'
    hashed = hmac.new( oauth_key, signature_base_string, hashlib.sha1 )
    oauth_parameters['oauth_signature'] = base64.b64encode( hashed.digest() )
    oauth_header = 'OAuth realm="http://www.tumblr.com",' + 'oauth_nonce="' + oauth_parameters['oauth_nonce'] + '",' + 'oauth_timestamp="' + oauth_parameters['oauth_timestamp'] + '",' + 'oauth_consumer_key="' + oauth_parameters['oauth_consumer_key'] + '",' + 'oauth_signature_method="HMAC-SHA1",oauth_version="1.0",oauth_signature="' + oauth_parameters['oauth_signature'] +'"'

    req = urllib2.Request( request_tokenURL )
    req.add_header( 'Authorization', oauth_header )
    tokenstr = urllib2.urlopen( req ).read()
    tokens = {}
    for token in tokenstr.split('&'):
        tname, tval = urllib.splitvalue(token)
        tokens.update({tname: tval})
    TUMBLRAUTH.update({'oauth_token': tokens.get('oauth_token', ''), 'oauth_secret': tokens.get('oauth_token_secret', '')})
    return TUMBLRAUTH

# tclient = TumblrRestClient(**TUMBLRAUTH)
