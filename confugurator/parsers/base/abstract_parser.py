import requests
from bs4 import BeautifulSoup
from config import Base

class DefaultParser:

    def __init__(self,url,from_file=False) -> None:
        if from_file is True:
            with open(f'parser/docs/{url}','rb') as f:
                html = str(f.read())
        else:
            html = requests.get(url).text
        # print(html)
        print('------------------------')
        self.bs = BeautifulSoup(html,'html.parser')

    def parse(self)->list[Base]:
        raw_data = self.get_raw_data()
        return self.convert_data_to_cls(raw_data)

    def get_raw_data(self):
        pass

    def convert_data_to_cls(self,raw_data):
        pass