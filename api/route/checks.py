from fastapi import APIRouter
from fastapi.responses import JSONResponse
from back.checks import jaro, levenshtein, regex

router = APIRouter()

regex_class = regex.RegexCheck()

@router.get("/regex")
async def regex(url: str):
    return JSONResponse(
        {
            "status": "success",
            "response": regex_class.check_url(url)
        }
    )


def setup(app):
    app.include_router(router, prefix="/checks")
