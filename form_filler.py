import csv
from selenium import webdriver
# adding incognito
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# opening an instance of browser
driver = webdriver.Chrome(executable_path='/Users/aayushsharma/python/voterlist/chromedriver', chrome_options=option)
driver.get("file:/Users/aayushsharma/python/autofillforms/form.html")

# with open('fin_news.csv', 'r') as csvfile:
#     datareader = csv.reader(csvfile)
#     for row in datareader:
#         print(row.decode('utf-8'))

date_elem = driver.find_element_by_id("date")
get_link = driver.find_element_by_id("link")
get_headline = driver.find_element_by_id("headline")
get_content = driver.find_element_by_id("content")
get_newsof = driver.find_element_by_id("newsof")

date_elem.send_keys("2018/12/3")
get_link.send_keys("https://sharesansar.com/hello")
get_headline.send_keys("This is my headline")
get_content.send_keys("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Numquam quo dignissimos consequatur debitis ducimus dolorum voluptates, error at maiores odit eos reiciendis inventore ex, molestiae quibusdam rerum unde consequuntur doloremque!")
get_newsof.send_keys("NEPSE")
