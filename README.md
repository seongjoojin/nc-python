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
