from playwright.sync_api import Page, expect
from config import (
    LOGIN_PAGE_URL, 
    PRODUCT_PAGE_URL, 
    STANDARD_USER, 
    PASSWORD, 
    WRONG_PASSWORD, 
    ERROR_USERNAME_PASSWORD, 
    ERROR_LOCKED_OUT_USER,
    LOCKED_OUT_USER, 
    ERROR_USERNAME,
    ERROR_PASSWORD
)

def test_login_fails_with_incorrect_password(page: Page):
    """
    TC-001 | Priority: High
    Verifies: wrong password shows exact error message and no redirect occurs.
    Risk: unauthorized access with bad credentials, and unclear login feedback.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto(LOGIN_PAGE_URL)

    page.locator('[data-test="username"]').fill(STANDARD_USER)
    page.locator('[data-test="password"]').fill(WRONG_PASSWORD)
    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text(ERROR_USERNAME_PASSWORD)
    expect(page).to_have_url(LOGIN_PAGE_URL)

def test_login_fails_with_locked_out_user(page: Page):
    """
    TC-002 | Priority: High
    Verifies: locked out user is not able to log in and recieves correct error
    message
    Risk: Lockedout users have access to website.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto(LOGIN_PAGE_URL)

    page.locator('[data-test="username"]').fill(LOCKED_OUT_USER)
    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text(ERROR_LOCKED_OUT_USER)
    expect(page).to_have_url(LOGIN_PAGE_URL)

def test_login_fails_with_no_username_and_password_entered(page: Page):
    """
    TC-003 | Priority: low
    Verifies: no password and username shows exact error message and no redirect occurs.
    Risk: unauthorized access with bad credentials, and unclear login feedback.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto(LOGIN_PAGE_URL)

    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text(ERROR_USERNAME)
    expect(page).to_have_url(LOGIN_PAGE_URL)

def test_login_fails_with_no_password_entered(page: Page):
    """
    TC-004 | Priority: low
    Verifies: no password shows exact error message and no redirect occurs.
    Risk: unauthorized access with bad credentials, and unclear login feedback.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto(LOGIN_PAGE_URL)

    page.locator('[data-test="username"]').fill(STANDARD_USER)
    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text(ERROR_PASSWORD)
    expect(page).to_have_url(LOGIN_PAGE_URL)

def test_login_fails_with_no_username_entered(page: Page):
    """
    TC-005 | Priority: low
    Verifies: no username shows exact error message and no redirect occurs.
    Risk: unauthorized access with bad credentials, and unclear login feedback.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto(LOGIN_PAGE_URL)

    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text(ERROR_USERNAME)
    expect(page).to_have_url(LOGIN_PAGE_URL)

def test_login_succeeds_with_valid_login_credentials(page: Page):
    """
    TC-006 | Priority: High
    Verifies: valid login credentials allow access to the website.
    Risk: users not being able to access their accounts.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto(LOGIN_PAGE_URL)

    page.locator('[data-test="username"]').fill(STANDARD_USER)
    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()
    
    expect(page).to_have_url(PRODUCT_PAGE_URL) 