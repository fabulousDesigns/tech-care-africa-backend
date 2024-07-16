from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import customers, orders

app = FastAPI(
    title="Tech Care for All Africa API",
    description="API for managing customers and orders",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Tech Care for All Africa API"}


app.include_router(customers.router)
app.include_router(orders.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)