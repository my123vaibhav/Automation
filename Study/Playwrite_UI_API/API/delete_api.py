#Sync Version – DELETE
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    request_context = p.request.new_context(
        extra_http_headers={
            "x-api-key": "reqres-free-v1",
            "Content-Type": "application/json"
        }
    )
    response = request_context.delete("https://reqres.in/api/users/2")
    print("Status Code:", response.status)   # usually 204 (No Content)
    print("URL:", response.url)
    print("Response Text:", response.text()) # delete may return empty body
    request_context.dispose()
#Async Version – DELETE
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
        response = await request_context.delete("https://reqres.in/api/users/2")
        print("Status Code:", response.status)   # usually 204
        print("URL:", response.url)
        print("Response Text:", await response.text())
        await request_context.dispose()
asyncio.run(main())
