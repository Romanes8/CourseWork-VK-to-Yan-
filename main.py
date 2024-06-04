import requests
from datetime import datetime
import json
from tqdm import tqdm
import functions as f
from vk_photo import VK_photo
from yandex import Yandex


# вызов функции ввода исходных параметров для получения списка переменнных [vk_token, user_ids, Yan_token, count]
data_list = f.input_data()

# вызов функции folder_create для создания папки на Яндекс Диске
folder_name = f.folder_create(data_list[2])

# создание объекта на основе класса VK_photo для получения фотографий из vk и их параметров ввиде списка словарей(parameters_list)
VK_photo_info = VK_photo(data_list[1], data_list[0], data_list[3])

# вызов параметра parameters_list из класса VK_photo_info и создание переменной parameters_list для ее передачи в объект класса Yandex
parametrs_list = VK_photo_info.parameters_list

#создание объекта на основе класса Yandex
VK_to_Yan = Yandex(parametrs_list, folder_name, data_list[2])

#Вызов функции объекта класса Yandex по выгрузке фотографий на Яндекс диск
VK_to_Yan.photo_to_Yan()