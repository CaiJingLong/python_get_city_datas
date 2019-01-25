from requests_html import HTMLSession, HTMLResponse, HtmlElement, Element

html_session = HTMLSession()


def get_county(url: str) -> list:
    name = ""
    no = ""
    r: HTMLResponse = html_session.get(url)
    html = r.html
    result = []
    l: list = html.find(".countytr")
    t: list = []
    for e in l:
        e: Element = e
        tds = e.find("td")
        for td in tds:
            td: Element = td
            if td.text.isnumeric():
                no = td.text
            else:
                name = td.text
                result.append((name, no))
    return result


if __name__ == '__main__':
    get_county("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/13/1302.html")
