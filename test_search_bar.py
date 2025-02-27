from playwright.async_api import Page, expect
import pytest

@pytest.mark.asyncio
async def test_search_bar_visible(page: Page):
    search_bar = page.locator('#search-icon')
    await expect(search_bar).to_be_visible()
