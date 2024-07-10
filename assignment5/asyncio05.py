import asyncio
from random import random  # Correctly import the random function

# Coroutine to prepare rice
async def rice():
    # Simulate cooking time
    cook_time = 1 + random()
    await asyncio.sleep(cook_time)
    print(f'(Rice) : cooking {cook_time} seconds.....')
    return f'Rice is  : completed' 

# Coroutine to prepare noodle
async def noodle():
    # Simulate cooking time
    cook_time = 1 + random()
    await asyncio.sleep(cook_time)
    print(f'(Noodle) : cooking {cook_time} seconds.....')
    return f'Noodle is  : completed' 

# Coroutine to prepare curry
async def curry():
    # Simulate cooking time
    cook_time = 1 + random()
    await asyncio.sleep(cook_time)
    print(f'(Curry) : cooking {cook_time} seconds......')
    return f'Curry is  : completed' 

# Main coroutine
async def main():
    # Create tasks for each dish
    tasks = [
        asyncio.create_task(rice()),
        asyncio.create_task(noodle()),
        asyncio.create_task(curry())
    ]
    
        # Wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    # Get the first completed task
    first_completed_task = done.pop()
    print(first_completed_task.result())  # Print the result of the first completed task

# Run the main coroutine
asyncio.run(main())

