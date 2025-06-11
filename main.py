from fastapi import FastAPI

from app.route import user_route

from app.models.database import engine, Base


Base.metadata.create_all(bind=engine)
# Base.metadata.drop_all(bind=engine)


app = FastAPI()

# app.include_router(authentication.router)

app.include_router(user_route.router)
