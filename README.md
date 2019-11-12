# nc-python-web-scraper

Python으로 웹 스크래퍼 만들기

# 0 Introduction

## 0.0 Why learn Python

- 사용하는 곳도 많고 사용되는 용도도 다양한 언어

## 0.2 Requirements

- 구글 크롬

## 0.3 How to Ask for Help

- 목적이 뭔지(너희가 원하는 것)
- 뭐를 해봤는지
- 뭐를 해봤는데 안 되는지
- error가 어떻게 생겼는지 (어떤 에러인지)

## 0.4 Code Python Online

https://repl.it/

# 1 Theory

## 1.0 Data Types of Python

파이썬은 변수 이름은 snake case로 지어줘야함

None : 존재하지 않음

```python
a_string = 'like'
a_number = 2
a_float = 3.14
a_boolean = True
a_none = None
```

## 1.1 Lists in Python

https://docs.python.org/3/library/index.html

https://docs.python.org/3/library/stdtypes.html#list

- list
- tuple

list 는 Mutable Sequence 임 (수정 가능)

```python
days = ["Mon","Tue","Wed","Thur","Fri"]
print(days)
days.append("Sat")
days.reverse()
print(days)
```

## 1.2 Tuples and Dicts

https://docs.python.org/3/library/stdtypes.html#tuples

tuple 은 Immutable Sequence 임 (수정 불가능)

```python
days = ("Mon","Tue","Wed","Thur","Fri")
```

https://docs.python.org/3/library/stdtypes.html#dict

```python
nico = {
    "name": "Nico",
    "age": 29,
    "korean": True,
    "fav_food": ["Kimchi", "Sashimi"]
}

print(nico)
nico["handsome"] = True
print(nico)

```

## 1.3 Built-in Functions

- function은 어떤 행동(기능)을 가지고 있고 계속 반복할 수 있는 것임
- 우리는 행동(기능)을 작성하고 반복해서 재사용하려고 노력함.

https://docs.python.org/3/library/functions.html

```python
print(len("sdfsdfsdfsdf"))
age = "18"
print(type(age))
n_age = int(age)
print(type(n_age))
```

## 1.4 Creating a Your First Python Function

파이썬에서는 함수를 정의한다고 함.

```py
def say_hello():
	print("hello")
	print("bye")

say_hello()
```

## 1.5 Function Arguments

```py
def say_hello(who):
	print("hello", who)

say_hello("evanjin")

def plus(a,b):
	print(a+b)

def minus(a,b=0):
	print(a-b)

plus(2,5)
minus(2)
```

## 1.6 Returns

- function이 return 된 값으로 치환됨
- python은 return하는 순간 function은 종료됨
- 한 번에 하나의 값만 return 할 수 있음

```py
def p_plus(a, b):
    print(a + b)


def r_plus(a, b):
    return a + b


p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result,r_result)
```

## 1.8 Keyworded Arguments

```py
def plus(a, b):
    return a - b


result = plus(b=30, a=1)
print(result)


def say_hello(name, age, are_from, fav_food):
    return f"Hello {name} you are {age} you are from {are_from} you like {fav_food}"


hello = say_hello(
    name="evanjin", age="22", are_from="korean", fav_food="kimchi")
print(hello)
```

## 1.9 Code Challenge!

7가지 function

plus, mius, times, division, negation, power, remainder

```py
def plus(a, b):
    return int(a) + int(b)


def mius(a, b):
    return int(a) - int(b)


def times(a, b):
    return int(a) * int(b)


def division(a, b):
    return int(a) / int(b)


def negation(a):
    return -int(a)


def power(a, b):
    return int(a)**int(b)


def remainder(a, b):
    return int(a) % int(b)
```

## 1.10 Conditionals part One

https://docs.python.org/3/library/stdtypes.html#truth-value-testing

```py
def plus(a, b):
    if type(a) is int and type(b) is int:
        return a - b
    else:
        return None


print(plus(12, "10"))
```

## 1.11 if else and or

https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

https://docs.python.org/3/library/stdtypes.html#comparisons

```py
def age_check(age):
	print(f"you are {age}")
	if age < 18:
		print("you cant drink")
	elif age == 18 or age == 19:
		print("you are new to this")
	elif age > 20 and age < 25:
		print("you are still kind of young")
	else:
		print("enjoy your drink")

age_check(18)
```

## 1.12 for in

```py
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for day in days:
	if day is "Wed":
		continue;
	else:
		print(day)
```

## 1.13 Modules

- 기능의 집합

```py
from math import ceil, fsum as num

print(ceil(1.5))
print(num([-1.5, 1, 5]))
```

# 2 Building a Job Scrapper

## 2.0 What is Web Scrapping

- 웹 상의 데이터를 추출하는 하는 것을 말함

## 2.1 What are We Building

https://kr.indeed.com/

https://stackoverflow.com/jobs

위 사이트에서 일자리를 가져온 뒤 엑셀 시트에 옮길 것

## 2.2 Navigating with Python

https://requests.readthedocs.io/en/master/

https://github.com/psf/requests

**가상환경 생성**

`python3 -m venv web-scraper`

**가상환경 활성화**

`source web-scraper/bin/activate`

**가상환경 비활성화**

`deactivate`

**가상환경 삭제**

`deactivate`

`sudo rm -rf web-scraper`

**requests 설치**

`python -m pip installå requests`

**beautifulsoup4 설치**

https://www.crummy.com/software/BeautifulSoup/

`python -m pip install beautifulsoup4`

## 2.3 Extracting Indeed Pages

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

soup은 데이터를 추출함

## 2.9 StackOverflow Pages

1. 페이지를 가져올 것
2. request를 만들 것
3. job을 추출하기
