from re import T
import re
import pytest
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value
from lib2to3.pgen2 import driver
from selenium import webdriver
import time
import pickle
from selenium.webdriver.common import actions
from selenium.webdriver.common import by
from selenium.webdriver.common import keys
#from selenium.webdriver.common import keys  
from selenium.webdriver.common.keys import Keys  
#from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
#PATH = "C:\Program Files (x86)\chromedriver.exe"
PATH = r"E:\chromedriver.exe"
#comment
#comment no 3


#th
# is is fifth committ
#hy
#this is commit
#this iss second commit
#thiss is third commit
#thiss iss fourth commit

#this is new chanege

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

driver = webdriver.Chrome(PATH ,options=chrome_options )
driver.maximize_window()  
actionChains = ActionChains(driver)






intvariable = pickle.load(open(r"C:\Users\Ibrahim\.vscode\variableFile.dat", "rb"))
strvariable = str(intvariable)
intvariable = intvariable + 1
pickle.dump(intvariable ,  open(r"C:\Users\Ibrahim\.vscode\variableFile.dat", "wb"))


firstnamee = "ibrahim"
lastnamee = "rehman"
email = "ibrahim"+strvariable+"@yopmail.com"







#@pytest.mark.parametrize("total, dic" , [(10,5),(10,2),(10,6)])
def basic_info():
    
    driver.get("https://avaxdev.akru.co/")
    getstarted = WebDriverWait(driver, 30).until(
            #EC.visibility_of_element_located((By.ID ,'navbar-header-sticky-starter'))
            EC.presence_of_element_located((By.ID ,'navbar-header-sticky-starter'))
        )

    getstarted.click()


    WebDriverWait(driver , 2).until(
        EC.presence_of_element_located((By.XPATH , "//input[@name='gender1' and @value='yes']"))
    ).click()


    conti = driver.find_element_by_xpath("//button[@class='primary-btn' and text()='Continue'] ").click()

    #SelectStarterPlan
    WebDriverWait(driver , 2).until(
        EC.presence_of_element_located((By.XPATH , "//h3[@class='title' and text()='Starter']//parent::div//button"))
    ).click()

    #checkLowRadiobutton
    WebDriverWait(driver , 5).until(
        EC.presence_of_element_located((By.NAME , "low"))
    ).click()

    #Selectlowerplan
    driver.find_element(By.XPATH , "//div[@class='service-inner']//button[@class='primary-btn modal-mini-button'] ").click()


    #firstname
    WebDriverWait(driver , 5).until(
        EC.presence_of_element_located((By.NAME , "firstName"))
    ).send_keys(firstnamee)
    
    #firstname = driver.find_element_by_name("firstName").send_keys(firstnamee)
    lastname = driver.find_element_by_name("lastName").send_keys(lastnamee)
    emailin = driver.find_element_by_name("email").send_keys(email)

    #individualradiobutton
    driver.find_element_by_xpath("//input[@value='Individual']").click()

    agreeselect = driver.find_element_by_name("agreeCheck").click()
 
    #agree and continue button
    agreeconti = driver.find_element_by_xpath("//button[@class='primary-btn mr-1 '] ").click()
    
    try:
        if(WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH , "//h5[text()=' Verify Your Email ']"))
            )): 
                return True
       
    except:
        if(WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.XPATH,"//a[@class='thm-btn btn-style-modal-SignUp']") , "Do you want to continue through Email?"))):
            # sendmail = driver.find_element_by_xpath("//a[@class='thm-btn btn-style-modal-SignUp']")
            # sendmail.click()
            # casek = True
            return False, "Email already registerd"
  

def verify_mail():
    # if driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div') .size['width'] != 0 :
    #     mailLink = driver.find_element(By.XPATH , '/html/body/div[2]/div/div[1]/div/div/div[3]/div[1]/a')
    #     actionChains.move_to_element(mailLink).click().perform()

    driver.execute_script("window.open('');")
    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://yopmail.com/en/")

    #Find and give mail
    yopmail = WebDriverWait(driver , 30).until(
        EC.presence_of_element_located((By.ID , "login"))
    )
    yopmail.send_keys(Keys.CONTROL + "a")
    yopmail.send_keys(email)
    yopmail.send_keys(Keys.ENTER)
    try:
            if (driver.find_element_by_xpath('//*[@id="r_dialog"]')):
                print(" Capctah found")
                time.sleep(3)

                WebDriverWait(driver, 10).until(EC.frameToBeAvailableAndSwitchToIt(By.xpath("//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]")))

                WebDriverWait(driver, 20).until(EC.elementToBeClickable(By.cssSelector("div.recaptcha-checkbox-checkmark"))).click()
                time.sleep(3)


                # driver.switch_to.frame('a-lubtvn1tatio')
                # print("Enter into iframe")

                
                # capcha = driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]')
                # actionChains.move_to_element(capcha).click().perform()
                # time.sleep(2)


    except:
            print(" No Capcta found")

    ifframe = WebDriverWait(driver , 30).until(
        EC.frame_to_be_available_and_switch_to_it("ifmail")
        #EC.presence_of_element_located((By.XPATH, "//iframe[@name='ifmail']"))
    )
    
    #driver.switch_to.frame("ifmail")
    verify = driver.find_element(By.XPATH , "//a//b")
    verify.click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[2])

    try:
        if(
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH , "//h1[@class='title' and text()='Contact Info']"))
        )):
            return True
    except:
        return False
    

def contact_info():
    firstname = driver.find_element_by_name("address")
    firstname.send_keys(Keys.CONTROL + "a")
    firstname.send_keys("islamabad")
    

    selectcountry = Select(driver.find_element_by_name("citizenshipLabel"))
    selectcountry.select_by_visible_text("United States")
    

    selectstate = Select(driver.find_element_by_name("stateName"))
    selectstate.select_by_visible_text("California")
    

    phone = driver.find_element_by_name("number")
    phone.send_keys(Keys.CONTROL + "a")
    phone.send_keys("03215716436")
    

    city = driver.find_element_by_name("city")
    city.send_keys(Keys.CONTROL + "a")
    city.send_keys("california")
    

    zipc = driver.find_element_by_name("zipCode")
    zipc.send_keys(Keys.CONTROL + "a")
    zipc.send_keys("46000")


    dob = driver.find_element_by_id("date-picker-dialog")
    dob.send_keys(Keys.CONTROL + "a")
    dob.send_keys("01/01/1970")


    verifyphone = driver.find_element_by_xpath("//button[@class='primary-btn' and text()='Verify']")
    verifyphone.click()
    time.sleep(2)




    driver.execute_script("window.open('');")
    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[3])
    otplink = "https://avaxdevapi.akru.co/api/user/showOtp/" + email
    driver.get(otplink)
    driver.refresh()

    time.sleep(2)
    input = driver.find_element_by_xpath('/html/body/pre').text
    otp = (input[39: 43])


    driver.switch_to.window(driver.window_handles[2])

    WebDriverWait(driver , 2).until(
        EC.presence_of_element_located((By.NAME , "otp"))
    ).send_keys(otp)
    #driver.find_element_by_name("otp").send_keys(otp)

    ssn = driver.find_element_by_name("securityNumber")
    ssn.send_keys(Keys.CONTROL + "a")
    ssn.send_keys("566650509")

    conticontact = driver.find_element_by_xpath("//button[@class='primary-btn mr-1']").click()

    try:
        if(
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH , "//h1[text()='Account Details']"))
        )):
            return True
    except:
        if(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , "div[role='alert']"))
        )):
            chkl = driver.find_element_by_css_selector("div[role='alert']")
            print(chkl.text)
            return False

    
def account_detail():
    skipb  = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH ,"//button[@class='primary-btn mr-1']"))
    )
    #skipb = driver.find_element_by_xpath('//*[@id="root"]/div/section/div/div/div/div/div/div[3]/form/div[2]/div[2]/div/div/button')
    skipb.click()
   
    if(
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH , "//h1[text()='Agreements']"))
        )):
        return True
    else:
         False

    



def agreement():
    pont1 = driver.find_element_by_name("point1")
    pont1.click()

    pont2 = driver.find_element_by_name("point2")
    pont2.click()

    pont3 = driver.find_element_by_name("point3")
    pont3.click()

    agreconti = driver.find_element_by_xpath("//button[@class='primary-btn ml-auto d-block']")
    agreconti.click()
    
    if(
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH , "//h1[text()='Please review.']"))
        )):
        return True
    else:
        return False




def Please_review():
    verifyinfo = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH ,"//button[@class='primary-btn ml-auto d-block']"))
            )
    verifyinfo.click()
    try:
        if(WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH , "//div[@role='alert']"))
            )):
                return True
        else:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH ,"//button[@class='primary-btn ml-auto d-block']"))
            )
            return True
           

    except:
        return False

def verify_mail2():
    
    cretewallet = driver.find_element_by_xpath("//button[@class='primary-btn ml-auto d-block']").click()
    
    #modale
    WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH ,"//div[@class='donwload-btn']"))
            ).click()
    

    

    # if(WebDriverWait(driver, 120).until(
    #              EC.presence_of_element_located((By.XPATH ,"//div[@class='mg_bd mg_bf _e']"))
    #          )):
    #     print("check email")
    
    time.sleep(2)

    driver.execute_script("window.open('');")
    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[4])
    driver.get("https://yopmail.com/en/")
    


    yopmail = WebDriverWait(driver , 30).until(
        EC.presence_of_element_located((By.ID , "login"))
    )
    yopmail.send_keys(Keys.CONTROL + "a")
    yopmail.send_keys(email)
    yopmail.send_keys(Keys.ENTER)
    try:
            if (driver.find_element_by_xpath('//*[@id="r_dialog"]')):
                print(" Capctah found")
                time.sleep(3)

                WebDriverWait(driver, 10).until(EC.frameToBeAvailableAndSwitchToIt(By.xpath("//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]")))

                WebDriverWait(driver, 20).until(EC.elementToBeClickable(By.cssSelector("div.recaptcha-checkbox-checkmark"))).click()
                time.sleep(3)

    except:
            print(" No Capcta found")

    ifframe = WebDriverWait(driver , 30).until(
        EC.frame_to_be_available_and_switch_to_it("ifmail")
        #EC.presence_of_element_located((By.XPATH, "//iframe[@name='ifmail']"))
    )
    
    #driver.switch_to.frame("ifmail")
    verify = driver.find_element(By.XPATH , "//strong[text()='Log in to Akru TestNet']")
    verify.click()
    time.sleep(2)


    driver.switch_to.window(driver.window_handles[2])


    if (WebDriverWait(driver, 60).until( 
            EC.text_to_be_present_in_element((By.XPATH,'//h5[@class="title"]') , "New Account Created"))):
            print(" New account created succeccfully ")
            newaccountok = driver.find_element_by_xpath('//button[@class="primary-btn" and @type="button"]')
            newaccountok.click()
            return True
    else:
        return False       

    time.sleep(2)





def test_basicinfo():
    case = basic_info()
    assert case
def test_verifymail():
    verifymail = verify_mail()
    assert verifymail
def test_contact_info():
    contactifo = contact_info()
    assert contactifo
def test_account_detail():
    acc = account_detail()
    assert acc
def test_agreement():
    agree = agreement()
    assert agree
def test_please_review():
    pr = Please_review()
    assert pr
def test_verify_mail():
    vm = verify_mail2()
    assert vm
#basic_info()
# To run test
# python -m pytest .\test_param.py -W ignore::DeprecationWarning -p no:warnings --tb=line  -rx