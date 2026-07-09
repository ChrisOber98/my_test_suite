import pytest

from config import LOGIN_PAGE_URL, PASSWORD, STANDARD_USER, PRODUCT_PAGE_URL
from playwright.sync_api import Page, expect

@pytest.fixture
def logged_in_page(page: Page):
    """
    Logs in as standard_user and returns the page on the inventory screen.
    """

    page.goto(LOGIN_PAGE_URL)

    page.locator('[data-test="username"]').fill(STANDARD_USER)
    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url(PRODUCT_PAGE_URL)

    return page