from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import string
from random import *
import random
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

user = []
passw = []
phone = []
open_names = open("names.txt","r")
names = open_names.read()
names = names.split()

#--- WORKS ---#
def bestbuy():
    start = time.time()
    for i in range(len(user)):
        driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
        driver.get("https://www.bestbuy.com/identity/newAccount?token=tid%3A82e1c83a-4d9a-11ec-8d37-020ec801d58b")
        driver.find_element(By.XPATH, '//input[@id="firstName"]').send_keys(random.choice(names))
        driver.find_element(By.XPATH, '//input[@id="lastName"]').send_keys(random.choice(names))
        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(user[i])
        driver.find_element(By.XPATH, '//input[@id="fld-p1"]').send_keys(passw[i])
        driver.find_element(By.XPATH, '//input[@id="reenterPassword"]').send_keys(passw[i])
        driver.find_element(By.XPATH, '//input[@id="phone"]').send_keys(phone[i])
        driver.find_element(By.XPATH, '//input[@id="phone"]').send_keys(phone[i])
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        print("Account Successfully Created")
    end = time.time()
    print(end - start)

#--- WORK IN PROGRESS ---# (Need to find method to bypass or work against PX hold and click)
def walmart():
    for i in range(len(user)):
        driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
        driver.get("https://www.walmart.com/account/signup?vid=oaoh")
        driver.find_element(By.XPATH, '//input[@data-tl-id="signup-first-name-input"]').send_keys(random.choice(names))
        driver.find_element(By.XPATH, '//input[@data-tl-id="signup-last-name-input"]').send_keys(random.choice(names))
        driver.find_element(By.XPATH, '//input[@data-tl-id="signup-email-input"]').send_keys(user[i])
        driver.find_element(By.XPATH, '//input[@data-tl-id="signup-password-input"]').send_keys(passw[i])
        driver.find_element(By.XPATH, '//button[@data-tl-id="signup-submit-btn"]').click()
        print("Account Successfully Created")

#--- WORK IN PROGRESS ---# (Need to find link or method to get into create account page)
def target():
    for i in range(len(user)):
        driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
        driver.get("https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_create_account")
        driver.find_element(By.XPATH, '//span[@class="Link-sc-1khjl8b-0 kdCHb AccountLink-sc-gx13jw-1 dWsPuD"]').click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(user[i])
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(random.choice(names))
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(random.choice(names))
        driver.find_element(By.XPATH, '//input[@id="phone"]').send_keys(phone[i])
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(passw[i])
        driver.find_element(By.XPATH, '//button[@id="createAccount"]').click()
        print("Account Successfully Created")
        time.sleep(10)

#--- WORK IN PROGRESS ---#
def microsoft():
    for i in range(len(user)):
        driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
        driver.get("https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1637807758&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2faccount.microsoft.com%2fauth%2fcomplete-signin%3fru%3dhttps%253A%252F%252Faccount.microsoft.com%252F%253Frefp%253Dsignedout-index%2526refd%253Dwww.google.com&lc=1033&id=292666&lw=1&fl=easi2&mkt=en-US&lic=1&uaid=4d50aa7e5a2c4d408a512ff3ff6a3f6a")
        driver.find_element(By.XPATH, '//input[@id="MemberName"]').send_keys(user[i])
        driver.find_element(By.XPATH, '//input[@id="PasswordInput"]').send_keys(passw[i])
        #randomly guess 1000-9999 (extremly quick)
        #solve captcha (will think aobut it)


#Inputs
choose = input(" 1. Bestbuy \n 2. Target \n 3. Walmart \n 4. Microsoft \n Choose a website: ")
catchall = input("Enter your catchall: ")
amount = int(input("How many accounts do you want: "))

#Generates Password
for gen_pass in range(amount):
  characters = string.ascii_letters + string.punctuation  + string.digits
  password = "".join(choice(characters) for x in range(randint(15, 24)))
  passw.append(password)

#Generates Email
for gen_email in range(amount):
    random_name = random.choice(names)
    random_name2 = random.choice(names)
    new_gmail = random_name + random_name2 + catchall
    user.append(new_gmail)
print(passw)
print(user)

#---- RUNS BESTBUY ACC GEN ----#
if choose == "1":
    area_code = input("Enter your area code: ")
    for gen_phone in range(amount):
        tredigi = str(random.randint(100,999))
        quadigi = str(random.randint(1000,9999))
        new_phone = area_code + tredigi + quadigi
        phone.append(new_phone)
    print(phone)
    bestbuy()


#---- RUNS TARGET ACC GEN ----#
if choose == "2":
    area_code = input("Enter your area code: ")
    for gen_phone in range(amount):
        tredigi = str(random.randint(100,999))
        quadigi = str(random.randint(1000,9999))
        new_phone = area_code + tredigi + quadigi
        phone.append(new_phone)
    print(phone)
    target()

#---- RUNS WALMART ACC GEN ----#
if choose == "3":
    walmart()

#---- RUNS MICROSOFT ACC GEN ----#
if choose == "4":
    microsoft()

