# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class TestdemoPipeline(object):
    def process_item(self, item, spider):
        return item
    def __init__(self):
        self.conn=pymysql.connect(host='127.0.0.1',port=3306,user'root',passwd='cw123456',db='connect',charset='utf-8')
        self.cursor=self.conn.cursor()
        self.cursor.execute("truncate table Movie")
        self.conn.commit()

    def process_item(self,item,spider):
        jsonnext=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.filename.write(jsonnext.encode("utf-8"))
        return item
    def close_spider(self,spider):
        self.filename.close()