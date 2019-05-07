import time
import unittest
from selenium import webdriver
from selenium import 
from _elementtree import Element

#invoke new firefox Instance
ff_driver = webdriver.Firefox()

# Wait time of 30 sec to find Element
ff_driver.implicitly_wait(30)
ff_driver.maximize_window()

# Open the required page
ff_driver.get("http://www.lambdatest.com")
    
# Sleep time of 10 seconds
time.sleep(10)

# Close the Browser
ff_driver.close()
