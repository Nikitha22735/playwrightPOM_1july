from playwright.sync_api import sync_playwright
import pytest
from datetime import datetime

# @pytest.mark.av
def test_dimensions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width":600,"height":300})
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)



# @pytest.mark.av
def test_mobile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # print(**p.devices["iPhone XR"])
        context = browser.new_context(**p.devices["iPhone XR"])
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)

# @pytest.mark.av
def test_geoLocations():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(geolocation={"latitude":36.7783,"longitude":-119.4179}, permissions=["geolocation"])
        page = context.new_page()
        page.goto("https://browserleaks.com/geo")
        page.wait_for_timeout(13000)



def test_netWorkmocking():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(geolocation={"latitude":36.7783,"longitude":-119.4179}, permissions=["geolocation"])
        page = context.new_page()        
        page.goto("https://testautomationpractice.blogspot.com/")
        context.set_offline(True)
        page.wait_for_timeout(5000)
        context.set_offline(False)
        page.wait_for_timeout(13000)

@pytest.mark.av
def test_screenshots():
     with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()        
            page.goto("https://testautomationpractice.blogspot.com/")
            time = datetime.now()
            time = str(time)
            time = time.replace(" ","_").replace(":","_").replace(".","_")
            # time = time.replace(":","_")
            # time = time.replace(".","_")
            print(time)
            # page.screenshot(path=f"screenshots/ss2_{time}.png", full_page=True)
            page.locator("button.start").screenshot(path=f"screenshots/ss2_{time}.png")


