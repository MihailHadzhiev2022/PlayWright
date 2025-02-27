from playwright.sync_api import Page

def test_search_bar_visible(page: Page):
    page.goto("https://www.investor.bg/")

    search_bar = page.locator('#search-icon')
    assert search_bar.is_visible()
