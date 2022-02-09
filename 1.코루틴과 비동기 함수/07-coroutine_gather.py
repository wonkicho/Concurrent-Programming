import time
import asyncio

#동기적 코드 실행 예시
async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime) #await 비동기 함수 처리하는 키워드, 단순 wait이 아님
    #time.sleep(mealtime)
    print(f"{name} 식사완료, {mealtime} 시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime
    
async def main():
    #순서대로 동작하게 되어있음
    result = await asyncio.gather(
            delivery("A", 10),
            delivery("B", 3),
            delivery("C", 4),
        )
    
    print(result)#[10, 3, 4], return값이 리스트 형태로 들어감
    
if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)