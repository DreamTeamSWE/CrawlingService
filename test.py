import instagrapi.exceptions

from crawler.Crawler import Crawler
from repository.DatabaseHandler import DatabaseHandler
from crawler.profiles.FacadeAddProfile import FacadeAddProfile

facade = FacadeAddProfile('fuckitsjaq')
x = facade.add_profile()
print(f'exit code: {x}')
