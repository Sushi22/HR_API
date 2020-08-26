import requests
import urllib3
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import passlib
from passlib.hash import sha256_crypt
from selenium.webdriver.chrome.options import Options
from decouple import config


def hr_info():
    options=Options()
    options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.headless=True
    
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'    
    options.add_argument('user-agent={0}'.format(user_agent))


    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
  
    driver.get("https://www.hackerrank.com/auth/login?h_l=body_middle_left_button&h_r=login")


    # driver.get_screenshot_as_file("screenshot.png")
    username=driver.find_element_by_xpath('//*[@id="input-1"]')

    password=driver.find_element_by_xpath('//*[@id="input-2"]')

    username.send_keys(config('user_name'))
    password.send_keys(config('pass_word'))

    driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[4]/button').click()

    driver.implicitly_wait(5) 

    driver.execute_script("window.scrollTo(0,700)")
    n=5
    j=18
    hr_data={}

    for i in range(2,n):
        title=driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div/div[4]/div/div[2]/div[2]/div[{i}]/div[1]/div/div/h3').text
        j+=1                            
        progress=driver.find_element_by_xpath(f'//*[@id="content"]/div/div/div/div[4]/div/div[2]/div[2]/div[{i}]/div[1]/div/div/div/div/div[2]').text
        hr_data[title]=progress
   
               

    # hr_url="https://www.hackerrank.com/sushmitajoshi22"
    # data=requests.get(hr_url)
    return hr_data

print(hr_info())
my_data=hr_info()