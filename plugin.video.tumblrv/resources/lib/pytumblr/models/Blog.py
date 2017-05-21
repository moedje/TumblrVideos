from Post import Post, Posts

class Theme(dict):
    def __init__(self, **kwargs):
        """
        : attribute title_font_weight : string
        : attribute header_image_scaled : string
        : attribute header_focus_width : float
        : attribute header_bounds : string
        : attribute show_description : bool
        : attribute avatar_shape : string
        : attribute show_avatar : bool
        : attribute show_title : bool
        : attribute header_full_height : float
        : attribute header_stretch : bool
        : attribute background_color : string
        : attribute link_color : string
        : attribute header_focus_height : float
        : attribute title_color : string
        : attribute header_image : string
        : attribute body_font : string
        : attribute show_header_image : bool
        : attribute title_font : string
        : attribute header_full_width : float
        : attribute header_image_focused : string
        """
        super(Theme, self).__init__(**kwargs)
        self.title_font_weight = None
        self.header_image_scaled = None
        self.header_focus_width = None
        self.header_bounds = None
        self.show_description = None
        self.avatar_shape = None
        self.show_avatar = None
        self.show_title = None
        self.header_full_height = None
        self.header_stretch = None
        self.background_color = None
        self.link_color = None
        self.header_focus_height = None
        self.title_color = None
        self.header_image = None
        self.body_font = None
        self.show_header_image = None
        self.title_font = None
        self.header_full_width = None
        self.header_image_focused = None

    def __getattr__(self, name):
        """        
        :param item: 
        :return: Blog
        :rtype: Blog 
        """
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such item: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Trail(dict):

    def __init__(self, **kwargs):
        """
        : attribute post : Post
        : attribute content_raw : string
        : attribute content : string
        : attribute blog : Blog
        : attribute is_current_item : bool
        """
        super(Trail, self).__init__(**kwargs)
        self.post = Post(**kwargs.get('post', {}))
        self.blog = Blog(**kwargs.get('blog', {}))
        self.content_raw = None
        self.content = None
        self.is_current_item = None
        self.is_root_item = None


class Blog(dict):

    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, **value):
        self._theme = Theme(**value)

    def __init__(self, **kwargs):
        """
        : attribute share_likes : bool
        : attribute active : bool
        : attribute share_following : bool
        : attribute name : string
        : attribute theme : Theme
        : attribute can_be_followed : bool
        """
        super(Blog, self).__init__(**kwargs)
        self.__dict__ = kwargs
        self._theme = Theme(**kwargs.get('theme', {}))
        self.posts = Posts(kwargs.get('posts', []))
        self.active = None
        self.ask = None
        self.ask_anon = None
        self.ask_page_title = None
        self.can_be_followed = None
        self.can_subscribe = None
        self.description = None
        self.is_adult = False
        self.is_nsfw = False
        self.likes = []
        self.name = None
        self.reply_conditions = None
        self.share_following = None
        self.share_likes = None
        self.subscribed = None
        self.title = None
        self.total_posts = None
        self.updated = None
        self.url = None

    def get(self, key, default=None):
        if key in self:
            return getattr(self, key, default)
        else:
            return default

    def __getattr__(self, name):
        """        
        :param item: 
        :return: Blog
        :rtype: Blog 
        """
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such item: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Blogs(list):

    def __init__(self, d):
        super(Blogs, self).__init__(d)
        if isinstance(d, list):
            self.__dict__ = {"blogs": d}
            self.extend(d)
        elif isinstance(d, dict):
            self.__dict__ = d
            self.extend(d.get('blogs', []))

    def __getitem__(self, item):
        blog = super(list, self).__getitem__(item)
        #blog = super(Blogs, self).__getitem__(item)
        assert isinstance(blog, Blogs)
        return blog

    def __setitem__(self, index, value):
        try:
            assert isinstance(value, Blog)
            super(Blogs, self).__setitem__(index, value)
        except:
            blog = Blog(**value.__dict__)
            super(Blogs, self).__setitem__(index, blog)

    def get(self, key, default=None):
        if key in self:
            return getattr(self, key, default)
        else:
            return default