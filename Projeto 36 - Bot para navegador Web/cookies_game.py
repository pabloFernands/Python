from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Opção de deixar o chrome aberto
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

x = 0
while x < 1000:
    #whait for seconds to execute
    #sleep(1)
    total_cookies = int(driver.find_element(By.ID, value="money").text)
    print(total_cookies)
    cookie.click()
    cursor = driver.find_element(By.ID, value="buyCursor")
    cursor_price = int(driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text.split()[2])
    #print(cursor_price)
    grandma = driver.find_element(By.ID, value="buyGrandma")
    grandma_price = int(driver.find_element(By.CSS_SELECTOR, value='#buyGrandma b').text.split()[2])
    print(grandma_price)
    if grandma_price <= total_cookies:
        grandma.click()

    elif cursor_price <= total_cookies:
        cursor.click()

    else:
        cookie.click()
    x += 1


