import json

f = open('./data/city-version-3.json')

obj: dict = json.load(f)

province_list: list = obj["provinceList"]

for province in province_list:
    # city_list = province["cityList"]
    province_file = open('./province_data/%s.json' % province["name"], 'w')
    json.dump(province, province_file, indent="  ")
