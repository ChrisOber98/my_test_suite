from playwright.sync_api import Page, expect

def test_add_item_to_cart(logged_in_page: Page):
    """
    TC-007 | Priority: High
    Verifies: User is able to correctly add item to cart & is properly notified
    Risk: users not being able to add items to cart / not being notified.
    Spec: test-cases/saucedemo-test-cases.md
    """

    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]').click()
    
    expect(logged_in_page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")
    expect(logged_in_page.locator('[data-test="remove-sauce-labs-backpack"]')).to_have_text("Remove")
    
