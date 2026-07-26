from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user_router
from app.routers import user_router, auth_router   # ← auth_router を追加
from app.routers import keyword_router
from app.routers import personality_router
from app.routers import connection_router
from app.routers import user_keyword_router
from app.routers import user_personality_router

app = FastAPI(title="My API", version="1.0.0")

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # Next.js のオリジンを許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(auth_router)   # ← 追加
app.include_router(keyword_router)
app.include_router(personality_router)
app.include_router(connection_router)
app.include_router(user_keyword_router)
app.include_router(user_personality_router)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}