import os
import cx_Oracle
import time
import requests
import numpy as np 
from bs4 import BeautifulSoup
URL = "http://ticket2.movie.daum.net/Movie/MovieRankList.aspx"
res = requests.get(URL)
soup = BeautifulSoup(res.content, 'lxml')
box = soup.find_all('div', class_="desc_boxthumb")
# count = 0
data = []
for movie in box:  
    title, ranking = movie.find('strong', class_="tit_join"), movie.find('em', class_="emph_grade")
    movie, grade = title.get_text().strip(), ranking.get_text().strip()
    # print(movie, grade)
    list2 = [movie, grade]#movie, grade를 list(이름,평점)로 가진 형태로 만듦
    data.append([movie,grade])#data에 list2의 모든데이터를 가지고 있는 리스 형태로 변환