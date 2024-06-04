import requests
from datetime import datetime


#класс VK_photo принимает на вход ID пользователя VK, VK токен, количество фото для загрузки на Яндекс Диск.
#класс получает и формирует в виде списка словарей информацию о фотографиях, необходимую для загрузки фото на Яндекс Диск.
class VK_photo:
    def __init__(self, user_ids, vk_token, count):
        self.user_ids = user_ids
        self.vk_token = vk_token
        self.count = count
        self.parameters_list = self.photo_info()

    #метод получения фотографий из VK
    def get_photo(self):
        url_vk = 'https://api.vk.com/method/photos.get'
        params = { 'owner_id': self.user_ids,
                   'album_id': 'profile',
                   'access_token': self.vk_token,
                   'extended': 1,
                   'count': self.count,
                   'v': '5.199'
                  }
        self.response = requests.get(url=url_vk, params=params).json()
        return self.response

    # метод формирования списка словарей с нужными параметрами фотографий
    def photo_info(self):
        self.parameters_list = []
        response = self.get_photo()
        items = response['response']['items']
        for el in items:
            list_sizes = []
            for sizes in el['sizes']:
                size_fhoto = sizes['height']*sizes['width']
                list_sizes.append(size_fhoto)
            list_sizes_sorted = sorted(list(enumerate(list_sizes)), reverse=True, key=lambda x: x[1])
            parameters_dict = {'likes': el['likes']['count'],
                               'date': str(datetime.fromtimestamp(el['date']))[0:10],
                               'url': el['sizes'][list_sizes_sorted[0][0]]['url'],
                               'size': el['sizes'][list_sizes_sorted[0][0]]['type']
                               }
            self.parameters_list.append(parameters_dict)
        return self.parameters_list