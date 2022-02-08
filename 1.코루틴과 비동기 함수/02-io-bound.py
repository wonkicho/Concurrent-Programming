def io_bound_func():
    print("값을 입력해주세요")
    input_value = input()
    return int(input_value) + 100

#user가 입력할 때까지 대기, 즉 응답 기다림
#주체가 누구냐에 따라 정의할 수 있음

if __name__ == "__main__":
    result = io_bound_func()
    print(result)
    