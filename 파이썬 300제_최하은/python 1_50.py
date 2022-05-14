#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello World')


# In[2]:


print("Mary's cosmetics")


# In[3]:


print('신씨가 소리질렀다. "도둑이야".')


# In[5]:


print("C:\Windows")


# In[6]:


print("안녕하세요.\n만나서\t\t반갑습니다.")


# In[7]:


print ("오늘은", "일요일")


# In[8]:


print("naver;kakao;sk;samsung")


# In[9]:


#sep="데이터 사이에 넣고 싶은 것"
print("naver","kakao","samsung", sep=";")


# In[10]:


print("naver","kakao","sk","samsung", sep="/")


# In[11]:


#end="줄바꿈 안되게 해주는거"
print("first", end="");print("second")


# In[12]:


5/3


# In[14]:


#삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
print(삼성전자*10)


# In[15]:


시가총액 = 29800000000000
현재가 = 50000
PER = 15.79

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))


# In[18]:


s = "hello"
t = "python"

print(s+"!", t)


# In[20]:


2+2*3


# In[21]:


a = "132"
print(type(a))


# In[22]:


num_str = "720"
print(int(num_str))


# In[24]:


num = 100
num = str(num)
print(type(num))


# In[25]:


float("15.79")


# In[26]:


year = "2020"
year = int(year)
print(year, year+1, year+2)


# In[27]:


#에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 
#총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
월금액 = 48584
print(월금액*36)


# In[31]:


letters = 'python'

print(letters[0],letters[2])


# In[33]:


license_plate = "24가 2210"

print(license_plate[-4:])


# In[34]:


string = "홀짝홀짝홀짝"

print(string[::2])


# In[35]:


string = "PYTHON"
print(string[::-1])


# In[36]:


phone_number = "010-1111-2222"

print(phone_number.replace("-"," "))


# In[37]:


phone_number = "010 1111 2222"

print(phone_number.replace(" ",""))


# In[4]:


#변수.split(" ") 겹따옴표 안에 들어가는거 기준으로 나누기. 없으면 공백 기준으로 나눔.
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])


# In[5]:


string = 'abcdfe2a354a32a'

print(string.replace('a','A'))


# In[6]:


print('-'*80)


# In[9]:


t1 = 'python'
t2 = 'java'

a = (t1+ " " +t2+" ")

print(a*4)


# In[13]:


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))


# In[18]:


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))


# In[19]:


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")


# In[22]:


상장주식수 = "5,969,782,550"

상장주식수 = 상장주식수.replace(",","")

print(int(상장주식수), type(int(상장주식수)))


# In[24]:


분기 = "2020/03(E) (IFRS연결)"

분기 = 분기.split("(")

print(분기[0])


# In[25]:


data = "   삼성전자    "

print(data.strip())


# In[26]:


ticker = "btc_krw"

ticker.upper()


# In[27]:


ticker = "BTC_KRW"

ticker.lower()


# In[29]:


#첫번째 글자 대문자해주는 메서드 capitalize
a = "hello"
a = a.capitalize()
a


# In[30]:


#문자열에서 특정 문자로 끝나는지 확인하고 싶을때. 변수.endswith("확인하고 싶은 문자")

file_name = "보고서.xlsx"

file_name.endswith("xlsx")


# In[31]:


#문자열이 특정 문자로 시작하는지 확인하고 싶을때. 변수.startswith("확인하고 싶은 문자")
file_name = "2020_보고서.xlsx"

file_name.startswith("2020")


# In[32]:


a = "hello world"
a.split(" ")


# In[34]:


ticker = "btc_krw"

ticker.split("_")


# In[41]:


date1 = "2020-05-01"

date1.split("-")


