#!/usr/bin/env python
# coding: utf-8

# ### 크롤링
# - 데이터를 수집 분류하는 것을 의미하고 주로 html 수집

# ### requests 라이브러리 사용법

# In[2]:


#서버에 페이지 정보를 요청할 때 사용하는 라이브러리
import requests as req


# In[4]:


res = req.get("https://www.naver.com/")
#[200] : 응답에 성공했다는 의미


# In[19]:


#text 콘텐트를 뽑아옴! 
#res.text


# ### BeautifulSoup 라이브러리
# - parsing 분류 분석
# - 응답된 데이터에서 원하는 부분만 추출

# In[7]:


get_ipython().system('pip install beautifulsoup4')


# In[8]:


from bs4 import BeautifulSoup as bs


# ### parsing

# In[20]:


#bs(파싱할 데이터, "파싱 방법")
result = bs(res.text,"lxml")


# In[11]:


result.select_one("a")


# In[17]:


re = result.select("a.nav")[2]


# In[18]:


re.text


# ### melon

# In[25]:


#406 : 요청 거부
melonUrl= req.get("https://www.melon.com/")
melonUrl


# In[29]:


#network f5 하고 User-Agent 복사 붙이기 및 키밸류 값으로 만들기
#get 두번째 파라미터에 headers 속성으로 넣기
h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
melonUrl= req.get("https://www.melon.com/",headers=h) 


# In[33]:


#parsing
result2 = bs(melonUrl.text,"lxml")


# In[58]:


#targeting
chart = result2.select("span.menu_bg")


# In[59]:


#slicing & printing
for i in range(9):
    print(chart[i].text)


# In[66]:


v = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}


# In[69]:


ranking = req.get("https://www.melon.com/chart/index.htm",headers = v)


# In[72]:


result3 = bs(ranking.text,"lxml")


# In[87]:


target = result3.select("div.rank01 a")


# In[88]:


len(target)


# In[134]:


singer = result3.select("div.rank02>a:first-child")
singer


# In[137]:


for i in range(len(singer)):
    print(target[i].text,singer[i].text)


# # data frame으로 만들기

# In[139]:


singer_list = []
title_list = []
rank_list = []


# In[147]:


for i in range(len(singer)):
    title_list.append(target[i].text)
    singer_list.append(singer[i].text)
    rank_list.append(i+1)


# In[148]:


#data frame column name key:value
#변수에 넣었으면 데이터프레임으로 바꿀 준비 완료
dic = {"가수":singer_list,"노래제목":title_list,"순위":rank_list}


# In[149]:


import pandas as pd


# In[154]:


df = pd.DataFrame(dic)
df.set_index("순위")


# # 네이버 영화 평점 

# In[157]:


res4 = req.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20211108")


# In[158]:


result4 = bs(res4.text,"lxml")


# In[159]:


title = result4.select("div.tit5>a")


# In[160]:


score = result4.select(".point")


# In[161]:


title_list = []
score_list = []
rank_list = []

for i in range(len(title)):
    title_list.append(title[i].text)
    score_list.append(score[i].text)
    rank_list.append(i+1)


# In[162]:


dic1 = {"영화제목":title_list, "평점":score_list,"랭킹":rank_list}


# In[163]:


import pandas as pd


# In[164]:


df1 = pd.DataFrame(dic1)


# In[166]:


df1.set_index("랭킹")


# In[ ]:




