# 获取省市数据列表

代码使用说明

git clone https://github.com/CaiJingLong/python_get_city_datas.git city

python3 city/dump_data.py

## 文件说明

city_get.py : 爬取数据的文件

dump_data.py: 将数据转为 json

format-data.py: 美化数据并输出到文件

## 其他说明

目前只有json形式,数据库形式没有打算开发

如果需要到街道层级,这个程序是不支持的,但是简单的扩展一下也是可以支持的,不过那样文件会更大,绝对不适合使用json作为载体了

目前也很夸张了 json的纯文本格式有30M+的大小

----

甚至如果你有需求,需要爬取到第五级,也就是街道级,数据量会扩大接近一百倍,可以联系我私聊(cjl_spy@163.com) :-D