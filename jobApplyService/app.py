import feedparser
from newspaper import Article
from time import sleep
from json import dumps
from kafka import KafkaProducer

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if False:
    # driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub",
    #                          DesiredCapabilities.CHROME)
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    '''
    sign in
    '''

    targetUrl = "https://www.linkedin.com/"+\
        "login?fromSignIn=true&trk="+\
        "guest_homepage-basic_nav-header-signin"

    authPath = "/Users/zisheng/auth.txt"

    driver.get(targetUrl)

    f = open(authPath,"r")
    userStr = f.readline()
    pwStr = f.readline()

    username = driver.find_element_by_id('username')
    pw = driver.find_element_by_id('password')

    username.send_keys(userStr)
    pw.send_keys(pwStr)


'''
go to jobs listings
'''

def getElemBy(cstr_,class_str):
    return driver.find_element_by_xpath("//*[contains(@"+cstr_+", '"+class_str+"')]")

def getTextBy(cstr_, class_str):
    return driver.find_element_by_xpath("//*[contains(@"+cstr_+", '"+class_str+"')]").text


jobListsUrl = "https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=%22software%20engineer%22%20%22new%20grad%22&location=United%20States"

driver.get(jobListsUrl)

elems = driver.find_elements_by_xpath("//*[contains(@class, 'job-card-container')]")

job_title_class = "jobs-details-top-card__job-title"
company_title_class = "jobs-details-top-card__company-url"
details_id = "job-details"
for elem in elems:
    elem.click()
    title_str = getTextBy("class",job_title_class)
    company_str = getTextBy("class",company_title_class)
    details_str = getTextBy("id",details_id)
    
    print(company_str,"-",title_str)
    break


# driver.quit()
