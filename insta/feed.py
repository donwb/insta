def get_feed_items(api):
    
    results = api.feed_timeline()
    items = [item for item in results.get('feed_items', [])
        if item.get('media_or_ad')]

    for item in items:
        # print(item['media_or_ad']['code'])
        print(item['media_or_ad']['user']['username'])
    

def get_userid(api, username):
    user_info = api.username_info(username)
    id = user_info['user']['pk']

    return id