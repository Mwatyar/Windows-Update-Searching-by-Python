import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.catalog.update.microsoft.com/Search.aspx?q=Microsoft Excel 2016 (KB4461600) 64 ビット版 の更新プログラム')
time.sleep(3)
driver.find_element_by_xpath('//*[@class="resultsbottomBorder resultsButtonWidth"]').click()
time.sleep(5)
driver.switch_to_window(driver.window_handles[1]) 
driver.find_element_by_tag_name('a').click()
time.sleep(10)


driver.quit()