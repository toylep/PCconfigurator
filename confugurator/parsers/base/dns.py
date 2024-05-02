from parsers.base.abstract_parser import DefaultParser
from db import DNSVideoCard
#https://www.dns-shop.ru/product/microdata/d5635852-337e-11eb-a211-00155d03332b/
#https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/ catalog-products view-simple
class DNSDefaultParser(DefaultParser):

    def get_raw_data(self):
        raw_data = self.bs.find_all('div',{'data-id':'product'})
        return raw_data

    def convert_data_to_cls(self, raw_data):
        data_list = []
        for row in raw_data:
            try:
                data = row.find('a',{'class':'catalog-product__name ui-link ui-link_black'}).find('span').text.split('                ')[1].split(' [')[0].split()
                print('data',data)
                vendor = data[0]
                # print(data[1])
                name = ' '.join(data[1:5] if data[1] == 'AMD' else data[1:4])
                price = ''.join(row.find('div',{'class':'product-buy__price'}).text.split()[:2]).strip()
                # print(name)
                # print(price)
                data_list.append(DNSVideoCard(
                    name=name,
                    price=price,
                    vendor=vendor,
                    ))
            except Exception:
                continue


        return data_list
