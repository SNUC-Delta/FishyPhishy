from fastapi import APIRouter
from fastapi.responses import JSONResponse
from back.models.similarity.similarity import Similarity

router = APIRouter()
model = Similarity()


@router.get("/image")
async def image_compare(url1: str, url2):
    return JSONResponse(
        {
            "status": "success",
            "response": float(model.get_image_embeddings(url1, url2))
        }
    )


def setup(app):
    app.include_router(router, prefix="/compare")
