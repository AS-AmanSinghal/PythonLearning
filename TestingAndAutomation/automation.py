from selenium import webdriver

chrome_brower = webdriver.Chrome('./chromedriver.exe')

chrome_brower.maximize_window()

chrome_brower.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_brower.title

showMessageButton = chrome_brower.find_element_by_class_name('btn-default')

assert 'Show Message' in chrome_brower.page_source

userMessage = chrome_brower.find_element_by_id('user-message')

userMessage.clear()

userMessage.send_keys('I am Extra Cool')

# showMessageButton.click()

chrome_brower.close()
