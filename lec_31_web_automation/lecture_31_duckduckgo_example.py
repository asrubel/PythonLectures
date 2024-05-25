from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.duckduckgo.com")
print(driver.title)

search = driver.find_element("name", "q")
search.clear()
search.send_keys("python")
search.submit()

sleep(3)

# TODO
results = driver.find_elements('class_name', 'kY2IgmnCmOGjharHErah')
for r in results:
    print(r.text)
