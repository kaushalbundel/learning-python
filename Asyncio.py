import asyncio

# function that prints one wait for sometime and then prints two
# notice the async and await use which is similar what is done in js code, ie. await is used only with async
async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() -s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")
'''
result:
one
one
one
two
two
two
/home/kaushalbundel/01-programming/python/asyncIO/Asyncio.py executed in 1.05 seconds
'''
