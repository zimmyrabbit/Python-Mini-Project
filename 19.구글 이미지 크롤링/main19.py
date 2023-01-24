#!/usr/bin/env python
# coding: utf-8

# In[11]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)


# In[12]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

elem = driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
elem.send_keys('바다')
elem.send_keys(Keys.RETURN)


# In[13]:


import time
elem = driver.find_element(By.TAG_NAME,'body')
for i in range(10):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

try:
    driver.find_element(By.CSS_SELECTOR,'#islmp > div > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input').click()

    for i in range(5):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass


# In[14]:


links=[]
images = driver.find_elements(By.CSS_SELECTOR,'#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')

for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))

print('찾은 이미지 개수 : ', len(links))


# In[15]:


import urllib.request

for i,k in enumerate(links):
    url = k
    urllib.request.urlretrieve(url, 'D:\\sourceTree\\Python Mini Project\\19.구글 이미지 크롤링\\photo\\'+str(i)+'.jpg')

print('다운로드 완료')

