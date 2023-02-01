from fastapi import FastAPI
from routers import abbonamenti,auth,transazioni,users,utils
from errors.errors import handlers,errors
import uvicorn

app=FastAPI()

app.include_router(abbonamenti)
app.include_router(auth)
app.include_router(transazioni)
app.include_router(users)
app.include_router(utils)

for h,e in zip(handlers,errors):
    app.add_exception_handler(e, h)
app.add_exception_handler(Exception, handlers[1])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info",reload=True)