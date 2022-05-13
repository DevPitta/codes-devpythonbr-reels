"""
This code uses the selenium
and webdriver-manager libraries
and results in a google search for the keyword.

-> Requirements:
    . pip install selenium
    . pip install webdriver-manager
"""

from selenium.webdriver import Firefox 
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

browser = Firefox(executable_path=GeckoDriverManager().install())

browser.get('https://www.google.com.br')

browser.find_element_by_xpath("//input[@title='Pesquisar']").send_keys('Python programming')

browser.find_element_by_xpath("//input[@title='Pesquisar']").send_keys(Keys.RETURN)
