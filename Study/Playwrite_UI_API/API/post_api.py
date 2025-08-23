from playwright.sync_api import sync_playwright
#Sync Version (with headers & JSON body)
with sync_playwright() as p:
    request_context = p.request.new_context(
        extra_http_headers={
            "x-api-key": "reqres-free-v1",
            "Content-Type": "application/json"
        }
    )
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = request_context.post(
        "https://reqres.in/api/users",
        data=payload  # Playwright automatically sends JSON if Content-Type is set
    )
    print("Status Code:", response.status)
    print("URL:", response.url)
    print("Response JSON:", response.json())
    request_context.dispose()
#Async Version
import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        request_context = await p.request.new_context(
            extra_http_headers={
                "x-api-key": "reqres-free-v1",
                "Content-Type": "application/json"
            }
        )
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = await request_context.post(
            "https://reqres.in/api/users",
            data=payload
        )
        print("Status Code:", response.status)
        print("URL:", response.url)
        print("Response JSON:", await response.json())
        await request_context.dispose()
asyncio.run(main())

