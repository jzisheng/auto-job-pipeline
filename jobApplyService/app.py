from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import time


def getElemBy(cstr_,class_str):
    return driver.find_element_by_xpath("//*[contains(@"+cstr_+", '"+class_str+"')]")

def getTextBy(cstr_, class_str):
    return driver.find_element_by_xpath("//*[contains(@"+cstr_+", '"+class_str+"')]").text



DEBUG = False

f = open(authPath)
d = json.load(f)
userStr = d["email"]
pwStr = d["password"]

if DEBUG:
    # driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub",
    #                          DesiredCapabilities.CHROME)
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    '''
    sign in
    '''

    targetUrl = "https://www.linkedin.com/"+\
        "login?fromSignIn=true&trk="+\
        "guest_homepage-basic_nav-header-signin"

    authPath = "/Users/zisheng/auth.json"

    driver.get(targetUrl)



    username = driver.find_element_by_id('username')
    pw = driver.find_element_by_id('password')

    username.send_keys(userStr)
    pw.send_keys(pwStr)
    getElemBy("class","btn__primary--large from__button--floating").click()
    


import boto3
def sendSnsMessage(subject_str,msg_json_str):
    sns = boto3.client('sns',
                       region_name='us-east-1',
                       aws_access_key_id=d["aws_access_key_id"],
                       aws_secret_access_key= d["aws_secret_access_key"])
    # Publish a simple message to the specified SNS topic
    response = sns.publish(
        TopicArn = 'arn:aws:sns:us-east-1:337851407731:jobs_topic',
        Subject = subject_str,
        Message = msg_json_str
    )
    # Print out the response
    print(response)


'''
go to jobs listings
'''
def searchJobs():
    jobListsUrl = "https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=%22software%20engineer%22%20%22new%20grad%22&location=United%20States"

    driver.get(jobListsUrl)

    elems = driver.find_elements_by_xpath("//*[contains(@class, 'job-card-container')]")

    job_title_class = "jobs-details-top-card__job-title"
    company_title_class = "jobs-details-top-card__company-url"
    details_id = "job-details"
    i = 0
    elem = elems[i]
    elem.click()
    
    title_str = getTextBy("class",job_title_class)
    company_str = getTextBy("class",company_title_class)
    details_str = getTextBy("id",details_id)
    url_str = driver.current_url
    
    msg = {
        'title':title_str,
        'company':company_str,
        'details_str':details_str,
        'url':url_str
    }
    sendSnsMessage('position',json.dumps(msg))

    # this is the part thats wack
    time.sleep(2)
    action = ActionChains(driver)
    e = getElemBy("class", "jobs-apply-button artdeco-button")
    action.double_click(e)
    
def applyLever():
    s = "https://jobs.lever.co/plaid/02998813-cd2a-4449-9eb1-49ee383d977f?lever-origin=applied&lever-source=LinkedInPaid"
    driver.get(jobListsUrl)
    


searchJobs()
# sendSnsMessage('test','{"messsage":"Hello World"}')
# driver.quit()
