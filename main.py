from Facade import Facade
import time
import logging


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
start = time.time()

x = Facade()
x.start_crawling()

logging.info(f'execution time: minutes: {int((time.time() - start) / 60)} and seconds: {int((time.time() - start) % 60)}')
