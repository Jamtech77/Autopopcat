from selenium import webdriver
import threading

options=webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options)

url= u"https://popcat.click/"
driver.get(url)
popcat = driver.find_element_by_xpath("//*")

def press_t1():
    while 1:
        popcat.send_keys("TaiwannumberoneTaiwannumberoneTaiwannumberoneTaiwannumberone")

def press_t2():
    while 1:
        popcat.send_keys("TaiwannumberoneTaiwannumberoneTaiwannumberoneTaiwannumberone")

t1_thread = threading.Thread(target=press_t1)
t2_thread = threading.Thread(target=press_t2)

t1_thread.start()
t2_thread.start()
