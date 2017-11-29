from flask import Flask, abort, request, redirect
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
import sys
from flask import render_template
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys

#from wtforms.ext.appengine.db import model_form
#from models import MyModel


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("spam.html")

msgs = ['This is stupid', 'This is very stupid', 'You are stupid', 'Sarahah is stupid', 'Yes, you heard that right, this is stupid shit !',
			'Aap chutiye hain','Aap chutiye kyu hain','Aap vajra chutiye hain']
#msgs = ['Test1', 'Test2', 'Test3']



@app.route("/spam", methods=['POST'])
def spam():

    browser = webdriver.Firefox(executable_path='/Users/iankurgarg/Downloads/geckodriver')
    url = request.form['surl']
    ncount = request.form['ncount']
    msg = request.form['msg']
    if (msg == ''):
        msg = get_msg()

    n = len(msgs)
    for i in range(int(ncount)):
        send_msg(browser, url, msg)
        k = i
        if (k >= n):
            k = k%n
        msg = msgs[k]
        sleep(1)

    #rowser.close()

    return "Done"

#app.run(host='0.0.0.0')

def get_msg():

	i = randint(0, len(msgs))
	return msgs[i]


def send_msg(browser, url, msg):
    browser.get(url)
    username = browser.find_element_by_id( "Text" )
    submit   = browser.find_element_by_id( "Send"   )

    username.send_keys(msg)
    if is_exists_by_xpath(browser, '//div[@class="recaptcha-checkbox-checkmark" and @role="presentation"]'):
        browser.find_element_by_xpath('//div[@class="recaptcha-checkbox-checkmark" and @role="presentation"]').click()
    sleep(2)


    submit.click()

def is_exists_by_xpath(browser, xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except Exception:
        return False
    return True


app.run(host='0.0.0.0', threaded=True)