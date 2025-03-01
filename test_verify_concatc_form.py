import pytest
from playwright.async_api import async_playwright, Page, expect

@pytest.mark.asyncio
async def test_verify_contact():
    # Start Playwright and create the necessary context and page.
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the website.
        await page.goto("https://www.investor.bg/")

        # Locate the contact link and verify if it's visible.
        contact = page.locator('a[href="//www.investor.bg/p/contacts/"]', has_text="Контакти")
        await expect(contact).to_be_visible()

        # Clean up and close the browser after the test.
        await browser.close()
