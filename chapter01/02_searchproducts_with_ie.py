import os
from selenium import webdriver

# get the path of IEDriverServer
"""
运行脚本后，Selenium 会加载 InternetExplorerDriver 服务，用它来启动浏览器和执行脚本。
InternetExplorerDriver 服务在 Selenium 脚本和浏览器之间扮演类似中介角色。
"""
dir = os.getcwd()
ie_driver_path = dir + '\IEDriverServer.exe'

# create a new Internet Explorer session
driver = webdriver.Ie(ie_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get('http://demo-store.seleniumacademy.com/')

# get the search textbox
search_field = driver.find_element_by_name('q')
search_field.clear()

# enter search keyword and submit
search_field.send_keys('phones')
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")

# get the number of anchor elements found
print 'Found ' + str(len(products)) + ' products:'

# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print product.text

# close the browser window
driver.quit()
