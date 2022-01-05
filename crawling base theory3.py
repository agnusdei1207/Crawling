#!/usr/bin/env python
# coding: utf-8

# ### 웹 페이지 제어
# - Selenium

# In[1]:


#!pip install selenium


# In[75]:


#webdriver : 웹을 통제하기 위한 라이브러리
#Keys : 웹을 통해 입력하기 위한 라이브러리 예) 검색
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd


# ### chromedriver 필요

# In[34]:


#res
driver = wb.Chrome()
driver.get("https://www.naver.com/")

input_area = driver.find_element_by_css_selector("input#query")
input_area.send_keys("손")
#input_area.clear() 검색창 비우기

#input_area.send_keys(Keys.ENTER)
driver.find_element_by_css_selector("button#search_btn").click()


# In[35]:


driver = wb.Chrome()
driver.get("https://www.google.co.kr/")

input_area = driver.find_element_by_css_selector("input.gLFyf.gsfi")
input_area.send_keys("광주날씨")
input_area.send_keys(Keys.ENTER)


# In[36]:


soup = bs(driver.page_source,'lxml')
soup.select("span.wob_t.q8U8x#wob_tm")[0].text


# ### 한솥

# In[78]:


driver = wb.Chrome()
driver.get("https://www.hsd.co.kr/menu/menu_list#none")
btn = driver.find_element_by_css_selector("a.c_05")
try:
    for i in range(10):
            btn.click()
except:
    print("끝이 나면 이 글이 출력 된다.")
    #bs(res.text,"lxml")
soup = bs(driver.page_source,"lxml")
menu = soup.select("h4.h.fz_03")
price = soup.select("div.item-price>strong")


dic = {"메뉴이름":menu, "가격":price}
df = pd.DataFrame(dic)
df


# ## 이미지 수집

# In[76]:


import time #시간제어
import os #파일,폴더 제어 (생성,삭제,존재여부 파악)
from urllib.request import urlretrieve #이미지 경로를 파일로 저장시킨다.


# In[60]:


if not os.path.isdir("./이미지"):#존재여부 파악
    os.mkdir("./이미지")


# In[79]:


driver = wb.Chrome()
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%8B%A4%ED%81%AC%EC%97%90%EB%8D%B4")
body = driver.find_element_by_css_selector("body")
for i in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
soup = bs(driver.page_source,"lxml")
img = soup.select("img._image._listImage")
img[0]["src"]

img_list = []

for i in img:
    #img[o]
    #img[1]
    #img[2] 
    #img[i]
    # i = img[i]
    try:
        img_list.append(i["data-lazy-src"])
    except:
        img_list.append(i["src"])

for i in range(len(img_list)):
    urlretrieve(img_list[i],'./이미지/'+str(i+1)+".jpg")
    time.sleep(0.5)
    print("{}번째 이미지 저장완료".format(i+1))


# In[87]:


driver = wb.Chrome()
driver.get("https://www.hsd.co.kr/menu/menu_list#none")
btn = driver.find_element_by_css_selector("a.c_05")
try:
    for i in range(10):
            btn.click()
except:
    print("끝이 나면 이 글이 출력 된다.")
    #bs(res.text,"lxml")
soup = bs(driver.page_source,"lxml")
menu = soup.select("h4.h.fz_03")
price = soup.select("div.item-price>strong")


img = soup.select("a.item-cont")


img_list = []

if not os.path.isdir("./한솥 이미지"):
    os.mkdir("./한솥 이미지")
    
for i in img:
        img_list.append(i["src"])

for i in range(len(img_list)):
    urlretrieve(img_list[i],"./이미지/"+str(i+1)+".jpg")
    time.sleep(1)
    print("{}번째 이미지 저장완료".format(i+1))


# In[97]:


driver = wb.Chrome()
driver.get("http://www.google.com")

gmail = driver.find_element_by_css_selector("a.gb_f")
# \n : click
# 새 탭으로 열기
gmail.send_keys(Keys.CONTROL+"\n")
#실행되어 있는 탭 확인
driver.window_handles
#탭 전환하기
driver.switch_to.window(driver.window_handles[1])
#현재 제어하는 탭 끄기
driver.close()


# In[103]:


#pip inatsll pyautogui
import pyautogui
import pyperclip


# In[104]:


time.sleep(1)
pyautogui.hotkey("ctrl","2")

print(pyautogui.size())

print(pyautogui.position())

pyautogui.moveTo(2934,133)

pyautogui.click()


# In[ ]:




