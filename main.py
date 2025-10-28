from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.infrastructure.api.routes import point_turism_router
from app.infrastructure.api.routes import category_router

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
 
app.include_router(point_turism_router.router)
app.include_router(category_router.router)
