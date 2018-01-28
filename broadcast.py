def check_livestream(api, userid):
    broadcasting = api.user_broadcast(userid)
    return broadcasting is not None
