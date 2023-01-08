import uvicorn

from app.runner.setup import setup

if __name__ == "__main__":
    app = setup()
    uvicorn.run(app, host="0.0.0.0", port=8000)
