from pydelicious import get_userposts, get_urlposts, get_popular

def initUserDict(tag, count=5):
    user_dict = {}
    for p1 in get_popular(tag=tag)[0:count]:
        for p2 in get_urlposts(p1['href']):
                user = p2['user']
                user_dict[user] = {}

    return user_dict

def fillItems(user_dict):
    all_item = {}
    for user in user_dict:
        for i in range(3):
            try:
                posts = get_userposts(user)
                break
            except:
                #print "failed, retrying"
                time.sleep(4)

        for post in posts:
            url=post['href']
            user_dict[user][url] = 1.0
            all_item[url] = 1

    for ratings in user_dict.values():
        for item in all_item:
            if item not in ratings:
                ratings[item] = 0.0

