import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_main_navigation():
    # Start Playwright and create the necessary context and page.
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the website.
        await page.goto("https://www.investor.bg/")

        # Click the 'Ок, продължи' button
        ok_button = page.locator("button", has_text="Ок, продължи")
        await ok_button.click()

        # Click the menu toggle
        menu_item = page.locator("#menu-toggle")
        await menu_item.click()


        await browser.close()
