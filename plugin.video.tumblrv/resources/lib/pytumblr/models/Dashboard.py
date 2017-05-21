from Post import *
from Blog import *

class Dashboard(Posts):

    def __init__(self, d, **kwargs):
        """
        : attribute meta : Meta
        : attribute response : Response
        """
        super(Dashboard, self).__init__(d)
        self._posts = Posts(d)
        self.response = None
        self.id = None


    @property
    def posts(self):
        """
        Returns list of model.Post.Post
        :param value: 
        :return: array Post 
        """
        return self._posts

    @posts.setter
    def posts(self, value):
        self._posts = Posts(value)

    def get(self, key, default={}):
        if key in self:
            return getattr(self, key, default)
        else:
            return {}