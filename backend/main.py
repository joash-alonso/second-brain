from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Base entry point

    Returns:
        dict[str]: A simple message
    """
    return {"message": "Hello, world!"}
