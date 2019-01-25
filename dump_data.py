import json

from city.city_get import Province, County, City, provinceList
import datetime

from city.version_util import get_version

version = get_version()

di = dict()
di["version"] = version
now = datetime.datetime.now()
date = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
di["date"] = date
di["timeStamp"] = now.timestamp()

proList = []


def make_province(p: Province):
    p.fetch_city_list()
    p_dict = dict()
    city_list = []

    p_dict["name"] = p.name

    for city in p.cityList:
        city: City = city
        c_dict = dict()
        c_dict["name"] = city.name
        c_dict["no"] = city.no
        city_list.append(c_dict)
        make_city(city, c_dict)

    p_dict["cityList"] = city_list
    proList.append(p_dict)


def make_city(city: City, city_obj: dict):
    city.fetch_county_list()
    li = []
    county_list: list[County] = city.countyList
    for county in county_list:
        c_obj = dict()
        c_obj["name"] = county.name
        c_obj["no"] = county.no
        li.append(c_obj)

    city_obj["countyList"] = li
    pass


for province in provinceList:
    print("province = %s" % province.name)
    make_province(province)

di["provinceList"] = proList

s = json.dumps(di)

f = open("data/city-version-%s.json" % version, 'w')

f.write(s)
