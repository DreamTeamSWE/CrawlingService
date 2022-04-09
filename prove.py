from repository.DatabaseHandler import DatabaseHandler
from repository.ProfilesRepository import ProfilesRepository
from crawler.profiles.ProfileFactory import ProfileFactory
from datetime import datetime

# prof = ProfilesRepository()
# x = prof.select_profile('blueshukin')
# ls = x[0]['data_ultimo_check']
# ls = '2018-12-01 00:00:00'
# ls = datetime.strptime(ls, '%Y-%m-%d %H:%M:%S')
# now = datetime.now()
#
# print(ls)
# print(now)
# # #days of difference beetwen current time and last check
# diff = (now - ls).days
# print(diff)

db = ProfilesRepository()
for i in range (10):
    db.get_profile_for_crawling_level_1()
