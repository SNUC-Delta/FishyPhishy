from fastapi import APIRouter
from fastapi.responses import JSONResponse
from back.checks import jaro, levenshtein, regex

router = APIRouter()

regex_class = regex.RegexCheck()
jaro_class = jaro.JaroWinkler()
levenshtein_class = levenshtein.Levenshtein()


@router.get("/regex")
async def regex(url: str):
    return JSONResponse(
        {
            "status": "success",
            "response": regex_class.check_url(url)
        }
    )


@router.get("/jaro")
async def jaro(test: str, reference: str):
    return JSONResponse(
        {
            "status": "success",
            "response": jaro_class.jaro_winkler(test, reference)
        }
    )


@router.get("/levenshtein")
async def levenshtein(test: str, reference: str):
    return JSONResponse(
        {
            "status": "success",
            "response": levenshtein_class.levenshtein_distance(test, reference)
        }
    )


@router.get("/all")
async def test_all(test: str, reference: str):
    return JSONResponse(
        {
            "status": "success",
            "response": {
                "regex": regex_class.check_url(test),
                "jaro": jaro_class.jaro_winkler(test, reference),
                "levenshtein": levenshtein_class.levenshtein_distance(test, reference)
            }
        }
    )


def setup(app):
    app.include_router(router, prefix="/checks")
