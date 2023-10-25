from fastapi import APIRouter
from back.assets.pretty_response import JSONResponse
from back.models.similarity.similarity import Similarity

router = APIRouter()
model = Similarity()
print("Model loaded")


def get_similarity(url1: str, url2: str):
    if not url1 or not url2:
        return 0.0
    if url1 == url2:
        return 1.0
    if "None" in url1 or "None" in url2:
        return 0.0
    return float(model.get_image_embeddings(url1, url2))


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
