import pytumblr
import datetime
import os

def getAllPosts (client, blog):
    offset = 0
    allposts = []
    more = True
    while more:
        post_response = client.posts(blog, limit=20, offset=offset, filter="text").get('posts', [])
        if len(post_response) < 1:
            more = False
        else:
            allposts.extend(post_response)
            offset += 20
    return allposts

def any_keyword_in(keywords, string):
    for keyword in keywords:
        if keyword in string:
            return True
    return False

def search(keywords, client, tumblr_url, write_to_datefile=False):
    if not isinstance(keywords, list):
        raise Exception("search keywords must be a list")
    items = []
    posts = getAllPosts(client, tumblr_url)
    for post in posts:
        body = post.get('body', " ").encode("utf-8") + ' ' + post.get('caption', " ").encode("utf-8") + ' ' + post.get('source_title', " ").encode("utf-8") + ' ' + post.get('summary', " ").encode("utf-8")+ ' ' + str(post.get('tags', [])[:])
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
