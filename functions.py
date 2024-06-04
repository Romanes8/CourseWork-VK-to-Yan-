import requests


# функция ввода исходных данных, возвращает список переменных VK токена,
# ID пользователя VK, токена Яндекс Диска и количества фотографий
def input_data():
    vk_token = input("Введите токен VK: ")
    user_ids = int(input("Введите user id VK: "))
    Yan_token = input("Введите токен Яндекс Диска: ")
    count_fhoto = input("Укажите количство загружаемых фотографий(по умолчанию 5 фотографий): ")
    if count_fhoto == '':
        count = 5
        print('На Яндекс Диск загрузится 5 фотографий.')
    else:
        count = count_fhoto
    return [vk_token, user_ids, Yan_token, count]


# функция создания папки на Яндекс Диске
def folder_create(Yan_token):
    folder_name = input("Введите название папки для фото на Яндекс Диске: ")
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': Yan_token}
    params = {'path': folder_name}
    while requests.get(url=url, params=params, headers=headers).status_code == 200:
        print('Такая папка уже существует, введите другое имя.')
        folder_name = input("Введите название папки для фото на Яндекс Диске: ")
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': Yan_token}
        params = {'path': folder_name}
    else:
        print(f'Папка {folder_name} создана')
        requests.put(url=url, params=params, headers=headers)
        return folder_name





