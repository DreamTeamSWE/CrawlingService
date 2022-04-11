import logging
from repository.ProfilesRepository import ProfilesRepository
from crawler.profiles.FacadeAddProfile import FacadeAddProfile


def prove():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # f = FacadeAddProfile('')
    # ret = f.add_profile()
    # print(ret)
    r = ProfilesRepository()
    r.insert_profile('iposticini')


if __name__ == '__main__':
    prove()
