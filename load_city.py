import json

f = open("1548394043.809042.txt", 'r')
# dic: dict = json.load(f)
#
# version_ = dic["version"]
#
# province_list_ = dic["provinceList"]
#
# for province in province_list_:
#     name = province["name"]
#     city_list = province["cityList"]
#

dic = json.load(f)
version_ = dic["version"]
ds = json.dumps(dic, indent="  ")

f = open("version-%s-pretty.txt" % version_, 'w')

f.write(ds)

