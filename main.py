from crawler.Crawler import Crawler
from repository.DatabaseHandler import DatabaseHandler

db = DatabaseHandler('crawler_test')

x = db.do_write_query("insert into location (lat, lng, loc_name, category) values (42,42,'prova','prova')")

y = db.do_read_query('select * from location limit 10')


print(x)

print(y)