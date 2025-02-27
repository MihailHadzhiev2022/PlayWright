import pytest
from playwright.async_api import async_playwright

@pytest.fixture(scope="function", autouse=True)
async def setup_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        new_context = await browser.new_context()
        page = await new_context.new_page()
        await page.goto("https://www.investor.bg/")
        yield page
        await browser.close()
