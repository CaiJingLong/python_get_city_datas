import json

f = open("./data/city-version-3.json", 'r')

dic = json.load(f)
version_ = dic["version"]
print("version = %s" % version_)
ds = json.dumps(dic, indent="  ")

f = open("./data/city-version-%s-pretty.json" % version_, 'w')

f.write(ds)

print("convert success")
