import requests

#token_for_vk = input('Token for vk information:')
token_for_vk = '34f4f11807efbe8c1b82a0850fa70f137c556b7221acde76b2acbf4e7d90fc485f5bd4fdd4ccb496e8e95'
def GetInfoFromVk(user_id):
    """ get infomration from the vk about person."""
    url_vk = 'https://api.vk.com/method/account.getProfileInfo'
    params = {
            'access_token': token_for_vk,
            'user_id': user_id,
            'extended': 1,
            'v': 5.131
        }
    res = requests.get(url_vk, params=params).json()
    rrr = res[
        'response'
    ]
    return rrr

def GetPhotosVkData(user_id, count=5):
    """This function would get you the profile picture of the person in best resolution."""
    url_vk = 'https://api.vk.com/method/photos.get'
    params = {
        'access_token': token_for_vk,
        'user_id': user_id,
        'album_id': 'profile',
        'extended': 1,
        'count': count,
        'v': 5.131
        }
    res = requests.get(url_vk, params=params).json()
    rrr = res['response']['items']
    return rrr
    for k in rrr:
        return (k['sizes'][-1]['url'])
