import time
import os
import threading

"""
전역 인터프리터 잠금(GIL, Global interpreter Lock)
한번에 1개의 스레드만 유지하는 락
하나의 스레드가 다른 스레드 차단하며 제어를 얻는 것을 막음
멀티 스레딩 - io bound에 유용
            - cpu bound에는 gil에 의해 원하는 결과 얻지 못함
            
멀티 프로세싱을 통해 멀티스레딩 단점 보완
"""

nums = [50, 63, 32]

def cpu_bound_func(num):
    print(f'{os.getpid()} process | {threading.get_ident()} thread')
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
                
    return total

def main():
    for num in nums:
        cpu_bound_func(num)
        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)