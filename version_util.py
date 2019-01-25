import json

f = open("CONFIG", 'r')
p = json.load(f)
version = p["version"]


def get_version() -> int:
    return version
