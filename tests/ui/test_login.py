from playwright.sync_api import Page, expect

def test_login_fails_with_incorrect_password(page: Page):
    """
    TC-001 | Priority: High
    Verifies: wrong password shows exact error message and no redirect occurs.
    Risk: unauthorized access with bad credentials, and unclear login feedback.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto('https://www.saucedemo.com/')

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("wrong_password")
    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")
    expect(page).to_have_url('https://www.saucedemo.com/')