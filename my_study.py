from selenium import webdriver

driver = webdriver.Firefox(executable_path="/Users/vladis/Downloads/geckodriver")

driver.get('http://www.google.com')

driver.find_element_by_css_selector(".gLFyf").send_keys("Selenium WebDriver")
driver.find_element_by_css_selector(".FPdoLc > center:nth-child(1) > input:nth-child(1)").click()

driver.find_element_by_css_selector()