from fastapi import APIRouter

router = APIRouter()

# Inicio del server: py -m uvicorn products:app --reload

@router.get("/products")
async def products():
    return ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"],