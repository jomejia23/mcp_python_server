from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.page.set_viewport_size({"width": 1920, "height": 1080})

def after_scenario(context, scenario):
    context.page.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()