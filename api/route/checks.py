import asyncio
from urllib.parse import urlparse

from fastapi import APIRouter
from back.assets.pretty_response import JSONResponse
from back.checks import jaro, levenshtein, regex

from back.assets import internet
from api.route import compare

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


async def screenshot(url: str):
    base_url = "https://urlscan.io/api/v1/search/?q=domain:{}&size=1"
    domain = urlparse(url).netloc
    url = base_url.format(domain)
    response = await internet.get_json(url)
    print(response)
    try:
        screenshot_url = response.get("results")[0].get("screenshot")
    except IndexError:
        screenshot_url = None
    return screenshot_url


async def scan_url_json(test: str):
    base_url = "https://urlscan.io/api/v1/search/?q=domain:{}&size=1"
    domain = urlparse(test).netloc
    url = base_url.format(domain)
    response = await internet.get_json(url)
    print(response)
    try:
        screenshot_url = response.get("results")[0].get("screenshot")
    except IndexError:
        screenshot_url = None
    print(screenshot_url)
    return {
            "status": "success",
            "response": response,
            "screenshot_url": screenshot_url
        }

@router.get("/urlscan")
async def urlscan(test: str):
    base_url = "https://urlscan.io/api/v1/search/?q=domain:{}&size=1"
    domain = urlparse(test).netloc
    url = base_url.format(domain)
    response = await internet.get_json(url)
    print(response)
    try:
        screenshot_url = response.get("results")[0].get("screenshot")
    except IndexError:
        screenshot_url = None
    print(screenshot_url)
    return JSONResponse(
        {
            "status": "success",
            "response": response,
            "screenshot_url": screenshot_url
        }
    )


@router.get("/all")
async def test_all(test: str, reference: str):
    s1 = await screenshot(test)
    s2 = await screenshot(reference)
    print(s1)
    print(s2)
    return JSONResponse(
        {
            "status": "success",
            "response": {
                "regex": regex_class.check_url(test),
                "jaro": jaro_class.jaro_winkler(test, reference),
                "levenshtein": levenshtein_class.levenshtein_distance(test, reference),
                "urlscan": await scan_url_json(test),
                "screenshot similarity": compare.get_similarity(
                    s1,
                    s2
                ) if s1 and s2 else 0.0
            }
        }
    )


def setup(app):
    app.include_router(router, prefix="/checks")


if __name__ == "__main__":
    asyncio.run(urlscan("https://www.google.com"))
