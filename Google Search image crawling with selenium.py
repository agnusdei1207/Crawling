#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium bs4 tqdm')


# In[6]:


from selenium import webdriver as wb # 브라우저를 조작하는 도구
from selenium.webdriver.common.keys import Keys # 키 입력을 도와주는 도구(키보드)
from bs4 import BeautifulSoup as bs # 문서를 파싱해서 선택자 활용을 도와주는 도구
from tqdm import tqdm # 반복문 진행 정도를 시각화해주는 도구
from urllib.request import urlretrieve # 이미지 다운로드를 도와주는 도구
import time # 시간제어 도구
import os # 폴더 생성,삭제,이동 등을 도와주는 도구


# In[20]:


keyword = "럭스" # 수집하고 싶은 검색 키워드!


# In[21]:


# 이미지가 저장될 폴더 생성
# 해당 폴더가 있는지 확인
if os.path.isdir('./'+keyword) == False :
    os.mkdir("./"+keyword) # 폴더 생성


# In[22]:


url = 'https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjs85-GsN7vAhX4xYsBHR6aBg0Q_AUoAXoECAEQAw&biw=1745&bih=852'.format(keyword)

driver = wb.Chrome() # 브라우져 생성
driver.get(url) # url 요청
time.sleep(3) # 페이지 로딩까지 3초 대기

cnt = 0
pre_img_src = [] # 이전에 다운로드된 경로

for j in range(3) :  # range = 크롤링양!  더보기가 나오기까지 스크롤을 내리게 셋팅
    img_html = bs(driver.page_source,'html.parser')

    # 이미지 태그 수집
    images = img_html.select('img.rg_i.Q4LuWd')

    # 이미지 태그의 src 속성 값 추출
    img_src = []
    for img in images :
        src = img.get('src')
        if src != None : # img 태그에 src 속성이 없는 경우
            if src not in pre_img_src : # 이전에 다운로드한 경로에 있는지 검사
                img_src.append(src)
        else : # img 태그에 src 속성이 있는 경우
            src = img.get('data-src')
            if src not in pre_img_src :
                img_src.append(src)

    # 파일 다운로드
    # img_src를 반복문으로 돌면서 저장, tqdm 사용
    for src in tqdm(img_src) :
        cnt += 1
        urlretrieve(src,'./{}/{}.png'.format(keyword,cnt))

    pre_img_src += img_src # 다운로드한 경로를 이전 리스트에 추가    
        
    # 화면 스크롤
    for i in range(6):
        driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)


# In[ ]:




