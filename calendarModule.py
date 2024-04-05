#!/usr/bin/env python
# coding: utf-8

# In[7]:





# 인수로 연도를 넘겨받아 윤년, 평년을 판단해서 윤년이면 True, 평년이면 False를 리턴하는 isLeapYear(year) 함수를 만든다.

# In[14]:


def isLeapYear(year):
    #연도가 4로 나눠 떨어지고 100으로 나눠 떨어지지 않거나 400으로 나눠 떨어지면 윤년, 그렇지 않으면 평년
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
########


# 인수로 년, 월을 넘겨받아 그 달의 마지막 날짜를 리턴한는 lastDay(year, month)함수를 만든다.

# In[16]:


def lastDay(year, month) :
    #각 달의 마지막 날짜를 기억하는 리스트를 만든다.
    m = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #인수로 넘겨받은 연도에 해당되는 2월의 마지막 날짜를 확정한다.
    m[1] = 29 if isLeapYear(year) else 28
    #마지막 날짜를 리턴시킨다.
    return m[month - 1]


# 인수로 년, 월, 일을 넘겨받아 1년 1월 1일부터 지나온 날짜의 합계를 리턴하는 totalDay(year, month, day) 함수를 만든다.

# In[23]:


def totalDay(year, month, day):
    #인수로 넘어온 연도가 다 지나지않았으므로 1년 1일부터 전년도 12월 31일까지 지난 날짜를 계산한다.
    total = (year - 1) * 365 + ((year - 1) // 4) - ((year - 1) // 100) + ((year - 1) // 400)
    #전년도 12월 31일까지 지난 날짜에 전달까지 지난 날짜를 더한다.
    for i in range(1, month):
        total += lastDay(year, i)
    ########
    #전달까지 지난 날짜에 일을 더해서 리턴한다.
    return total + day;


# 인수로 년, 월, 일을 넘겨받아 요일을 계산해서 숫자로 리턴하는 weekDay(year, month, day) 함수를 만든다  
# 일(0), 월(1), 화(2), 수(3), 목(4), 금(5), 토(6)

# In[25]:


def weekDay(year, month, day):
    return totalDay(year, month, day) % 7


# 테스트

# In[ ]:


#파이썬 파일 1개만 사용할 때는 if __name__ == '__main__' : 를 사용하나 사용하지 않으나 아무런 차이가 없다.
#현재 파이썬 파일이 다른 파이썬 파일에서 모듈로 import 된다면 if __name__ == '__main__' : 블록 내부의 코드는 실행되지 않는다.
if __name__ == '__main__' : 
    print(isLeapYear(2024))
    print(lastDay(2024, 2))
    print(totalDay(2024, 3, 8))
    print(weekDay(2024, 3, 8))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




