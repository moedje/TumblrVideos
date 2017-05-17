import pytumblr
import datetime
import os

def getAllPosts (client, blog):
    offset = 0
    while True:
        post_response = client.posts(blog, limit=20, offset=offset, filter="text", type="text")
        reslist = []
        if len(post_response.get('posts','')) is 0 and len(post_response.get('blogs','')) is 0:
            return
        if len(post_response.get('blogs','')) > 0:
            reslist = post_response['blogs']
        elif len(post_response.get('posts','')) > 0:
            reslist = post_response['posts']
        for item in reslist:
            print(str(repr(item)))
            yield item
        offset += 20

def any_keyword_in(keywords, string):
    for keyword in keywords:
        if keyword in string:
            return True
    return False

def search(keywords, client, tumblr_url, write_to_datefile=False):
    if not isinstance(keywords, list):
        raise Exception("search keywords must be a list")
    items = []
    for post in getAllPosts(client, tumblr_url):
        body = post.get('body', "not text").encode("utf-8")
        # think this is right
        timestamp = post.get('timestamp')
        if timestamp:
            post_date = datetime.datetime.fromtimestamp(timestamp).strftime('%F')
            # append date we're on to this file to get an idea of progress/time left
            if write_to_datefile:
                # optionally write the date of current post to a file
                with open('dateSearchIsOn', 'a') as f:
                    f.write(post_date + "\n")

         # if any(['blueball' in lbody, 'blue ball' in lbody, 'dear white people' in lbody]):
        if any_keyword_in(keywords, body.lower()):
            items.append(post)
    return items
