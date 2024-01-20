import importlib
import json
import os

import fastapi
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)


@app.get("/")
async def root():
    return {"status": "Alive"}


if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)
        os.environ['phisherman'] = config.get("phisherman-api-key")

    print("Starting server...")
    for file in os.listdir("api/route"):
        if file.endswith(".py"):
            importlib.import_module(f"api.route.{file[:-3]}").setup(app)

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
