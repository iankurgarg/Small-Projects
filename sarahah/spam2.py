from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
import sys
from time import sleep
#import selenium.webdriver.support.ui.WebDriverWait

browser = webdriver.Firefox(executable_path='/Users/iankurgarg/Downloads/geckodriver')
url = sys.argv[1]

def send_msg(msg):
    browser.get(url)
    username = browser.find_element_by_id( "Text" )
    submit   = browser.find_element_by_id( "Send"   )

    username.send_keys(msg)

    submit.click()


for i in range(200):
    send_msg("chutiya "*i)
    sleep(1)


browser.close()

