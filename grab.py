#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
import config
import sys

driver = webdriver.PhantomJS("./phantomjs")
driver.set_window_size(1024,768)

driver.get('https://czds.icann.org/en')

#log in
userF = driver.find_element_by_id("edit-name")
userF.send_keys(config.username)
passF = driver.find_element_by_id("edit-pass")
passF.send_keys(config.password)
time.sleep(0.1)
#submit
submitF = driver.find_element_by_id("edit-submit")
submitF.click()

#request page
time.sleep(0.1)
driver.get('https://czds.icann.org/en/request/add')
time.sleep(0.1)
#select zones
approvedF = driver.find_element_by_id("tld-filter-approved")
approvedF.click()
pendingF = driver.find_element_by_id("tld-filter-pending")
pendingF.click()
time.sleep(0.1)
allF = driver.find_element_by_id("edit-tlds-fieldset-tld-all")
if not allF.is_enabled():
    #no zones to request
    sys.exit()
allF.click()
#enter reason
reasonF = driver.find_element_by_id("edit-reason")
reasonF.send_keys(config.request_message)
time.sleep(0.1)

#next form page
nextF = driver.find_element_by_id("edit-next1")
nextF.click()
time.sleep(0.1)

#agree to terms
termsF = driver.find_element_by_id("edit-agree-tc")
termsF.click()
#next form page
nextF = driver.find_element_by_id("edit-next2")
nextF.click()
time.sleep(0.1)

#empty ip field
ipF = driver.find_element_by_id("edit-ips-from-request-ip-0")
ipF.clear()
time.sleep(0.1)
#submit
requestBF = driver.find_element_by_id("edit-submit")
requestBF.click()
time.sleep(0.1)

#TODO add success check
driver.quit()

