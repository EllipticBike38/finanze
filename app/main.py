from fastapi import FastAPI
from routers import abbonamenti,auth,transazioni,users,utils

app=FastAPI()

app.include_router(abbonamenti)
app.include_router(auth)
app.include_router(transazioni)
app.include_router(users)
app.include_router(utils)