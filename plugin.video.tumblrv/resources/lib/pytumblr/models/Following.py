from Post import Post, Posts
from Blog import Blogs, Blog

class Following(list):

    def __init__(self, d):
        super(Following, self).__init__(d)
        if isinstance(d, list):
            self.__dict__ = {"blogs": d}
            self.extend(d)
        elif isinstance(d, dict):
            self.__dict__ = d
            self.extend(d.get('blogs', []))

    def __getitem__(self, item):
        blog = super(list, self).__getitem__(item) #super(Following, self).__getitem__(item)
        assert isinstance(blog, Blog)
        return blog

    def __setitem__(self, index, value):
        #blog = super(Following, self).__getitem__(value)
        assert isinstance(value, Blog)
        super(list, self).__setitem__(index, Blog(value))

    def get(self, key, default=None):
        if key in self:
            return getattr(self, key, default)
        else:
            return default