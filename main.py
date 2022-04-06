from Facade import Facade
import time

start = time.time()

x = Facade()
x.start_crawling()

print(f'execution time: minutes: {int((time.time() - start) / 60)} and seconds: {int((time.time() - start) % 60)}')
