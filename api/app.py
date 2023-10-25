import importlib
import os

import fastapi

app = fastapi.FastAPI()


@app.get("/")
async def root():
    return {"status": "Alive"}


if __name__ == "__main__":
    print("Starting server...")
    for file in os.listdir("api/route"):
        if file.endswith(".py"):
            importlib.import_module(f"api.route.{file[:-3]}").setup(app)

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
