from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given('I am on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate_to('https://www.saucedemo.com/')

@when('I enter valid credentials and click login')
def step_impl(context):
    context.login_page.login('standard_user', 'secret_sauce')

@then('I should be redirected to the inventory page')
def step_impl(context):
    assert 'inventory.html' in context.page.url

@then('I should not see any error messages')
def step_impl(context):
    assert not context.login_page.has_error_message()

@then('the inventory page should be displayed successfully')
def step_impl(context):
    context.inventory_page = InventoryPage(context.page)
    assert context.inventory_page.is_inventory_displayed()

@given('I am logged in to the application')
def step_impl(context):
    context.execute_steps('''
        Given I am on the login page
        When I enter valid credentials and click login
        Then I should be redirected to the inventory page
    ''')
    context.inventory_page = InventoryPage(context.page)

@when('I click the logout button from the hamburger menu')
def step_impl(context):
    context.inventory_page.logout()

@then('I should be redirected to the login page')
def step_impl(context):
    assert context.page.url.endswith('/index.html')

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@when('I click the login button')
def step_impl(context):
    context.page.click('[data-test="login-button"]')

@then('I should remain on the login screen')
def step_impl(context):
    assert context.page.url.endswith('/index.html')

@then('I should see the error message "{message}"')
def step_impl(context, message):
    error_message = context.login_page.get_error_message()
    assert message in error_message

@then('the error message should have a red background')
def step_impl(context):
    error_element = context.page.locator('[data-test="error"]')
    background_color = error_element.evaluate('el => window.getComputedStyle(el).backgroundColor')
    assert 'rgb(226, 35, 26)' in background_color