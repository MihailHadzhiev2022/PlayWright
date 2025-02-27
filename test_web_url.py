from playwright.sync_api import Page

def test_web_url(page:Page):
    page.goto("https://www.investor.bg/")

    hreche = page.locator('.responsive-scroll', has_text="Темите днес:")
    assert hreche.is_visible()