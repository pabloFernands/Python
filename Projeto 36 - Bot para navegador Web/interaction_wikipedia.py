from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
first_name.send_keys("Pablo")
last_name = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
last_name.send_keys("Fernandes")
email_adress = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
email_adress.send_keys("pablo@hotmail.com", Keys.ENTER)

#print(article_value.text)

driver.quit()

