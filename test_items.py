import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_xpath("//*[@id='add_to_basket_form']/button[@type='submit']")
    assert button.is_displayed(), "Button not found"


