from playwright.sync_api import Page

def test_main_navigation(page: Page):
    page.goto("https://www.investor.bg/")
    # Click the first menu item
    ok_button = page.locator("button", has_text="Ок, продължи")
    ok_button.wait_for()
    ok_button.click()

    menu_item = page.locator("#menu-toggle")
    menu_item.click()
    first_idem = page.locator('a', has_text="Начало")
    first_idem.click()
    assert page.url == "https://www.investor.bg/"
