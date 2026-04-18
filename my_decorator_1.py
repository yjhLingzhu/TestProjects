from fastapi import FastAPI
import functools  # 新增导入

app = FastAPI()

# 修改后的装饰器1
def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper

# 修改后的装饰器2
def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)
    return wrapper

# 路由装饰器应该在自定义装饰器上方
@app.get("/route1")
@decorator1  # 应用在路由装饰器下方
def route1():
    return {"message": "Route 1"}

@app.get("/route2")
@decorator2
def route2():
    return {"message": "Route 2"}

@app.get("/route3")
@decorator1
@decorator2
def route3():
    return {"message": "Route 3"}

# 未使用装饰器的路由不受影响
@app.get("/route4")
def route4():
    return {"message": "Route 4"}


if __name__ == "__main__":
    # T1 DK
    # 我的可以投产
    # hahah投产
    import uvicorn
    uvicorn.run(app="my_decorator_1:app", host="0.0.0.0", reload=True)
