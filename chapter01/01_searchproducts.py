from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)  # 使用30秒隐式等待时间来定义 Selenium 执行步骤的超时时间
driver.maximize_window()  # 调用 Selenium API 来最大化浏览器窗口

# navigate to the application home page
# 在 get() 方法被调用后，WebDriver 会等待，一直到页面加载完成才继续控制脚本
driver.get('http://demo-store.seleniumacademy.com/')

# get the search textbox
# find_element_by_name() 方法会返回第一个 name 属性值与输入参数匹配的元素
search_field = driver.find_element_by_name('q')
# 使用 clear() 方法来清理之前的值
search_field.clear()

# enter search keyword and submit
# 通过 send_keys() 方法输入新的特定的值
search_field.send_keys('phones')
# 调用 submit() 方法提交搜索请求
search_field.submit()

# 提交搜索请求后，Firefox浏览器会加载结果页面。结果页面中有一系列与搜索项(phones)匹配的产品

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")

# get the number of anchor elements found
print('Found ' + str(len(products)) + ' products:')

# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print product.text

# close the browser window
driver.quit()
