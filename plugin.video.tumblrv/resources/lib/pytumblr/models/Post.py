from Blog import *

class PostType:

    def __init__(self, typename):
        self.__value__ = str(typename)

    @property
    def NONE(self):
        self.__value__ = None
        return self.__value__

    @property
    def ALL(self):
        self.__value__ = None
        return self.__value__

    @property
    def VIDEO(self):
        self.__value__ = 'video'
        return self.__value__

    @property
    def AUDIO(self):
        self.__value__ = 'audio'
        return self.__value__

    @property
    def PHOTO(self):
        self.__value__ = 'photo'
        return self.__value__

    @property
    def TEXT(self):
        self.__value__ = 'text'
        return self.__value__

    @property
    def LINK(self):
        self.__value__ = 'link'
        return self.__value__

    @property
    def CHAT(self):
        self.__value__ = 'chat'
        return self.__value__

    def __str__(self):
        return str(self.__value__.lower())

    def __repr__(self):
        return self.__str__()


class Reblog(dict):

    def __init__(self, **kwargs):
        """
        : attribute comment : string
        : attribute tree_html : string
        """
        super(Reblog, self).__init__(**kwargs)
        self.comment = None
        self.tree_html = None

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Player(dict):

    def __init__(self, **kwargs):
        """
        : attribute width : float
        : attribute embed_code : string
        """
        super(Player, self).__init__(**kwargs)
        self.width = None
        self.embed_code = None

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Sizes(dict):

    def __init__(self, **kwargs):
        """
        : attribute url : string
        : attribute width : float
        : attribute height : float
        """
        super(Sizes, self).__init__(**kwargs)
        self.url = None
        self.width = None
        self.height = None

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Exif(dict):

    def __init__(self, **kwargs):
        """
        : attribute camera : string
        : attribute focal_length : string
        : attribute exposure : string
        : attribute i_s_o : float
        : attribute aperture : string
        """
        super(Exif, self).__init__(**kwargs)
        self.camera = None
        self.focal_length = None
        self.exposure = None
        self.i_s_o = None
        self.aperture = None

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Photo(dict):

    def __init__(self, **kwargs):
        """
        : attribute caption : string
        : attribute alt_sizes : array
        : attribute original_size : OriginalSize
        """
        super(Photo, self).__init__(**kwargs)
        self.original_size = Sizes(**kwargs.get('original_size', {}))
        self.alt_sizes = []
        self.caption = None
        for size in kwargs.get('alt_sizes', []):
            self.alt_sizes.append(Sizes(**size))

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Post(dict):

    def __init__(self, **kwargs):
        """
        : attribute reblog : Reblog
        : attribute summary : string
        : attribute id_property : float
        : attribute blog_name : string
        : attribute trail : array
        : attribute post_url : string
        : attribute state : string
        : attribute player : array
        : attribute can_send_in_message : bool
        : attribute slug : string
        : attribute duration : float
        : attribute html5_capable : bool
        : attribute type_property : string
        : attribute short_url : string
        : attribute caption : string
        : attribute thumbnail_width : float
        : attribute display_avatar : bool
        : attribute date : string
        : attribute can_like : bool
        : attribute reblog_key : string
        : attribute can_reblog : bool
        : attribute format : string
        : attribute tags : array
        : attribute thumbnail_height : float
        : attribute thumbnail_url : string
        : attribute note_count : float
        : attribute video_type : string
        : attribute can_reply : bool
        : attribute video_url : string
        : attribute post_author : string
        : attribute timestamp : float
        """
        super(Post, self).__init__(**kwargs)
        self.__dict__ = kwargs
        self.blog = Blog(**kwargs.get('blog', {}))
        self.reblog = Reblog(**kwargs.get('reblog', {}))
        self.player = Player(**kwargs.get('player', {}))
        self.trail = Trail(**kwargs.get('trail', {}))
        self._name = kwargs.get('name', kwargs.get('blog_name', ''))
        self.type_property = PostType(kwargs.get('type'))
        self.tags = []
        self.id = None
        self.can_like = False
        self.can_reblog = False
        self.can_reply = False
        self.can_send_in_message = False
        self.caption = None
        self.date = None
        self.display_avatar = None
        self.duration = None
        self.followed = None
        self.format = None
        self.html5_capable = None
        self.liked = None
        self.liked_timestamp = None
        self.note_count = None
        self.post_author = None
        self.post_url = None
        self.reblog_key = None
        self.recommended_color = None
        self.recommended_source = None
        self.short_url = None
        self.slug = None
        self.state = None
        self.summary = None
        self.thumbnail_height = None
        self.thumbnail_url = None
        self.thumbnail_width = None
        self.timestamp = None
        self.video_type = None
        self.video_url = None
        self.video_url = None

    def get(self, key, default=None):
        if key in self:
            return getattr(self, key, default)
        else:
            return default

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, blogname):
        self._name = blogname
    @property
    def blog_name(self):
        return self._name
    @blog_name.setter
    def blog_name(self, blogname):
        self._name = blogname

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)
    def __setattr__(self, name, value):
        self[name] = value
    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Posts(list):

    def __init__(self, d):
        super(Posts, self).__init__(d)
        if isinstance(d, list):
            self.__dict__ = {"posts": d}
            self.extend(d)
        elif isinstance(d, dict):
            self.__dict__ = d
            self.extend(d.get('posts', []))

    def __getitem__(self, item):
        if self.__contains__(item):
            idx = self.index(item)
            post = self[idx]
            #post = super(list, self).__getitem__(item)
            #post = super(Posts, self).__getitem__(item)
            assert isinstance(post, Post)
            return post
        else:
            return None


    def __setitem__(self, index, value):
        post = Post(**value)
        super(list, self).__setitem__(index, post)


    def get(self, key, default=None):
        if key in self:
            return getattr(self, key, default)
        else:
            return default