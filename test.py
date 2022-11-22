from pprint import pprint
import requests

token = 'y0_AgAAAAAyWxpTAADLWwAAAADUdq_-3ajoWQMTRa2AGJO-97b9-LXQ1_Y'

class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers = headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers = headers, params = params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path = disk_file_path).get('href', '')
        response = requests.put(href, data = open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')




if __name__ == '__main__':
    ya = YandexDisk(token = token)
    yb = ya.upload_file_to_disk(disk_file_path = '/test1.txt', filename = 'test.txt')
    # count = 0 # считаем количество файлов на диске
    # for key in yb['items']:
    #     count += 1
    #     pprint(key['name']) # выводим только названия файлов на диске
    # pprint(count)   