import random
from queue import Queue
class page_ganerator:
    def __init__(self):
        print(' Generatoe został uruchomiony')
    def make_random_pages(self, liczba_stron,liczba_wymian):#generuje num sron
        self.pages_queue = Queue(maxsize=liczba_wymian)

        for i in range(liczba_wymian):
            val = random.randint(0, liczba_stron)

            self.pages_queue.put(val)

        return self.pages_queue
