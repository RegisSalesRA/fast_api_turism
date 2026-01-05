from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.infrastructure.api.routes import point_turism_router
from app.infrastructure.api.routes import category_router
from app.infrastructure.api.routes import city_router
from app.infrastructure.api.routes import user_router
from app.infrastructure.api.routes import review_router
from app.infrastructure.api.routes import image_router
from app.infrastructure.api.routes import album_router
from app.infrastructure.api.routes import favorite_router

app = FastAPI(
    title="API Pontos Turísticos",
    description="API de estudo para CRUD e filtros de Pontos Turísticos",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)
app.include_router(point_turism_router.router)
app.include_router(category_router.router)
app.include_router(city_router.router)
app.include_router(image_router.router)
app.include_router(album_router.router)
app.include_router(favorite_router.router)
app.include_router(review_router.router)
