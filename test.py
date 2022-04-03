import datetime

# x = Facade()

# x.start_crawling()

# c = Crawler()
# c.login_from_cookies()
# media = c.get_media('lorenzolinguini', 3)
# print(media)
# for m in media:
#     print(c.get_detailed_location(m.location.name, m.location.lat, m.location.lng))

# l = InternalRepository()

# x = l.select_location ('La Piola Alba', 44.7005, 8.0360)

# print(x[0]['id'])

# l = LocationFactory().build_from_db(x[0])


# db = DatabaseHandler('crawler_test')

# x = db.do_read_query("select * from location where lat = 44.5601 and lng = 11.3543")

# print(x)

# x = 323.123182

# x = round(x, 4)

# print(x)

# x = InternalRepository()

# response = x.save_location(location('prova4', 44.5601, 11.3543, 'ciao', 'ciao', 'ciao'))
# print(response['generatedFields'][0]['longValue'])

#random float beetwen 5 and 10

# current datetime

x = datetime('2022-04-01 10:10:18+00:00')
print(x.strftime("%Y-%m-%d %H:%M:%S"))