
import json

from playwright.sync_api import sync_playwright
import pytest


capabilities = {
    'browserName': 'Chrome',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 150,
    'LT:Options': {
        'platform': 'Windows 10',
        'build': 'Playwright Python Build',
        'name': 'Playwright Python Test',
        'user':'nikithathripuram',
        'accessKey': 'LT_mdwSuSZ2SrRa7ZX9fI8nFWpCeXDK0COkVnrNl5pQGL8Wcuo',
        'network': True,
        'video': True,
        'console': True
    }
}

@pytest.mark.av
def test_geoLocations():
    with sync_playwright() as p:
        browser = p.chromium.connect(f"wss://cdp.lambdatest.com/playwright?capabilities={json.dumps(capabilities)}")
        context = browser.new_context(geolocation={"latitude":36.7783,"longitude":-119.4179}, permissions=["geolocation"])
        page = context.new_page()
        page.goto("https://browserleaks.com/geo")
        page.wait_for_timeout(13000)