import json

f = open("city-version-2.json", 'r')

dic = json.load(f)
version_ = dic["version"]
ds = json.dumps(dic, indent="  ")

f = open("city-version-%s-pretty.json" % version_, 'w')

f.write(ds)
