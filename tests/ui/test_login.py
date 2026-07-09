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

def test_login_fails_with_locked_out_user(page: Page):
    """
    TC-002 | Priority: High
    Verifies: locked out user is not able to log in and recieves correct error
    message
    Risk: Lockedout users have access to website.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto('https://www.saucedemo.com/')

    page.locator('[data-test="username"]').fill("locked_out_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    expect(page).to_have_url('https://www.saucedemo.com/')

def test_login_fails_with_no_username_and_password_entered(page: Page):
    """
    TC-003 | Priority: low
    Verifies: no password and username shows exact error message and no redirect occurs.
    Risk: unauthorized access with bad credentials, and unclear login feedback.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto('https://www.saucedemo.com/')

    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url('https://www.saucedemo.com/')

def test_login_fails_with_no_password_entered(page: Page):
    """
    TC-004 | Priority: low
    Verifies: no password shows exact error message and no redirect occurs.
    Risk: unauthorized access with bad credentials, and unclear login feedback.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto('https://www.saucedemo.com/')

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Password is required")
    expect(page).to_have_url('https://www.saucedemo.com/')

def test_login_fails_with_no_username_entered(page: Page):
    """
    TC-005 | Priority: low
    Verifies: no username shows exact error message and no redirect occurs.
    Risk: unauthorized access with bad credentials, and unclear login feedback.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto('https://www.saucedemo.com/')

    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url('https://www.saucedemo.com/')

def test_login_succeeds_with_valid_login_credentials(page: Page):
    """
    TC-006 | Priority: High
    Verifies: valid login credentials allow access to the website.
    Risk: users not being able to access their accounts.
    Spec: test-cases/saucedemo-test-cases.md
    """

    page.goto('https://www.saucedemo.com/')

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')  