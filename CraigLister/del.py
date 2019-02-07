from selenium import webdriver

driver = webdriver.Chrome('/home/nsa/del/CraigLister/chromedriver')
driver.get("https://post.craigslist.org/k/jhLie1sp6RGiRj1PMK6qwQ/71TUI?s=type")
button = driver.find_element_by_xpath("//*[contains(text(), 'for sale by owner')]")
button.click()
