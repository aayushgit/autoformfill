import csv
from selenium import webdriver
# adding incognito
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# opening an instance of browser
driver = webdriver.Chrome(executable_path='/Users/aayushsharma/python/voterlist/chromedriver', chrome_options=option)
driver.get("file:/Users/aayushsharma/python/autofillforms/form.html")
date_elem = driver.find_element_by_id("date")
get_link = driver.find_element_by_id("link")
get_headline = driver.find_element_by_id("headline")
get_content = driver.find_element_by_id("content")
get_newsof = driver.find_element_by_id("newsof")
button = driver.find_element_by_id("button")
with open('fin_news.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader, None)
    for row in datareader:
        date_elem.send_keys(row[0])
        get_link.send_keys(row[1])
        get_headline.send_keys(row[2])
        get_content.send_keys(row[3])
        get_newsof.send_keys(row[4])
        button.click()

    datareader.close()
