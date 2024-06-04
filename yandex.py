import requests
import json
from tqdm import tqdm

#класс Yandex принимает на вход список словарей с параметрами фотографий, название папки на Яндекс Диске, токен Яндекс Диска,
#выполняет загрузку фотографий на Яндекс Диск и формирует отчет о загрузке в формате json.
class Yandex:
    def __init__(self, parameters_list, folder_name, Yan_token):
        self.parameters_list = parameters_list
        self.folder_name = folder_name
        self.Yan_token = Yan_token

    #метод формирования json файла для выгрузки отчета
    def json_info(self):
        # создание списка лайков для проверки на их повторение
        likes_list = []
        for el in self.parameters_list:
            likes_list.append(dict['likes'])
            # формирование json файла для выгрузки
        self.json_list = []
        for el in self.parameters_list:
            if el['likes'] in likes_list:
                json_dict = {"file_name": f"{el['likes']}.jpg_{el['date']}",
                            "size": el['size']
                                }
                self.json_list.append(json_dict)
                json_list_js = json.dumps(self.json_list)
                with open('upload_report.json', 'w') as f:
                    f.write(json_list_js)
            else:
                json_dict = {"file_name": f"{el['likes']}.jpg",
                                 "size": el['size']
                                 }
                self.json_list.append(json_dict)
                json_list_js = json.dumps(self.json_list)
                with open('upload_report.json', 'w') as f:
                    f.write(json_list_js)
        return self.json_list

        # метод загрузки фотографий на Яндекс Диск
    def photo_to_Yan(self):
        js_list = self.json_info()
        print(f'Загрузка фотографий в папку {self.folder_name}:')
        for el in tqdm(list(zip(self.parameters_list, js_list))):
            foto_url = el[0]['url']
            fhoto_name = el[1]['file_name']
            url_yn = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            headers = {'Authorization': self.Yan_token}
            params = {'url': foto_url,
                      'path': f'{self.folder_name}/{fhoto_name}'}
            response = requests.post(url=url_yn, params=params, headers=headers)
        print('Загрузка фотографий на Яндекс Диск завершена')