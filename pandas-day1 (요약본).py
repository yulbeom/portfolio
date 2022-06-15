#!/usr/bin/env python
# coding: utf-8

# In[4]:


# pandas 를 사용하기 위하여 모듈 import
import pandas as pd

# dictionary와 유사한 시리즈를 생성
dict_a = {'a':1, 'b':2, 'c':3}  # 딕셔너리의 키가 인덱스, 값이 값으로 
sr = pd.Series(dict_a)  # 딕셔너리의 자료를 시리즈로 변환

# 자료의 타입을 확인
print(type(dict_a), type(sr))

print(dict_a)
print()
print(sr)
sr


# In[9]:


# series -> class  : 인덱스배열 index, 데이터 값 배열 values
print(sr.index)  # -> ['a','b','c']
print(type(sr.values))  # ->[ 1  2  3]
print(sr[0:2])  # 숫자 인덱스로 자료를 가져옴, 숫자는 시작 포함, end 포함 안함
print(sr['a':'c'])    # 인덱스 명으로 검색, 시작과 마지막 모두 포함


# In[15]:


#  튜플 자료 또는 리스트를 시리즈로, 인덱스명 설정하면서 시리즈로 변환
tup_data = ('영인', '2010-05-06', '여', True)

sr1 = pd.Series(tup_data, index=['이름', '생년월일', '성별','학생여부'])
print(sr1[0], sr1['이름'])   # 영인 영인
print(sr1[['이름', '성별']], '\n', sr1[[0,2]])     # 영인 여    
# 시리즈[인덱스명] , 시리즈[숫자 인덱스]
# 범위로  -> 시리즈[인덱스명 : 인덱스명 ],  시리즈[숫자인덱스 : 숫자인덱스]
# 여러 개를 가져옴
# 시리즈[ [인덱스명, .. ] ],   시리즈[ [ 0, 2]]


# In[29]:


# 딕셔너리로 데이터프레임 생성 : 키가 컬럼으로 
# 시리즈가 여러개 모여서 데이터프레임이 됨
dict_data = {'c0': [1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],'c3':[10,11,12],
            'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
print(df)
print(df.index)
print(df.values)
print(df.columns)
list(df.items())
print(df['c0'].dtype)
df.info()


# In[35]:


# 2차원 배열을 데이터프레임으로 생성, 인덱스와 컬럼을 지정
df = pd.DataFrame([[15,'남','덕영중'], [17,'여','수리중']],
                 index=['준서', '예은'],
                 columns=['나이', '성별','학교'])
print(df)
print()
print(df.index)
print()
print(df.columns)


# In[36]:


# 인덱스명을 변경 => '준서','예은' : '학생1', '학생2'
# df.index = 새로운 인덱스 배열 (리스트)
df.index = ['학생1', '학생2' ]
print(df.index)


# In[38]:


# 컬럼명을 변경 => '나이', '성별','학교' : '연령','남녀', '소속'
# df.columns = 새로운 인덱스 배열 (리스트)
df.columns = ['연령','남녀', '소속' ]
df


# In[41]:


# 일부 인덱스명만 변경 df.rename( index={ 기존인덱스 : 새로운인덱스, ..})
# 일부 컬럼명만 변경 df.rename(columns={ 기존컬럼 : 새로운컬럼, ..})
df.rename(index={'학생1':'준서'}, columns={'연령': '나이'})
print(df)  # 기존 데이터프레임 수정 안됨

df.rename(index={'학생1':'준서'}, columns={'연령': '나이'}, inplace=True)
# df


# In[47]:


#  행/ 열 삭제
# 데이터프레임.drop(행 인덱스 또는 배열, axis=0, [inplace=True])
# 데이터프레임.drop(열 이름 또는 배열, axis=1)
df.drop(['나이', '소속'],axis=1)


# In[48]:


# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장 
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')


# In[49]:


# df을 복사해서 df_copy생성
df_copy = df.copy()


# In[51]:


print(df_copy)
# 우현의 자료를 삭제 후 원데이터에 적용
df_copy.drop('우현', axis=0, inplace=True)
df_copy


# In[56]:


df_copy = df.copy()  # 수학과 음악 과목을 삭제후 적용 
df_copy.drop(['수학', '음악'], axis=1, inplace=True)
df_copy


# In[66]:


print(df[['수학', '영어']])   # 데이터프레임의 컬럼을 선택
 print(df)
df.수학  # 데이터프레임.컬럼명


# In[62]:


#  행 선택 : df.iloc[숫자 인덱스], df.loc[인덱스명]
print(df.loc['서준'], df.iloc[0])
print(df.loc['서준' : '우현'], df.iloc[0 : 2])
print()
print(df.loc[['서준','우현']], df.iloc[[0,1]])


# In[65]:


# 행과 열을 선택 : 서준의 수학과 음악 점수 선택
# df.loc[ 행인덱스명, 컬럼명 ]
print(df.loc[ '서준', ['수학','음악'] ])
print(df.loc[ '서준':'우현', ['수학','음악'] ])


# In[67]:


# 서준의 수학 점수를 100으로 수정
df.loc['서준', '수학'] = 100
df


# In[68]:


df.iloc[ : : 2]   # [start : stop : step]


# In[69]:


df.iloc[ : : -1]   # 뒤에서 부터 역순으로 


# In[72]:


exam_data = {'이름':['서준', '우현','인아'],
            '수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)

# 특적 컬럼을 인덱스로 설정 : df.set_index(컬럼명, inplace=True)
df.set_index('이름', inplace=True)
df


# In[74]:


# 새로운 컬럼을 추가 : '국어': 90, 80, 90 을 추가
df['국어'] = [90,80,80]


# In[76]:


print(df)
# 서준과 인아의 국어점수 출력
print(df.loc[ ['서준', '인아'], '국어'])


# In[77]:


# 행 추가 : df.loc['새로운 이름'] = 값 또는 [값, ... ]
df.loc['동규'] = 0
df


# In[79]:


df.loc[3] = 0
df.loc[[3,'인아'], : ]


# In[80]:


# 기존행을 복사하여 새로운 행 추가
df.loc[4] = df.loc['동규']
df


# In[82]:


# index 초기화 : df.reset_index()
df.reset_index(inplace=True)
df


# In[83]:


# 이름을 인덱스 컬럼으로 설정
df.set_index('이름', inplace=True)
df


# In[93]:


df.set_index('수학')
df.reindex([ '서준','우현'])
df


# In[95]:


df.drop([3,4], axis=0, inplace=True)


# In[99]:


print(df.sort_index())  # index값으로 정렬
df.sort_values(by='수학')  # index값으로 정렬


# In[ ]:


# 이름, 국어, 영어, 수학 점수를 입력받아 딕셔너리에 저장한 후
# 해당 자료를 데이터프레임으로 설정
# 이름을 인덱스로 설정해서 결과 출력

students = {'이름':[],
           0:[],
           1:[],
           2:[]}

while True:
    name = input("이름 입력 ")
    if name == 'q':
        break
    students['이름'].append(name)
    score = input("국어 영어 수학 점수 입력 ").split()
    for idx, data in enumerate(score):
        students[idx].append(int(data))


# In[104]:


df = pd.DataFrame(students)
df.columns = ['이름','국어','영어','수학']
df.set_index('이름',inplace=True)


# In[105]:


df

