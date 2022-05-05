from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/teamgoals/detailed"
path = "C:/Users/NICO-PC/Desktop/PRACTICA/DATOS SIMPLES/chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()


lista_desplegable = Select(driver.find_element_by_id("country"))
lista_desplegable.select_by_visible_text("Argentina")

time.sleep(3)

lista_desplegable2 = Select(driver.find_element_by_id("season"))
lista_desplegable2.select_by_index("1")

time.sleep(3)

partidos = driver.find_elements_by_tag_name("tr")


matches = []
for partido in partidos:
    matches.append(partido.text)
    
driver.quit()
#Pandas
df = pd.DataFrame({"matches":matches})
print(df)
df.to_csv("LIGA ARGENTINA 2021.csv",index=False)
