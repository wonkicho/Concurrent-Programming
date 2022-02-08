#100까지의 숫자를 3중 for문 을 통한 연산 진행 -> cpu bound로 인해 실행 진행 불가
def cpu_bound_func(number:int):
    total = 1
    arrange = range(1, number + 1)
    for i in arrange:
        for j in arrange:
            for k in arrange:
                total *= i * j * k
                
    return total

if __name__ == "__main__":
    result = cpu_bound_func(10)
    print(result)