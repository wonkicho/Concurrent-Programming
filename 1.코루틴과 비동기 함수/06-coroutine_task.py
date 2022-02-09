import time
import asyncio

#동기적 코드 실행 예시
async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime) #await 비동기 함수 처리하는 키워드, 단순 wait이 아님
    #time.sleep(mealtime)
    print(f"{name} 식사완료, {mealtime} 시간 소요...")
    print(f"{name} 그릇 수거 완료")
    

async def main():
    #예약 과정
    task1 = asyncio.create_task(delivery("A", 2))
    task2 = asyncio.create_task(delivery("B", 1))
    
    await task2
    await task1
    
    #await task 2와 동일    
    await delivery("A", 2)
    
    
if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)