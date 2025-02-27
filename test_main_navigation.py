from playwright.async_api import Page, expect
import pytest


@pytest.mark.asyncio
async def test_main_navigation(page: Page):
    # Click the first menu item
    ok_button = page.locator("button", has_text="Ок, продължи")
    await ok_button.wait_for()
    await ok_button.click()

    menu_item = page.locator("#menu-toggle")
    await menu_item.click()
    #tststts

    first_item = page.locator('a', has_text="Начало")
    await first_item.click()
    first_item = page.locator('a', has_text="Начало")
    await first_item.click()

    # Use expect for assertion (async version of assert)
    await expect(page).to_have_url("https://www.investor.bg/")
