from crawler.Crawler import Crawler
from repository.DatabaseHandler import DatabaseHandler
import boto3
import json

from repository.InternalRepository import InternalRepository

x = InternalRepository()

a = x.select_location('prova',42,42)

print(a[0])