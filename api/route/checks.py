from urllib.parse import urlparse

from fastapi import APIRouter
from back.assets.pretty_response import JSONResponse
from back.checks import jaro, levenshtein, regex

from back.assets import internet


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


@router.get("/urlscan")
async def urlscan(test: str):
    base_url = "https://urlscan.io/api/v1/search/?q=domain:{}&size=1"
    domain = urlparse(test).netloc
    url = base_url.format(domain)
    response = await internet.get_json(url)
    return JSONResponse(
        {
            "status": "success",
            "response": response
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
