import json
from requests_html import HTMLSession
import requests_html

session = HTMLSession()


class Entity:
    name: str
    link: str
    no: str
    baseUrl = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/"

    def __str__(self) -> str:
        return "name:%s,link=%s" % (self.name, self.link)

    def __eq__(self, o: object) -> bool:
        return self.link == o.link

    def to_json(self) -> str:
        pass


class Province(Entity):

    def __init__(self) -> None:
        super().__init__()
        self.cityList = []

    def __str__(self) -> str:
        return "name:%s,link=%s" % (self.name, self.link)

    def fetch_city_list(self):
        url = "%s%s" % (Entity.baseUrl, self.link)
        r = session.get(url)
        r.encoding = "gbk"
        h: requests_html.HTML = r.html
        li: list[requests_html.Element] = h.find("a")
        for a in li:
            text = a.text
            if text.__contains__("京ICP"):
                continue
            href_ = a.attrs["href"]
            city = City()
            city.link = href_
            city.province = self
            # print(text, href_)

            try:
                index = self.cityList.index(city)
                city = self.cityList[index]
            except ValueError:
                self.cityList.append(city)

            if text.isnumeric():
                city.no = text
            else:
                city.name = text

        for city in self.cityList:
            city.fetch_county_list()

    def to_json(self) -> str:
        pass


class City(Entity):
    province: Province

    def __init__(self) -> None:
        super().__init__()
        self.countyList = []

    def fetch_county_list(self):
        print("%s 开始" % self.name)
        url = "%s%s" % (Entity.baseUrl, self.link)
        r = session.get(url)
        r.encoding = "gbk"
        h: requests_html.HTML = r.html
        li: list[requests_html.Element] = h.find("a")
        for a in li:
            text = a.text
            if text.__contains__("京ICP"):
                continue
            href_ = a.attrs["href"]
            county = County()
            county.link = href_
            county.province = self
            # print(text, href_)

            try:
                index = self.countyList.index(county)
                county = self.countyList[index]
            except ValueError:
                self.countyList.append(county)

            if text.isnumeric():
                county.no = text
            else:
                county.name = text

        for county in self.countyList:
            # print(county.__str__())
            pass

        print("%s 结束" % self.name)

    pass


class County(Entity):
    city: City
    pass


provinceList = []


def fetch_province_list():
    response = session.get("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html")
    response.encoding = "gbk"
    html: requests_html.HTML = response.html
    # s = response.content.decode("gbk")
    l: list = html.find("a")
    for a in l:
        ae: requests_html.Element = a
        href: str = ae.attrs.get("href")
        if href.endswith("html"):
            province = Province()
            province.name = ae.text.lstrip()
            province.link = href.lstrip()
            provinceList.append(province)


fetch_province_list()

if __name__ == '__main__':
    for p in provinceList:
        if p.name == "黑龙江省":
            p.fetch_city_list()
# session.close()
