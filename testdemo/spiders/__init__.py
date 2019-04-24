# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import django
import flask
def myabs(x):
    if x>=0:
        return x
    else:
        return -x
print(myabs(-99))