import json

from city.version_util import get_version

version = get_version()

f = open("./data/city-version-%s.json" % version, 'r')

dic = json.load(f)
print("version = %s" % version)
ds = json.dumps(dic, indent="  ")

f = open("./data/city-version-%s-pretty.json" % version, 'w')

f.write(ds)

print("convert success")
