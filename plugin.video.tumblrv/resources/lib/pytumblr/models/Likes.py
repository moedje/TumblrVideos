from Post import Post, Posts
from Blog import *

class Likes(Posts):

    def __init__(self, d):
        #self._posts = None
        self.liked_count = 0
        if isinstance(d, list):
            super(Likes, self).__init__(d)
        elif isinstance(d, dict):
            super(Likes, self).__init__(d.get('liked_posts', []))
        else:
            super(Likes, self).__init__([])

    def get(self, key, default=None):
        if key in self:
            return getattr(self, key, default)
        else:
            return default
