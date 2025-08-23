import time
from playwright.sync_api import sync_playwright
#Sync version
with sync_playwright() as p:
    request_context = p.request.new_context()
    start_time = time.time()
    response = request_context.get("https://reqres.in/api/users?page=2")
    end_time = time.time()

    print("Status Code:", response.status)
    print("URL:", response.url)
    print("Time Taken (seconds):", round(end_time - start_time, 3))
    print("Headers:", response.headers)
    print("Response JSON:", response.json())
    request_context.dispose()

#Async version
import time, asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        request_context = await p.request.new_context()
        start_time = time.time()
        response = await request_context.get("https://reqres.in/api/users?page=2")
        end_time = time.time()
        print("Status Code:", response.status)
        print("URL:", response.url)
        print("Time Taken (seconds):", round(end_time - start_time, 3))
        print("Headers:", response.headers)
        print("Response JSON:", await response.json())

        await request_context.dispose()

asyncio.run(main())

