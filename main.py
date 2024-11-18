import time
import os

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory":f"{os.getcwd()}/downloads"
}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chrome_options,service=service)

driver.get(url="")

time.sleep(3)
print("done")