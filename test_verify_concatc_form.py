import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_verify_contact(page: Page):
    contact = page.locator('a[href="//www.investor.bg/p/contacts/"]', has_text="Контакти")
    await expect(contact).to_be_visible()
