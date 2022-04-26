from crawler.crawled_data.CrawledData import CrawledData
from crawler.location.Location import Location
from repository.DatabaseHandler import DatabaseHandler
from repository.SQSHandler import SQSHandler

LIMIT_MIN = 0
LIMIT_MAX = 150
# da 0 a 149 ok

def main():
    index_id = LIMIT_MIN
    db = DatabaseHandler('crawler_test')
    sqs = SQSHandler('coda-crawler.fifo')
    while LIMIT_MIN - 1 < index_id < LIMIT_MAX:

        param = [{"name": "id", "value": {"longValue": index_id}}]

        query_post = 'select location.id as "loc_id", location.lat as "loc_lat", location.lng as "loc_lng", ' \
                     'location.loc_name as "loc_name", location.category as "loc_cat", location.phone as "loc_phone", '\
                     'location.website as "loc_website", location.is_restaurant as "loc_is_rest", post.id, ' \
                     'post.crawler_id, post.testo, post.data_pubb, post.username_autore from post ' \
                     'join location ' \
                     'on location.id = post.id_location where post.id = :id'

        query_img = 'select immagine.id as "img_id", immagine.post_id as "post_id" from immagine join post on ' \
                    'immagine.post_id = post.id where post.id = :id'

        db_data = db.do_read_query(query_post, param)

        if len(db_data) > 0:
            db_data = db_data[0]
            print('post id: ' + str(index_id))
            loc = Location(db_data['loc_name'], float(db_data['loc_lat']), float(db_data['loc_lng']),
                           db_data['loc_cat'],
                           db_data['loc_phone'], db_data['loc_website'], db_data['loc_id'])

            db_data_img = db.do_read_query(query_img, param)

            img_urls = []
            for el in db_data_img:
                img_urls.append(el['img_id'])
            print(img_urls)

            post = CrawledData(db_data['username_autore'], db_data['crawler_id'], db_data['data_pubb'], img_urls,
                               db_data['testo'], loc)

            sqs.enqueue_message(post)
            print('----------------------')
        index_id += 1


if __name__ == '__main__':
    main()
