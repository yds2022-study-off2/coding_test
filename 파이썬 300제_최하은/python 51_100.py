#!/usr/bin/env python
# coding: utf-8

# In[6]:


#51
movie_rank = ["닥터스트레인지","스플릿","럭키"]
print(movie_rank)


# In[7]:


#52
a = movie_rank
a.append("배트맨")
print(a)


# In[8]:


#53 list.insert(index, data) 메서드 몰랐음.
movie_rank.insert(1,"슈퍼맨")

print(movie_rank)


# In[10]:


#54
movie_rank.drop("럭키")

print(movie_rank)


# In[11]:


del movie_rank[3]

print(movie_rank)


# In[12]:


#55
del movie_rank[2:]

print(movie_rank)


# In[13]:


#56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)


# In[17]:


#57
nums = [1, 2, 3, 4, 5, 6, 7]

print("max:" max(nums))
print("min:" min(nums))


# In[22]:


# 문자열이랑 함수 사이에 쉼표 있어야함
print("max:", max(nums))
print("min:", min(nums))


# In[23]:


#58
nums = [1, 2, 3, 4, 5]

print(sum(nums))


# In[24]:


#59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook))


# In[27]:


#60 리스트에는 avg(), mean() 같은게 없는듯
nums = [1, 2, 3, 4, 5]

print(sum(nums)/len(nums))


# In[28]:


#61
price = ['20180728', 100, 130, 140, 150, 160, 170]

print(price[1:])


# In[32]:


#62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])


# In[33]:


#63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])


# In[34]:


#64
nums = [1, 2, 3, 4, 5]

print(nums[::-1])


# In[39]:


#65
interest = ['삼성전자', 'LG전자', 'Naver']

print(interest[0],interest[2])


# In[42]:


#66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest)


# In[43]:


# 리스트의 요소들을 쉼표와 따옴표 없이 공백으로 출력하기 위해서 " ".join(list) 메서드를 사용함

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))


# In[44]:


#67
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print("/".join(interest))


# In[45]:


#68
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))


# In[46]:


#69
string = "삼성전자/LG전자/Naver"

interest = string.split("/")
print(interest)


# In[49]:


#70
data = [2, 4, 3, 1, 5, 10, 9]

sort(data)


# In[50]:


# 정렬하는 메서드는 list.sort() / 변수 = sorted(list) 형태로 사용함
data.sort()
print(data)
#or
data2 = sorted(data)
print(data2)


# In[54]:


#71
my_variable = ()

print(type(my_variable))


# In[55]:


#72
movie_rank = ("닥터스트레인지","스플릿","럭키")
print(movie_rank)


# In[56]:


#73
a =(1)

print(type(a), a)


# In[57]:


#tuple에 하나의 데이터를 저장할 때는 원소 뒤에 쉼표 (원소 ,)를 입력해야함
a =(1,)

print(type(a), a)


# In[58]:


#74 tuple은 immutable한 자료형이기 때문에 값을 변경할 수 없기 때문이다.
t = (1, 2, 3)
t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment


# In[61]:


#75 t가 바인딩하는 데이터 타입은 tuple이다.
'''원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 
사용자 편의를 위해 괄호 없이도 동작합니다.'''
t = 1, 2, 3, 4
print(type(t))


# In[62]:


#76 tuple은 값을 수정할 수 없기 때문에 새로운 tuple을 만들어 다시 바인딩을 시켜야 한다.
t = ('a', 'b', 'c')

t = ('A', 'b', 'c')
print(t)


# In[63]:


#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')

interest.astype(list)
print(interest)


# In[64]:


interest = ('삼성전자', 'LG전자', 'SK Hynix')

interest = [print(interest)]
print(interest)


# In[69]:


# tuple을 list로 바꾸려면 list(tuple) 함수를 사용한다.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
a = list(interest)
print(a)


# In[70]:


#78
interest = ['삼성전자', 'LG전자', 'SK Hynix']

a = tuple(interest)

print(a)


# In[147]:


#79 a,b,c 각각에 tuple의 원소들이 바인딩되어 3번씩 9개가 출력될 것이다. -> 아니네...
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

print(type(a))
print(type(temp))


# In[76]:


#tuple unpacking 이래서 tuple만 되는줄 알았는데 리스트도 되는듯?ㄴㄴ언팩킹 뜻이
#tuple로 packing되어있는걸 unpacking 한다는 뜻.
temp = ['apple', 'banana', 'cake']
a,b,c = temp

print(a,b,c)
print(a)


# In[73]:


#80
a = (range(2,100,2))
print(a)


# In[74]:


# tuple을 만드려면 ()만 씌우는게 아니라 tuple() 함수를 사용해야한다.
a = tuple(range(2,100,2))
print(a)


# In[88]:


#81
# 뭐지
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

a,b,c,d,e,f,g,h,i,*j = scores
valid_score = a,b,c,d,e,f,g,h,i

*valid_score2, a, b = scores

print(valid_score)
print(valid_score2)


# In[85]:


#82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores

print(valid_score)


# In[89]:


#83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

a, *valid_score, b = scores

print(valid_score)


# In[90]:


#84

temp ={}

print(type(temp))


# In[98]:


#85

아이스크림 = {"메로나":1000, "폴라포":1200, "빵빠레":1800}

print(아이스크림)


# In[100]:


#86 dictionary에 값 추가하기.

#아이스크림={"죠스바":1200,"월드콘":1500}
#print(아이스크림)

아이스크림["죠스바"] = 1200
아이스크림["월드콘"] = 1500
print(아이스크림)


# In[102]:


ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print("메로나 가격:",ice["메로나"])


# In[103]:


ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice["메로나"] = 1300

print(ice)


# In[105]:


#89
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
del ice["메로나"]
print(ice)


# In[ ]:


#90 dic안에 "누가바"라는 key가 존재하지 않기 때문.
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'


# In[110]:


#91
inventory = {"메로나": {"가격":300, "재고":20}, "비비빅":{"가격":400,"재고":3},"죠스바": {"가격":250, "재고":100}}
inventory2 = {"메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
print(inventory)
print(inventory2)


# In[116]:


#92
print(inventory2["메로나"][0],"원")


# In[117]:


#93
print(inventory2["메로나"][1],"개")


# In[118]:


#94

inventory2["월드콘"] = [500,7]
print(inventory2)


# In[124]:


keys = list(print(keys.inventory2))


# In[123]:


# keys를 dic뒤에 소괄호랑 같이 붙여야함. 문제를 제대로 읽어...
ice = list(inventory2.keys())
print(ice)


# In[125]:


#96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(ice)


# In[126]:


icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

price = list(icecream.values())
print(sum(price))


# In[132]:


#98 
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)


# In[134]:


#99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = zip(keys,vals)
print(result)


# In[144]:


# zip함수의 파라미터로 key와 value에 해당하는 튜플을 "순서대로" 넣고,
#dict로 감싸주면 key와 value가 매칭된 dic를 만들 수 있다.
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))

print(result)
print(result["apple"])


# In[145]:


#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))

print(close_table)


# In[ ]:


#51~100 TIL

#53 list.insert(index, data) 메서드 몰랐음.
#54 del movie_rank[3] -> 리스트의 4번째 요소 삭제
#57 # 문자열이랑 함수 사이에 쉼표 있어야함
print("max:", max(nums))
#66 리스트의 요소들을 쉼표와 따옴표 없이 공백으로 출력하기 위해서 " ".join(list) 메서드를 사용함
#70 정렬하는 메서드는 list.sort() or 변수 = sorted(list) 형태로 사용함
#73 tuple에 하나의 데이터를 저장할 때는 원소 뒤에 쉼표 (원소 ,)를 입력해야함
#77 tuple을 list로 바꾸려면 list(tuple) 함수를 사용한다.
#79 a,b,c 각각에 tuple의 원소들이 바인딩되어 3번씩 9개가 출력될 것이다. -> 아니네... 양쪽 숫자가 똑같으면 unpacking돼서 변수에 각각 바인딩되고, 더이상 튜플이 아니기 때문에 unpacking이라고 함
temp = ('apple', 'banana', 'cake')
a, b, c = temp
#80 range함수를 사용해서 tuple을 만드려면 ()만 씌우는게 아니라 tuple() 함수를 사용해야한다.
a = tuple(range(2,100,2))
print(a)
#82 *를 이용하여 unpacking할 원소를 정할 수 있다.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores  -> scores에서 앞의 2개의 원소를 제외하고 나머지만 valid_score라는 변수에 바인딩.
#86 dictionary에 값 추가하기.
-기존 dic
아이스크림 = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
-추가할 요소 dic이름[key] = value
아이스크림["죠스바"] = 1200
아이스크림["월드콘"] = 1500
#89 딕셔너리 items 삭제. 
del ice["메로나"]
#91 딕셔너리 value값으로 여러개 넣을때 {} 아니고 []
inventory = {"메로나": {"가격":300, "재고":20}, "비비빅":{"가격":400,"재고":3},"죠스바": {"가격":250, "재고":100}}
inventory2 = {"메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
#92 딕셔너리 인덱싱(val이 여러개일때)
 dic[key][val idx]
print(inventory2["메로나"][0],"원")
#94 dic에서 vals뽑아서 리스트 만들기.
ice = list(inventory2.keys())
#98 딕셔너리 합치기
dic1
dic2
dic1.update(dic2)
#99 keys, vals 튜플 dic으로 만들기(순서대로 넣어야함)
변수 = zip(keys,vals)

