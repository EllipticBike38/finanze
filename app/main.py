from fastapi import FastAPI
from routers import abbonamenti,auth,transazioni,users,utils
import uvicorn

app=FastAPI()

app.include_router(abbonamenti)
app.include_router(auth)
app.include_router(transazioni)
app.include_router(users)
app.include_router(utils)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info",reload=True)