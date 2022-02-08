import requests

#server 에 request
def io_bound_func():
    result = requests.get("https://google.com")
    return result

if __name__=="__main__":
    for i in range(10):
        result = io_bound_func()
    print(result) #<Response [200]>