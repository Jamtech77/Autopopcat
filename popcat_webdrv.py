from selenium import webdriver

options=webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options)

url= u"https://popcat.click/"
driver.get(url)
popcat = driver.find_element_by_xpath("//*")

while 1:
    popcat.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
