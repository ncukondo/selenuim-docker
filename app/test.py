from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

"""
Use the Chrome DriverService.
https://chromedriver.chromium.org/getting-started
"""
class StartScrape():
    def __enter__(self):
        self.chrome_path = '/usr/bin/chromium-browser'
        self.chromedriver_path = '/usr/lib/chromium/chromedriver'
        self.o = Options()
        self.o.binary_location = '/usr/bin/chromium-browser'
        self.o.add_argument('--headless')
        self.o.add_argument('--disable-gpu')
        self.o.add_argument('--no-sandbox')
        self.o.add_argument('--window-size=1200x600')
        self.s = Service(executable_path=self.chromedriver_path)
        self.s.start()
        self.driver = webdriver.Remote(
            self.s.service_url,
            desired_capabilities=self.o.to_capabilities()
        )
        return self.driver

    def __exit__(self, exception_type, exception_value, traceback):
        self.driver.quit()


def screenShotFull(driver, filename, timeout=30):
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    driver.save_screenshot(filename)

with StartScrape() as driver:
    driver.get("https://www.google.com/")
    screenShotFull(driver,'./data/sample.png')
    print(driver.title)
