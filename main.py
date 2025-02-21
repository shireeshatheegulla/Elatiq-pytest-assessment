from selenium_recaptcha_solver import RecaptchaSolver
# from selenium.webdriver.common.by import By
from selenium import webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#

# test_ua = ''
#
# options = Options()
#
# options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
# options.add_argument("--window-size=1920,1080")
#
# options.add_argument(f'--user-agent={test_ua}')
#
# options.add_argument('--no-sandbox')
# options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path="C:\\Users\\91990\\Desktop\\chromedriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
#
test_driver = driver()
solver = RecaptchaSolver(driver=test_driver)

test_driver.get('https://www.google.com/recaptcha/api2/demo')

recaptcha_iframe = test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

solver.click_recaptcha_v2(iframe=recaptcha_iframe)