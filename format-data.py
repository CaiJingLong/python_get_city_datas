import json

f = open("1548394043.809042.txt", 'r')

dic = json.load(f)
version_ = dic["version"]
ds = json.dumps(dic, indent="  ")

f = open("version-%s-pretty.txt" % version_, 'w')

f.write(ds)

