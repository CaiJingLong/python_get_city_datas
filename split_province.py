import json

from city.version_util import get_version

version = get_version()

f = open('./data/city-version-%s.json' % version)

obj: dict = json.load(f)

province_list: list = obj["provinceList"]

for province in province_list:
    # city_list = province["cityList"]
    province_file = open('./province_data/%s.json' % province["name"], 'w')
    province["version"] = obj["version"]
    province["date"] = obj["date"]
    province["timeStamp"] = obj["timeStamp"]
    json.dump(province, province_file, indent="  ")
