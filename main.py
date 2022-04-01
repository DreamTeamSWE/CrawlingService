from crawler.Crawler import Crawler
from repository.DatabaseHandler import DatabaseHandler
import boto3
import json

cl = Crawler()
cl.login_from_cookies()
x = cl.get_public_following_list('francesco.erre')

print(x)