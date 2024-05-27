from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)


class ConsultAptForRent:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_option)

    def zillowConsult(self):
        self.driver.get("https://appbrewery.github.io/Zillow-Clone/")
        #time.sleep(2)
        self.address = self.driver.find_elements(By.CSS_SELECTOR, value="address")
        self.adress_list = []
        #transform list with text
        for adre in self.address:
            self.adress_list.append(adre.text)
        #print(adre.text)

        self.links = self.driver.find_elements(By.CSS_SELECTOR, value="a[data-test='property-card-link']")
        self.href_list = []
        for image_link in self.links:
            self.href = image_link.get_attribute("href")
            self.href_list.append(self.href)
        #print(self.href_list)

        self.prices = self.driver.find_elements(By.CLASS_NAME, value="PropertyCardWrapper__StyledPriceLine")
        self.prices_list = []
        self.pattern = r'\$([\d,]+)'
        for price in self.prices:
            match = re.search(self.pattern, price.text)
            if match:
                preco = match.group(1)
                preco = int(preco.replace(",", ""))
                self.prices_list.append(str(preco))
        print(self.prices_list)
        self.new_price_list = []
        #for value in self.prices_list:
            #self.new_price_list.append(value)
            #print(value)
            #forms_price.send_keys(value)
        #print(self.new_price_list)

    def formsCreate(self):

        x = 0
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd2Fq3H9I3MZbKJYnHVCSOBuj1ahRBvT8Q4c1Mgqh5ongexrw/viewform")
        time.sleep(2)

        # Outro jeito de criar lista
        # while x <= len(self.adress_list):
        #
        #     forms_adress.send_keys(self.adress_list[x])
        #     forms_price.send_keys(self.prices_list[x])
        #     forms_link.send_keys(self.href_list[x])
        #     x += 44

        for adress, price, url in zip(self.adress_list, self.prices_list, self.href_list):
            forms_adress = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div'
                                                                    '/div[2]/div/div[1]/div/div[1]/input')
            forms_price = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div'
                                                                   '/div[2]/div/div[1]/div/div[1]/input')
            forms_link = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div'
                                                                  '/div[2]/div/div[1]/div/div[1]/input')
            send_button = self.driver.find_element(By.XPATH,
                                                   value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            forms_adress.send_keys(adress)
            forms_price.send_keys(price)
            forms_link.send_keys(url)
            send_button.click()
            another_answer = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_answer.click()
            time.sleep(1)



rent_look = ConsultAptForRent()
rent_look.zillowConsult()
rent_look.formsCreate()

