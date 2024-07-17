import asyncio

#define an asynchronous iterrator
class AsyncIterator:

    #constructor, define some data
    def __init__(self):
        self.counter = 0
    
    #create an instance of the iterator
    def __aiter__(self):
        return self
    
    #return the next awaitable
    async def __anext__(self):
        #check for no further items
        if self.counter >= 10:
            raise StopAsyncIteration
        #increment the counter 
        self.counter += 1
        #simulate work
        await asyncio.sleep(1)
        #return the counter value
        return self.counter
    
#main coroutine
async def main():
    #loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(item)

#Running the async main function
asyncio.run(main())

