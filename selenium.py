#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 07:59:24 2018

@author: kash-py
"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup





#PROXY = '5.178.214.163:8080'

#options to make selenium headless or us it with proxy
#options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')  # Last I checked this was necessary.
#options.add_argument('--proxy-server=%s' % PROXY)
#driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
#browser = webdriver.Chrome(chrome_options=options) #use this line with options

browser = webdriver.Chrome()


browser.get('https://www.facebook.com')




