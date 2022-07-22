'''
main.py

Uses selenium firefox driver in headless mode to login and authorize access. 
'''
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("IITM_USERNAME")
password = os.getenv("IITM_PASSWORD")

options = Options()
options.add_argument("--headless")

# Step 1: Login Page
browser = webdriver.Firefox(options=options)
browser.get("https://netaccess.iitm.ac.in/account/login")

ele_usr = browser.find_element(By.ID, "username")
ele_pwd = browser.find_element(By.ID, "password")
ele_login_btn = browser.find_element(By.ID, "submit")

ele_usr.send_keys(username)
ele_pwd.send_keys(password)
ele_login_btn.click()

# Step 2: Redirect from Index Page to Approve Page.
assert browser.current_url == "https://netaccess.iitm.ac.in/account/index"
browser.get("https://netaccess.iitm.ac.in/account/approve")

# Step 3: Approve your device
ele_radio = browser.find_element(By.ID, "radios-1")
ele_radio.click()

ele_auth_btn = browser.find_element(By.ID, "approveBtn")
ele_auth_btn.click()

# Step 4: Validate that you're back at the index.
assert browser.current_url == "https://netaccess.iitm.ac.in/account/index"
