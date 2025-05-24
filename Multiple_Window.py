import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a").click()
time.sleep(2)
windowOpen = driver.window_handles
time.sleep(2)
driver.switch_to.window((windowOpen[1]))
time.sleep(2)
print(driver.find_element(By.XPATH, "/html/body/div[1]/h3").text)
driver.switch_to.window((windowOpen[0]))
time.sleep(2)
print(driver.find_element(By.XPATH, "/html/body/div[3]/div/div").text)
time.sleep(2)
driver.quit()