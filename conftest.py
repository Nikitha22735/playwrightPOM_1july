import allure
from playwright.sync_api import sync_playwright, expect
import pytest

# @pytest.fixture()
# def page():
#     with sync_playwright() as p:
#             browser = p.chromium.launch()
#             context = browser.new_context()
#             page = context.new_page()
#             yield
#             page.close()

@pytest.fixture()
def navigateToAmazon(page):
    page.goto("https://www.amazon.in/") 

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page")
        # page.screenshot()
        if page:
            allure.attach(page.screenshot(), 
                          name="failedpage", 
                          attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="session", autouse=True)
def cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()     
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.get_by_role("textbox", name="Username").fill("Admin")
        page.get_by_role("textbox", name="Password").fill("admin123")
        page.get_by_role("button", name="Login").click()
        page.wait_for_timeout(2000)
        context.storage_state(path="testData\\cookies.json")

@pytest.fixture(scope="function")
def page():
     with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state="testData\\cookies.json")
            page = context.new_page() 
            yield page    


