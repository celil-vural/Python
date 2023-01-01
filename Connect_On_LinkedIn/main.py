import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
mail=input("Please enter the mail:")
password=input("Please enter the password:")
count=int(input("Please enter the number of connections you want:"))
# You can use chrome or firefox instead of edge
# For this, enter the browser name instead of the edge below
# And download the appropriate driver in the browser version and put it in the same directory as this file.
# And replace msedgedriver.exe with the name of your own driver
driver=webdriver.Edge("msedgedriver.exe");
driver.get("https://www.linkedin.com/home")
time.sleep(0.2)
driver.maximize_window()
email_input=driver.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/div[2]/div[1]/input')
password_input=driver.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/div[2]/div[2]/input')
email_input.send_keys(mail)
time.sleep(0.2)
password_input.send_keys(password)
time.sleep(0.1)
password_input.send_keys(Keys.ENTER)
driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[5]/aside/div[1]/header/div[3]/button[2]").click()
driver.find_element(By.TAG_NAME,"html").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[2]/div/button").click()
time.sleep(5)
formule=1
while(count>0):
    list_counter=0
    if(count>4):
        while(list_counter<4):
            driver.find_element(By.XPATH,f'/html/body/div[3]/div/div/div[2]/section/div/div[1]/ul/li[{str(formule)}]/div/div/div/section/div[2]/footer/button').click()
            time.sleep(1)
            try:
                driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button").click()
                print("Your quota is full.Please try again later...")
                time.sleep(1)
                list_counter=4
                count=0
            except:
                list_counter+=1
                formule+=1
    else:
        while (count>0):
            driver.find_element(By.XPATH,f'/html/body/div[3]/div/div/div[2]/section/div/div[1]/ul/li[{str(formule)}]/div/div/div/section/div[2]/footer/button').click()
            time.sleep(1)
            try:
                driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button").click()
                print("Your quota is full.Please try again later...")
                time.sleep(1)
                count = 0
            except:
                count -= 1
                formule += 1
    driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
    count-=1
    time.sleep(1)
driver.close()