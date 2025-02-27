from playwright.async_api import Page, expect
import pytest

@pytest.mark.asyncio
async def test_web_url(page: Page):
    hreche = page.locator('.responsive-scroll', has_text="Темите днес:")
    await expect(hreche).to_be_visible()
