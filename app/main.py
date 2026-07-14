from fastapi import FastAPI

from app.database.database import Base, engine
import app.models.user

from app.api.user import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CloudDocs")

app.include_router(user_router)





app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "CloudDocs API Running"
    }