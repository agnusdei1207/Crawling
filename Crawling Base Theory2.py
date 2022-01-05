#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import requests as req
from bs4 import BeautifulSoup as bs


# ### 1달 동안의 영화 페이지 수집
# - 20210101 ~ 20210131

# In[19]:


#포문 안에 있으면 초기화 되기 때문에 밖으로 빼기

title_list = []
score_list = []
rank_list = []
date_list = []

for i in range(20210101,2021032):
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&tg=0&date="+str(i)
    res = req.get(url)
    soup = bs(res.text,"lxml")#parsing
    
    title = soup.select("div.tit5>a")#영화제목
    score = soup.select(".point")#평점
    
    
    
    for j in range(len(title)):
        title_list.append(title[j].text)
        score_list.append(score[j].text)
        rank_list.append(j+1)
        date_list.append(i)


# In[25]:


dic = {"영화":title_list,"평점":score_list,"순위":rank_list,"날짜":date_list}


# In[26]:


df = pd.DataFrame(dic)


# In[27]:


df.set_index("순위",inplace=True)


# In[28]:


df


# #### pandas 를 활용한 날짜 생성 

# In[29]:


date = pd.date_range(start="2021-01-01",end="2021-11-09")


# ### 문자형 포멧팅

# In[33]:


#string format time :strftime
days = date.strftime("%Y%m%d")
days


# In[35]:


import tqdm from tqdm_notebook


# In[36]:


title_list = []
score_list = []
rank_list = []
date_list = []

for i in tqdm_notebooks(days):
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&tg=0&date="+i
    res = req.get(url)
    soup = bs(res.text,"lxml")#parsing
    
    title = soup.select("div.tit5>a")#영화제목
    score = soup.select(".point")#평점
    
    
    
    for j in range(len(title)):
        title_list.append(title[j].text)
        score_list.append(score[j].text)
        rank_list.append(j+1)
        date_list.append(i)


# ### tqdm_notebook

# In[32]:


import tqdm from tqdm_notebook


# In[37]:


print(len(title_list))


# ### iframe 수집 

# In[40]:


res = req.get("https://www.naver.com/shoppingbox/shoppingboxnew/main.nhn?domain=Y%22")


# In[41]:


res


# In[55]:


parsing = bs(res.text,"lxml")
x = parsing.select("div.mall_area>a")


# In[56]:


for i in x:
    print(i.text)


# In[174]:


res = req.get("https://movie.naver.com/movie/point/af/list.naver")
res


# In[175]:


soup = bs(res.text,"lxml")


# In[176]:


soup.select("td.title")[0]


# ### tag 삭제

# In[177]:


a = soup.select("a.movie.color_b")
div = soup.select("div.list_netizen_score")
a2 = soup.select("a.report")


# In[121]:


# extract() : 태그를 삭제 시켜주는 함수


# In[179]:


for i in a:
    i.extract()


# In[180]:


for i in div:
    i.extract()


# In[181]:


for i in a2:
    i.extract()


# In[138]:


#strip() : 개행이나 tab 삭제 함수
soup.select("td.title")[0].text.strip()


# In[168]:


a


# In[178]:


score = soup.select("div.list_netizen_score>em")
score


# In[184]:


review = soup.select("td.title")
review


# In[186]:


#길이가 같다면 반복문을 한 번에 돌릴 수 있다.
title_list = []
score_list = []
review_list = []

for i in range(len(a)):
    title_list.append(a[i].text.strip())
    score_list.append(score[i].text.strip())
    review_list.append(review[i].text.strip())


# In[187]:


dic = {"영화제목":title_list,"평점":score_list,"리뷰":review_list}


# In[190]:


cnt = range(1,11)


# In[191]:


df = pd.DataFrame(dic, index=cnt) #0부터 시작하는 게 보기 불편하니 index속성 사용


# In[192]:


df


# In[194]:


df["평점"] #siries 형태


# In[195]:


df["평점"]=="10" #boolean 


# In[197]:


df["리뷰"][df["평점"]=="10"]


# In[198]:


df.iloc[0:5,0]


# In[200]:


df.loc[:,"영화제목":"평점"]


# In[ ]:




