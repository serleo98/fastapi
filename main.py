from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_request(request: Request, call_next):
    body = await request.body()
    headers = dict(request.headers)
    print("Solicitud recibida:", request.method, request.url.path)
    print("Encabezados de la solicitud:", headers)
    print("Cuerpo de la solicitud:", body.decode())
    print("---")

    response = await call_next(request)

    return response

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}

@app.post("/path")
async def demo_post():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}

@app.post("/payments/notify")
async def demo_post():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}
    
@app.post("/path-error")
async def demo_post():
    raise HTTPException(status_code=400, detail="This is an error message. Please use a POST request to transform the text to uppercase.")

@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
