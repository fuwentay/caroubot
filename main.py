# TODO: Iterate for different items. Select name and brand based on image name.
# TODO: Generate caption and description based on image and pipe it to the function

# Import libraries
import boto3
import os
import pandas as pd
import shutil
import time

from dotenv import load_dotenv
from queue import Queue
from selenium import webdriver
from selenium.webdriver.common.by import By
from tempfile import mkdtemp

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Load API Keys
load_dotenv()

# To click on the element based on the given xpath
def click_element_by_xpath(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()
    # Add a short delay to allow the page to load
    time.sleep(3)

# To list all the file names in the folder
def list_filenames():
    to_list_photos = [
    file for file in os.listdir("C:/Users/fuwen/OneDrive - NUS High School/Documents/Projects/carousell/to list/")
    ]
    return to_list_photos

# list_filenames()

# To extract title, brand & price from file name
def extract_info(filename):
    info = filename.split(".")[0]
    [title, brand, price] = info.split(";")
    return [title, brand, price]

# extract_info(list_filenames()[0])

# To shift file from "to list" to "listed" after it has been uploaded
def shift_file():
    file_path = "C:/Users/fuwen/OneDrive - NUS High School/Documents/Projects/carousell/to list/" + list_filenames()[0]
    new_file_path = "C:/Users/fuwen/OneDrive - NUS High School/Documents/Projects/carousell/listed/"
    shutil.move(file_path, new_file_path)

# shift_file()

# Automate the login process. It is defined as a stand-alone function to be called when force logged out
def login(driver):
    driver.get("https://www.carousell.sg/sell/")
    driver.maximize_window()

    # To delay the next step. if there is no delay, the chrome driver would not have enough time to load the element.
    # Thus, an exception would be raised (NoSuchElementException), breaking the script. In this case, we don't use error handling (try; except) because a simple 
    # time.sleep() would suffice. There will be more examples of error handling below.
    time.sleep(2)
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/header/div/div/div/div[2]/a[2]/p")
    click_element_by_xpath(driver, "/html/body/div[6]/div/div/div/div/div[2]/button[2]")

    actions = ActionChains(driver)
    actions.send_keys(os.environ['CAROUSELL_EMAIL'])
    actions.perform()

    # Slower send_keys to simulate human behaviour
    # for i in os.environ['CAROUSELL_EMAIL']:
    #     actions = ActionChains(driver)
    #     actions.send_keys(i)
    #     actions.perform()
    #     # time.sleep(0.5)

    time.sleep(1)
    
    actions = ActionChains(driver)
    actions.key_down(Keys.TAB)
    actions.perform()

    actions = ActionChains(driver)
    actions.key_up(Keys.TAB)
    actions.perform()

    actions = ActionChains(driver)
    actions.send_keys(os.environ['CAROUSELL_PASSWORD'])
    actions.perform()

    # Slower send_keys to simulate human behaviour
    # for i in os.environ['CAROUSELL_EMAIL']:
    #     actions = ActionChains(driver)
    #     actions.send_keys(i)
    #     actions.perform()
    #     # time.sleep(0.5)

    actions = ActionChains(driver)
    actions.key_down(Keys.ENTER)
    actions.perform()

    actions = ActionChains(driver)
    actions.key_up(Keys.ENTER)
    actions.perform()

    # TODO: try/except to wait till ReCAPTCHA solved
    # Time wait here is to solve ReCAPTCHA
    time.sleep(17)

def sell_listing(driver):
    # Upload images
    path = "C:/Users/fuwen/OneDrive - NUS High School/Documents/Projects/carousell/to list/" + list_filenames()[0]
    # XPATH was taken from element with input tag and type="file"
    select_photos = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div/div[1]/div[1]/div[2]/label/input")
    select_photos.send_keys(path)
    print("path sent successfully")

    time.sleep(3)

    # Select "Category"
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/div/div[1]")

    actions = ActionChains(driver)
    actions.send_keys("men's")
    actions.perform()

    time.sleep(3)

    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/div/div[2]/div[3]")

    # Select "Condition"
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[3]/div[2]/div/div[2]/div/button[3]/span")
    
    # Select "Listing Title"
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[4]/div[2]/div/div/div/input")
    actions = ActionChains(driver)
    # FIXME: ugly can be improved
    actions.send_keys(extract_info(list_filenames()[0])[0])
    actions.perform()

    # Select "Brand"
    # try:
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[4]/div[3]/div/div/div/div/input")

    time.sleep(3)
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[4]/div[3]/div/div[2]/div/div[34]")

    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[4]/div[4]/div/div/div/input")
    actions = ActionChains(driver)
    actions.send_keys(extract_info(list_filenames()[0])[1])
    actions.perform()    

    # Select "Size"
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[4]/div[5]/div/div/div/div/input")
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[4]/div[5]/div/div[2]/div/div[4]/div/div/p")

    # Select "Disable 'Buy' button"
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[5]/div[2]/div/button[2]/p[1]")

    # Select "Meet-up"
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[6]/div[5]/div/label/div/p")
    
    # Select location
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[6]/div[5]/div/div[1]/div/div/div/input")
    actions = ActionChains(driver)
    actions.send_keys("Bishan MRT Interchange")
    actions.perform()

    # Time sleep for dropdown menu to load
    time.sleep(5)

    # Select "Bishan MRT Interchange"
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[6]/div[5]/div/div[1]/div[2]/div/div[2]/div/p[1]")
    print("Selected location successfully.")

    # Close dropdown menu
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[6]/div[5]/div/label/div/p")
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[6]/div[5]/div/label/div/p")

    # Indicate price
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[1]/div[7]/div[3]/div[1]/div/div/input")
    actions = ActionChains(driver)
    actions.send_keys(extract_info(list_filenames()[0])[2])
    actions.perform()

    # Select "List now"
    click_element_by_xpath(driver, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/div[2]/button")
    print("Listed successfully.")

    time.sleep(10)    

while len(list_filenames())>0:
    driver = webdriver.Chrome()
    login(driver)
    # To extract title, brand & price of the first file in the folder. This sets up the parameters for the listing.
    extract_info(list_filenames()[0])
    sell_listing(driver)
    shift_file()