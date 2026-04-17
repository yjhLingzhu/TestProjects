from fastapi import FastAPI, Depends

app = FastAPI()


# 装饰器1
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)

    return wrapper


# 装饰器2
def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)

    return wrapper


# 路由装饰器1
@app.get("/route1")
@decorator1
def route1():
    return {"message": "Route 1"}


# 路由装饰器2
@app.get("/route2")
@decorator2
def route2():
    return {"message": "Route 2"}


# 同时使用多个装饰器
@app.get("/route3")
@decorator1
@decorator2
def route3():
    return {"message": "Route 3"}


@app.get("/route4")
def route4():
    return {"message": "Route 4"}


if __name__ == "__main__":
    # 测试 YYY RRR
    import uvicorn
    uvicorn.run(app="my_decorator:app", host="0.0.0.0", reload=True)
