#//tbody/tr/td[1]

from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get('https://stepupandlearn.in/wp-content/UI/tables.html')

element=driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
lastname=[]
for i in range(len(element)):
    lastname.append(element[i].text)

element=driver.find_elements(By.XPATH,"//tbody/tr/td[2]")

firstname=[]
for i in range(len(element)):
    firstname.append(element[i].text)

element=driver.find_elements(By.XPATH,"//tbody/tr/td[3]")

email=[]
for i in range(len(element)):
    email.append(element[i].text)

element=driver.find_elements(By.XPATH,"//tbody/tr/td[4]")

due=[]
for i in range(len(element)):
    due.append(element[i].text)

print(lastname.sort())
print(firstname.sort())
print(email.sort())
print(due.sort())

driver.close()