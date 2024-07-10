# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee(): #1
    print("coffee: prepare ingridients")
    sleep(1) #Run then stop 1 sec
    print("coffee: waiting...")
    await asyncio.sleep(5) #2: pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs(): #1
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)#2: pause, another tasks can be run
    print("eggs: ready")

async def main(): #1
    start = time()
    coffe_task = asyncio.create_task(make_coffee()) #scheule execution (create task from coroutine object)
    egg_task = asyncio.create_task(fry_eggs())#scheule execution
    #wait for completion, both task are schedule for execution already
    await coffe_task #run task with await
    await egg_task
    print(f"breakfast is ready in {time()-start} min")


asyncio.run(main()) #run top-level function concurrenytly