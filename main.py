from instagram_private_api import Client, ClientCompatPatch
import json
import os
import common as c

user_name = os.environ['INSTA_USER']
password = os.environ['INSTA_PASSWORD']

print('using creds: ', user_name, password)

# check to see if we have a cached settings file
use_cached = os.path.isfile('settings.json')

# this avoids hitting the login to many times and getting blocked
if use_cached:
    print("Settings file found, using cached creds...")
    
    with open('settings.json') as file_data:
        cached_auth = json.load(file_data, object_hook=c.from_json)
        api = Client(
            user_name, password,
            auto_patch=True, drop_incompat_keys=False,
            settings=cached_auth)
else:
    print("No cached settings, logging in...")

    api = Client(user_name, password, auto_path=True)
    cached_auth = api.settings
    with open('settings.json', 'w') as outfile:
        json.dump(cached_auth, outfile, default=c.to_json)


# this is the actual api call
results = api.feed_timeline()
items = [item for item in results.get('feed_items', [])
    if item.get('media_or_ad')]

for item in items:
    # print(item['media_or_ad']['code'])
    print(item['media_or_ad']['user']['username'])
    

