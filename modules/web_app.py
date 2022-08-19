from fastapi import FastAPI
from modules.routers import (
    users,
    admins

)
app = FastAPI(title="manoapp", description="test app")

app.include_router(users.router)
app.include_router(admins.router)