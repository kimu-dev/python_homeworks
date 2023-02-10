from pprint import pprint
import requests
import os


# ЗАДАЧА №1
def get_heroes(): # самый умный герой из списка ['Hulk', 'Captain America', 'Thanos']
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    files_url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(files_url)
    heroes_dict = response.json()
    heroes_dict_sorted = {}
    for hero in heroes_dict:
        if hero['name'] in heroes_list:
            heroes_dict_sorted[hero['name']] = hero['powerstats']['intelligence']

    return list(sorted(heroes_dict_sorted.items(), reverse = True))[0]


# ЗАДАЧА №2
class YaUploader: 
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(upload_url, headers = headers, params = params)
        pprint(response.json())
        return response.json()

    def upload(self, path_to_file: str):
        filename = os.path.basename(path_to_file)
        href = self._get_upload_link(path_to_file = f'Netology/{filename}').get('href', '')
        response = requests.put(href, data = open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

# ЗАДАЧА №3
# Самый важный сайт для программистов это stackoverflow. И у него тоже есть API Нужно написать программу, 
# которая выводит все вопросы за последние два дня и содержит тэг 'Python'. Для этого задания токен не требуется.

def get_stackoverflow():
    files_url = 'https://api.stackexchange.com/questions/'
    params = {'order': 'desc', 'min': '1668902400', 'max': '1669075200', 'sort': 'creation', 'tagged': 'python', 'site': 'stackoverflow'}
    response = requests.get(files_url, params = params)
    r = response.json()

    for key in r['items']:
        pprint(key['title'])


if __name__ == '__main__':
    pprint(get_heroes())
    get_stackoverflow()
    # Получить путь к загружаемому файлу и токен от пользователя
    base_path = os.getcwd()
    ydisk_catalog_name = 'ydisk'
    file_name = 'fio.txt'
    path_to_file = base_path +'\\'+ ydisk_catalog_name +'\\'+ file_name
    token = ...

    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

