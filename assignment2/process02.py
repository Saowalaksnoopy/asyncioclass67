# Multiprocessing 2 kitchens, 2 cookers, 2 dishes
# share resources
import multiprocessing
import os
from time import sleep, ctime, time

# Basket of sharing
class Basket:
    def __init__(self):
        self.eggs = 50
        self.lock = multiprocessing.Lock()
    
    def use_eggs(self, index):
        with self.lock:
            print(f'{ctime()} Kitchen-{index} : Chef-{index} has lock with eggs remaining {self.eggs}')
            self.eggs -= 1
            print(f'{ctime()} Kitchen-{index} : Chef-{index} has released lock with eggs remaining {self.eggs}')

# Chef cooking
def cooking(index, basket):
    # Chef use eggs for cooking
    basket.use_eggs(index)
    sleep(2)

# Kitchen cooking
def kitchen(index, shared_basket):
    print(f'{ctime()} Kitchen-{index} : Begin cooking...PID {os.getpid()}')
    cooking_time = time()
    cooking(index, shared_basket)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen-{index} : Cooking done in {duration:0.2f} seconds!')

if __name__ == "__main__":
    # Begin of main thread
    print(f'{ctime()} Main : Start Cooking...PID {os.getpid()}')
    start_time = time()

    basket = Basket()

    # Multi processes
    kitchens = list()
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index, basket))
        kitchens.append(p)
        # starting processes
        p.start()

    for index, p in enumerate(kitchens):
        # wait until processes are finished
        p.join()

    print(f'{ctime()} Main : Basket eggs remaining {basket.eggs}')
    duration = time() - start_time
    print(f'{ctime()} Main : Finished Cooking duration in {duration:0.2f} seconds')
