import os
import sqlite3
import json

from city.version_util import get_version

version = get_version()

db_name = "./data/city-version-%s.sqlite" % version

try:
    os.remove(db_name)
except:
    pass

conn = sqlite3.connect(db_name)

cursor = conn.cursor()


def exec_sql(sql: str):
    cursor.execute(sql)


def create_table():
    exec_sql("""create table province
(
	no int primary key,
	name TEXT
)
;
""")

    exec_sql("""
create unique index province_no_uindex
	on province (no)
;""")

    exec_sql("""create table city
    (
        no int primary key,
        name text,
        province_no int
    )
    ;
""")

    exec_sql("""
    create unique index city_no_uindex
        on city (no)
    ;""")

    exec_sql("""create table county
(
	no int primary key,
	name text,
	city_no int
)
;
""")
    exec_sql("""
        create unique index county_no_uindex
            on county (no)
        ;""")
    conn.commit()


create_table()


def insert_province(no, name):
    cursor.execute("""insert into province (no, name)
values (?, ?);
""", (no, name))
    pass


def insert_city(no, name, province_no):
    cursor.execute("""insert into city (no, name, province_no)
values (?, ?, ?);""", (no, name, province_no))
    pass


def insert_county(no, name, city_no):
    cursor.execute("""insert into county (no, name, city_no)
values (?, ?, ?);""", (no, name, city_no))
    pass


def convert_json_data():
    json_path = "./data/city-version-%s.json" % version
    f = open(json_path, 'r')
    params = json.load(f)
    province_list = params["provinceList"]
    for p in province_list:
        p_no = p["no"]
        insert_province(p_no, p["name"])
        city_list = p["cityList"]
        for city in city_list:
            no = city["no"]
            name = city["name"]
            insert_city(no, name, p_no)
            county_list = city["countyList"]
            for county in county_list:
                county_no = county["no"]
                county_name = county["name"]
                insert_county(county_no, county_name, no)
    conn.commit()
    pass


convert_json_data()

conn.close()
