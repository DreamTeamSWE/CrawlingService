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
    # # crawler = Crawler()
    # # crawler.login_from_cookies()
    # # x = crawler.get_media('lorenzolinguini', 5)
    # # print(x)
    # # pk=298711932, name='Piazza Duomo'
    logging.info('login from cookies...')
    s3 = boto3.client(service_name='s3')
    content_object = s3.get_object(Bucket='sweeat-crawler-cookies', Key='tommolocas.txt')
    file_content = content_object['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    cl = instagrapi.Client(json_content)
    logging.info('login successful!')
    medias = cl.location_medias_recent(106055111151602, 48)
    db = ProfilesRepository()
    for i, media in enumerate(medias):
        username = media.user.username
        if len(db.select_profile(username)) == 0:
            logging.info(f'{i}: add profile: ' + username)
            db.insert_profile(username)
        else:
            logging.info(f'{i}: profile already exists: ' + username)
    # crawler = Crawler()
    # crawler.login_from_account('collinaterenzio', 'dreamteam')
    # crawler.save_cookies()

    # import random
    # for i in range(120):
    #     x = random.randint(1, 12)
    #     if x == 1:
    #         print(f'ok: {i}')

    # import requests
    # api_key = 'bot5387718013:AAElCJj5EsTYSE3-ONQytxqi9dkiEtwg2XY'
    # chat_id = '-1001639546628'
    # message = 'messaggio da python'
    # for i in range (10):
    #     requests.get(f'https://api.telegram.org/{api_key}/sendMessage?chat_id={chat_id}&text={message}')


if __name__ == '__main__':
    prove()
    # os.system('coverage run -m unittest test.py')
    # os.system('coverage html')
    # os.system('.\\htmlcov\\index.html')

# pk di location per ampliare la lista di profili:
# , , , , , , 292435251595163, 1402084993153509,
# 100105881340388, 157421679, 379776280, 1635966796508958, 269768445, 108997440934705, 111472130189318, 715292428841704,
# 240192888, 100316634751956, 308894999781307, 110576520640631, 636580735, 2034385343520246
