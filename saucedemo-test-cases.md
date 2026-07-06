# SauceDemo Test Cases

## TC-001: Login fails with incorrect password

**Priority:** High

**Preconditions:**
- User is on the login page (https://www.saucedemo.com)
- User is not already logged in

**Steps:**
1. Enter `standard_user` in the Username field
2. Enter `wrong_password` in the Password field
3. Click the Login button

**Expected Result:**
- User remains on the login page (no redirect to inventory)
- Error message is displayed: "Epic sadface: Username and password do not match any user in this service"
- Error message appears with the error styling/icon

**Risk it protects against:** Unauthorized users gaining access with bad
credentials, and users being confused by missing/unclear error feedback.

## TC-002: Login fails with locked out user

**Priority:** High

**Preconditions:**
- User is on the login page (https://www.saucedemo.com)
- User is not already logged in

**Steps:**
1. Enter `locked_out_user` in the username field
2. Enter `secret_sauce` in the password field
3. Click the login button

**Expected Result:**
- User remains on the login page (no redirect to inventory)
- Error message is displayed: "Epic sadface: Sorry, this user has been locked out."

**Risk it protects against:** Unauthorized users gaining access with locked out accounts, and users
being confused by missing/unclear error feedback.

## TC-003: Login fails with no username and password entered

**Priority:** Low

**Preconditions:**
- User must be on login page (https://www.saucedemo.com)
- User must not be logged in

**Steps:**
1. Ensure username and password field are empty
2. Click login button

**Expected Result:**
- User remains on the login page (no redirect to inventory)
- Error message is displayed: "Epic sadface: Username is required"

**Risk it protects against:** Users being confused by missing/unclear error feedback.

## TC-004: Login fails with no password entered

**Priority:** Low

**Preconditions:**
- User must be on login page (https://www.saucedemo.com)
- User must not be logged in

**Steps:**
1. Enter `standard_user` into username field
2. Click login button

**Expected Result:**
- User remains on the login page (no redirect to inventory)
- Error message is displayed: "Epic sadface: Password is required"

**Risk it protects against:** Users being confused by missing/unclear error feedback.

## TC-005: Login fails with no username entered

**Priority:** Low

**Preconditions:**
- User must be on login page (https://www.saucedemo.com)
- User must not be logged in

**Steps:**
1. Enter `secret_sauce` into password field
2. Click login button

**Expected Result:**
- User remains on the login page (no redirect to inventory)
- Error message is displayed: "Epic sadface: Username is required"

**Risk it protects against:** Users being confused by missing/unclear error feedback.

## TC-006: Login succeeds with valid login credentials

**Priority:** High

**Preconditions:**
- User must be on login page (https://www.saucedemo.com)
- User must not be logged in

**Steps:**
1. Enter `standard_user` into username field
2. Enter `secret_sauce` into password field
3. Click login button

**Expected Result:**
- User redirects to product page (https://www.saucedemo.com/inventory.html)

**Risk it protects against:** Users not being able to correctly log into authorized accounts with valid
credentials.

## TC-007: Add item to cart

**Priority:** High

**Preconditions:**
- User must be on product page (https://www.saucedemo.com/inventory.html)
- User must be logged in

**Steps:**
1. Click add to cart button on Sauce Labs Backpack field

**Expected Result:**
- User should be notified in the top right corner with a red circle with a 1.
- Add to cart button should change to remove button

**Risk it protects against:** Users not being able to correctly add items to cart, and being incorrectly notified that an item has been added from the product page

## TC-008: Remove item from cart

**Priority:** High

**Preconditions:**
- User must be on product page (https://www.saucedemo.com/inventory.html)
- User must be logged in
- User must have 1x Sauce Labs Backpack in cart

**Steps:**
1. Click remove button on Sauce Labs Backpack field

**Expected Result:**
- User should see in the top right corner a red circle with a 1 be removed
- Remove button should change to add to cart button

**Risk it protects against:** Users not being able to correctly remove items from cart, and being incorrectly notified that an item has been removed from the product page

## TC-009: Successfully get thank you screen on checkout of an item

**Priority:** High

**Preconditions:**
- User must be on product page (https://www.saucedemo.com/inventory.html)
- User must be logged in
- User must have an empty cart

**Steps:**
1. Click Add to cart button on Sauce Labs Backpack field
2. Click shopping cart icon in top right of screen
3. Click checkout button
4. Enter `tim` into First Name field
5. Enter `smith` into Last Name field
6. Enter `123` into zip/postal code field
7. Click continue button
8. Click finish button

**Expected Result:**
- User should be redirected to (https://www.saucedemo.com/checkout-complete.html)
- Page layout should show
    - Checkout: Complete!
    - Thank you for your order! Your order has been dispatched, and will arrive just as fast as the pony can get there!

**Risk it protects against:** Users not being prompted on a successful purchase leaving users confused about their order status and if more steps are needed.

## TC-010: Successfully get correct overview on checkout of an item

**Priority:** Medium

**Preconditions:**
- User must be on product page (https://www.saucedemo.com/inventory.html)
- User must be logged in
- User must have an empty cart

**Steps:**
1. Click Add to cart button on Sauce Labs Backpack field
2. Click shopping cart icon in top right of screen
3. Click checkout button
4. Enter `tim` into First Name field
5. Enter `smith` into Last Name field
6. Enter `123` into zip/postal code field
7. Click continue button

**Expected Result:**
- User should be redirected to (https://www.saucedemo.com/checkout-step-two.html)
- Page layout should show
    - Checkout: Overview
    - 1x sauce labs backpack for 29.99
    - Payment Information: SauceCard #31337
    - Shipping Information: Free Pony Express Delivery!
    - Price Total Item total: $29.99 Tax: $2.40
    - Total: $32.39

**Risk it protects against:** Users not being shown a correct order overview leaving users confused about their order status.

## TC-011: Fail to checkout with no first name entered

**Priority:** Medium

**Preconditions:**
- User must be on checkout page (https://www.saucedemo.com/checkout-step-one.html)
- User must be logged in

**Steps:**
1. Enter `smith` into Last Name field
2. Enter `123` into zip/postal code field
3. Click continue button

**Expected Result:**
- User stays on checkout page (https://www.saucedemo.com/checkout-step-one.html)
- User is prompted with error message: "Error: First Name is required"

**Risk it protects against:** Users being confused by missing/unclear error feedback, and orders being submitted with incomplete customer information.

## TC-012: Fail to checkout with no last name entered

**Priority:** Medium

**Preconditions:**
- User must be on checkout page (https://www.saucedemo.com/checkout-step-one.html)
- User must be logged in

**Steps:**
1. Enter `tim` into First Name field
2. Enter `123` into zip/postal code field
3. Click continue button

**Expected Result:**
- User stays on checkout page (https://www.saucedemo.com/checkout-step-one.html)
- User is prompted with error message: "Error: Last Name is required"

**Risk it protects against:** Users being confused by missing/unclear error feedback, and orders being submitted with incomplete customer information.

## TC-013: Fail to checkout with no zip code entered

**Priority:** Medium

**Preconditions:**
- User must be on checkout page (https://www.saucedemo.com/checkout-step-one.html)
- User must be logged in

**Steps:**
1. Enter `tim` into First Name field
2. Enter `smith` into last name field
3. Click continue button

**Expected Result:**
- User stays on checkout page (https://www.saucedemo.com/checkout-step-one.html)
- User is prompted with error message: "Error: Postal Code is required"

**Risk it protects against:** Users being confused by missing/unclear error feedback, and orders being submitted with incomplete customer information.

## TC-014: Sorting items from Z-A correctly sorts

**Priority:** Medium

**Preconditions:**
- User must be on product page (https://www.saucedemo.com/inventory.html)
- User must be logged in
- Sorting must be currently set to (Name A to Z)

**Steps:**
1. Click sorting button (Name A to Z) and change to (Name Z to A)

**Expected Result:**
- User stays on product page (https://www.saucedemo.com/inventory.html)
- Products are sorted in this order:
    1. Test.allTheThings() T-Shirt (Red)
    2. Sauce Labs Onesie
    3. Sauce Labs Fleece Jacket
    4. Sauce Labs Bolt T-Shirt
    5. Sauce Labs Bike Light
    6. Sauce Labs Backpack

**Risk it protects against:** Users being presented incorrect sorting information.

## TC-015: User is correctly logged out

**Priority:** High

**Preconditions:**
- User must be on product page (https://www.saucedemo.com/inventory.html)
- User must be logged in

**Steps:**
1. Click 3 lines in top left corner
2. Select log out
3. Attempt to navigate directly to https://www.saucedemo.com/inventory.html

**Expected Result:**
- After step 2, user is redirected to login page (https://www.saucedemo.com)
- After step 3, access is blocked and user remains on the login page
- Error message is displayed: "Epic sadface: You can only access '/inventory.html' when you are logged in."

**Risk it protects against:** Users not being able to log out of accounts, or sessions remaining active after logout, leaving account information unprotected.