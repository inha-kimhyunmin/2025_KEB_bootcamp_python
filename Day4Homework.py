# V3.8) kwargs를 사용한 데코레이터 예제

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function Name : {func.__name__}")
        print(f"Arguments : {args}")
        print(f"Keyword Arguments : {kwargs}")
        result = func(*args, **kwargs)
        return result

    return wrapper


@log_decorator
def greet(name, greeting="안녕하세요", age=None):
    return f"{greeting}, {name} (age : {age})" if age else f"{greeting}, {name}"

#if age 저 구문은 age를 받지 못했으면 greeting과 name만 출력한다.
#age의 default값이 0이니까


print(greet("인하"))
print(greet("James", "Hello"))
print(greet("James", "Hello", 10))
print(greet("James", greeting="Nihao",
            age=20))  # 이렇게 하면 james는 튜플(가변인자)로 받고, 뒤는 key-value값 형태로 전달해서 keyword argument로 넘겨진다.
