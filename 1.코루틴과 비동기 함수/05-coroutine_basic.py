import asyncio

#일반적인 서브루틴
def hello_world():
    print("hello world")
    return 123

#await 은 코루틴 안에서 사용해야함
#await 객체는 코루틴, 태스크, 퓨처
async def hello_world():
    print("hello world")
    return 123

if __name__ == "__main__":
    asyncio.run(hello_world())