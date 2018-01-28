from instagram_private_api import Client, ClientCompatPatch
import json
import os
import time
import common as c
import broadcast as b
import feed as f

user_name = os.environ['INSTA_USER']
password = os.environ['INSTA_PASSWORD']
test_user = os.environ['TEST_USER_ID']
run_user = os.environ['RUN_USER_ID']

print('using creds: ', user_name, password)
print('Users: ', test_user, run_user)

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

# f.get_feed_items(api)
# uid = f.get_userid(api, test_user)

while True:

    is_broadcasting = b.check_livestream(api, test_user)
    log_color = "GREEN" if is_broadcasting else "RED"
    message = "{0}: {1} ".format(test_user, is_broadcasting)
    c.seperator(log_color)
    c.log(message, log_color)
    print('\n')

    time.sleep(15)



