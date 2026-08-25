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


# pip install pillow
from PIL import Image, ImageChops

def test_visualregression():
    with Image.open("screenshots\\ss1.png") as img1:
        with Image.open("screenshots\\ss2_2026-08-24_22_00_51_474755.png") as img2:
            diff = ImageChops.difference(img1, img2)
            diff.save("screenshots\\visual_diff.png")
            print(diff.getbbox())




def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="testData\\cookies.json")
        page = context.new_page()     
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_timeout(10000)
        # page.get_by_role("textbox", name="Username").fill("Admin")
        # page.get_by_role("textbox", name="Password").fill("admin123")
        # page.get_by_role("button", name="Login").click()
        # page.wait_for_timeout(2000)
        # context.storage_state(path="testData\\cookies.json")



