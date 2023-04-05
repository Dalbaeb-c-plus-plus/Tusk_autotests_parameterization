from selenium.webdriver.common.by import By
import time
 
def test_find__card_button(browser):
    try:
       link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
       browser.implicitly_wait(20)
       browser.get(link)
       # time.sleep(30)
       btn=browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button") 
       assert btn, "Button not found"
    finally:
       browser.quit()