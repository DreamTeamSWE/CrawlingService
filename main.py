from FacadeCrawling import FacadeCrawling
import time
import logging


def main(event, context):
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    start = time.time()

    x = FacadeCrawling()
    x.start_crawling()

    logging.info(f'execution time: minutes: {int((time.time() - start) / 60)} and seconds: {int((time.time() - start) % 60)}')


if __name__ == '__main__':
    main()
