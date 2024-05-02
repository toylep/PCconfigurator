import requests
from bs4 import BeautifulSoup
from db import VideoCard,CPU
from parsers.base.abstract_parser import DefaultParser

class TechnicalCityParser(DefaultParser):
    
    def parse(self):
        raw_data = self.get_raw_data()
        return self.convert_data_to_cls(raw_data)

    def get_raw_data(self):
        raw_data = self.bs.find('tbody').find_all('tr')
        return raw_data

    @classmethod
    def _parse_price(cls,data:str):
        data = data.text.strip()
        if data == '−' or data == '':
            data = None
        else:
            data = float(data[:-3])
        return data

    @classmethod
    def _parce_tpd(cls,data):
        data = data.text.strip()
        if data == '−':
            data = None
        else:
            data = data[:-1]
        return data


class VideoCardTehcCityParser(TechnicalCityParser):
    def convert_data_to_cls(self,raw_data):
        data_list = []
        for row in raw_data:
            try:
                data = row.find_all('td')
                name = data[1].find_all('a')[0].text.strip()
                type = data[2].find('span').text.strip()
                power_index = data[3].text.strip()
                arch = data[4].text.strip()
                tdp = self._parce_tpd(data[-1])
                price = self._parse_price(data[-2])
                # age = data[-3].text.strip()
                data_list.append(VideoCard(
                    name=name,
                    type=type,
                    power_index=power_index,
                    arch=arch,
                    price=price,
                    tdp=tdp
                ))
            except Exception as e:
                continue
        return data_list


class CPUTechCityParser(TechnicalCityParser):
     def convert_data_to_cls(self,raw_data):
        data_list = []
        for row in raw_data:
            try:
                data = row.find_all('td')
                name = data[1].find_all('a')[0].text.strip()
                type = data[2].find('span').text.strip()
                socket = data[3].text.strip()
                power_index = data[4].text.strip()
                core_threads = data[-4].text.strip()
                tdp = self._parce_tpd(data[-1])
                price = self._parse_price(data[-2])

                data_list.append(CPU(
                    name=name,
                    type=type,
                    power_index=power_index,
                    core_threads=core_threads,
                    price=price,
                    tdp=tdp,
                    socket=socket
                ))
            except Exception as e:
                continue
        return data_list