import requests
import pprint

token_for_vk = '34f4f11807efbe8c1b82a0850fa70f137c556b7221acde76b2acbf4e7d90fc485f5bd4fdd4ccb496e8e95' #input('Token for vk information:')
#token_for_vk = input('Token for infomation in vk: ')
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
    return rrr['city']['title'], rrr['sex'],


#a,b= GetInfoFromVk(670276685)
#print(a)


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


def ListOfCities(user_id):
    """This function would get you the list of cities in the country that you chosen."""
    city, sex = GetInfoFromVk(user_id)
    url_vk = 'https://api.vk.com/method/database.getCities'
    params = {
        'access_token': token_for_vk,
        'country_id': 1,
        'region_id': '',
        'q': '',
        'need_all': '',
        'count': 100,
        'v': 5.131
        }
    res = requests.get(url_vk, params=params).json()
    rrr = res['response']['items']
    for i in rrr:
        if i['title'] == f'{city}':
            return i['id']
        return rrr



def sex_number(sex_num):
    if sex_num == 1:
        return 2
    else:
        return 1

def age_preferences(numer_for_age):
    if numer_for_age == 1:
        return 18, 24
    elif numer_for_age == 2:
        return 25, 34
    elif numer_for_age == 3:
        return 35, 44
    elif numer_for_age == 4:
        return 45, 54
    elif numer_for_age == 5:
        return 55, 64
    elif numer_for_age == 6:
        return 65, 74
    elif numer_for_age == 7:
        return 75, 100




def get_users_for_date(user_id, number_for_age):
    """ get random users photos, names and ids by your criteria for you """
    number = ListOfCities(user_id)
    city_name, sex_num = GetInfoFromVk(user_id)
    num_for_part_sex = sex_number(sex_num)
    age_from, age_to = age_preferences(number_for_age)
    url_vk = 'https://api.vk.com/method/users.search'
    params = {
        'access_token': token_for_vk,
        'q': '',
        'sort': 0,
        'offset': '',
        'count': 3,
        'fields': 'photo',
        'country': 1,
        'city': number,
        'hometown': '',
        'sex': num_for_part_sex,
        'status': 6,
        'age_from': age_from,
        'age_to': age_to,
        'has_photo': 1,
        'v': 5.131
    }
    res = requests.get(url_vk, params=params).json()
    rrr = res['response']['items']
    values_of_key = [a_dict['photo'] for a_dict in rrr]
    name = [a_dict['first_name'] for a_dict in rrr]
    id_of_person = [a_dict['id'] for a_dict in rrr]
    return values_of_key, name, id_of_person

#print(get_users_for_date(670276685, 1))


import pathlib
pathlib.Path().resolve()

import os
#path = '/Users/mitch/Desktop/python class/python 2/thesis python 2'
print(os.path.abspath(os.getcwd()))
#print(os.listdir(path))