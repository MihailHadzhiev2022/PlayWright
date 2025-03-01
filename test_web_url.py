import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_web_url():
    # Start Playwright and create the necessary context and page.
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the website.
        await page.goto("https://www.investor.bg/")

        # Locate the element with the text "Темите днес:" and verify it is visible.
        hreche = page.locator('.responsive-scroll', has_text="Темите днес:")
        await expect(hreche).to_be_visible()

        # Clean up and close the browser after the test
        await browser.close()
