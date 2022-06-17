from FacadeCrawling import FacadeCrawling
import time
import logging


def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    while(True):
        start = time.time()

        x = FacadeCrawling()
        x.start_crawling()

        logging.info(f'execution time: minutes: {int((time.time() - start) / 60)} and seconds: {int((time.time() - start) % 60)}')
        time_spent = time.time() - start
        logging.info(f'next execution in: minutes: {int((time_spent * 5) / 60)} and seconds: {int((time_spent * 5) % 60)}')
        time.sleep(time_spent * 5)


if __name__ == '__main__':
    main()
