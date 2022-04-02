from Facade import Facade
from crawler.Crawler import Crawler
from repository.DatabaseHandler import DatabaseHandler
import boto3
import json

from repository.InternalRepository import InternalRepository

x = Facade()

x.start_crawling()

# c = Crawler()
# c.login_from_cookies()
# media = c.get_media('lorenzolinguini', 3)

# for m in media:
#     print(c.get_detailed_location(m.location.name, m.location.lat, m.location.lng))

# l = InternalRepository()

# x = l.select_location ('La Piola Alba', 44.7005, 8.03598)

# db = DatabaseHandler('crawler_test')

# x = db.do_read_query("select * from location where lat = 44.5601 and lng = 11.3543")

# print(x)

# x = 323.123182

# x = round(x, 4)

# print(x)