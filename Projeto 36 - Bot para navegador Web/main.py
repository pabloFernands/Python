from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

#Fechar apenas a aba
#driver.close()
#Fechar o programa


event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
#info_full = driver.find_element(By.XPATH, value="")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for x in range(len(event_names)):
    events[x] = {
        "Time": event_times[x].text,
        "Name": event_names[x].text,

    }

print(events)

driver.quit()
