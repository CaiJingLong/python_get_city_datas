# 获取省市数据列表

## 代码使用说明

git clone https://github.com/CaiJingLong/python_get_city_datas.git city

python3 city/dump_data.py

如果缺少python库, 自己用pip获取一下

## 数据来源
[国家统计局2018年](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/)

## 思路可以看我的[blog](https://www.kikt.top/posts/python/get_city_datas/)

[blog](https://www.kikt.top/posts/python/get_city_datas/)

讲述了一些网页布局的分析过程

## 文件说明

city_get.py : 爬取数据的文件

get_county.py: 获取第三级数据的优化版本

dump_data.py: 将数据转为 json

format-data.py: 美化json数据并输出到文件

convert_sqlite.py: 转化json为数据库

## 数据

目前有json格式(211k)

pretty json(405k)

sqlite(276k)

可以从data中下载

## 其他说明

如果需要到街道层级,这个程序是不支持的,但是简单的扩展一下也是可以支持的,不过那样文件会更大,不太适合使用json作为载体

现在的完整json文件有200k左右, 如果增加到4级(街道) 5级(居委会/村委会) 则数据会增长10/100倍

----

如果你有需求,需要爬取到第五级,数据量会扩大接近一百倍,可以联系我私聊(cjl_spy@163.com) :-D
