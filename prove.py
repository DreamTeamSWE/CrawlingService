import logging
import instagrapi
import boto3
import json
import os
from repository.ProfilesRepository import ProfilesRepository
from crawler.profiles.FacadeAddProfile import FacadeAddProfile
from crawler.Crawler import Crawler


def prove():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # crawler = Crawler()
    # crawler.login_from_cookies()
    # x = crawler.get_media('lorenzolinguini', 5)
    # print(x)
    # pk=298711932, name='Piazza Duomo'
    logging.info('login from cookies...')
    s3 = boto3.client(service_name='s3')
    content_object = s3.get_object(Bucket='sweeat-crawler-cookies', Key='instaswe2021.txt')
    file_content = content_object['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    cl = instagrapi.Client(json_content)
    logging.info('login successful!')
    medias = cl.location_medias_recent(298711932, 48)
    db = ProfilesRepository()
    for i, media in enumerate(medias):
        username = media.user.username
        if len(db.select_profile(username)) == 0:
            logging.info(f'{i}: add profile: ' + username)
            db.insert_profile(username)
        else:
            logging.info(f'{i}: profile already exists: ' + username)


if __name__ == '__main__':
    # prove()
    os.system('coverage run -m unittest test.py')
    os.system('coverage html')
    os.system('.\\htmlcov\\index.html')

