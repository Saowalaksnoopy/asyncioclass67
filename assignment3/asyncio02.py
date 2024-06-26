# example of running a coroutine
import asyncio

# Define a coroutine
async def custom_coro():
    # Await another coroutine
    await asyncio.sleep(1)
    print("Custom coroutine completed")

# Main coroutine
async def main():
    # Execute my custom coroutine
    await custom_coro()

# Start the coroutine program
asyncio.run(main())

