import json
import typing

from fastapi.responses import JSONResponse as UglyJSONResponse


class JSONResponse(UglyJSONResponse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=2,
            separators=(",", ":"),
        ).encode("utf-8")

    def json(self, content: str):
        return json.loads(content)
