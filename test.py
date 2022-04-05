from time import sleep
import time
import instagrapi.exceptions

from crawler.Crawler import Crawler
from repository.DatabaseHandler import DatabaseHandler
from crawler.profiles.FacadeAddProfile import FacadeAddProfile

# facade = FacadeAddProfile('lorenzolinguini')
# x = facade.add_profile()
# print(f'exit code: {x}')

# x = DatabaseHandler('crawler_test')
# transaction_id = x.begin_transaction()
# response = x.do_read_query('SELECT * FROM profilo_instagram where level = 1', transaction_id=transaction_id)[0]['post_visti']
# print('sleeping...')
# sleep(60)
# response = int(response) + 1
# x.do_write_query(f"UPDATE profilo_instagram SET post_visti = {response}  where level = 1", transaction_id=transaction_id)
# x.commit_transaction(transaction_id)

# resp = x.do_write_query('UPDATE profilo_instagram SET post_visti = post_visti + 1  where level = 1')
# print(resp)
from repository.ProfilesRepository import ProfilesRepository

start = time.time()

x = ProfilesRepository()
profiles = ['marco_food_details', 'estilo_ramy', 'diariodibrodo', 'flo_barone', 'blueshukin', 'matteofavaro']
for profile in profiles:
    x.insert_profile(profile)

# print(f'execution time: minutes: {int((time.time() - start) / 60)} and seconds: {int((time.time() - start) % 60)}')
