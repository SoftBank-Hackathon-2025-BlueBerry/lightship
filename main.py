import os
import uvicorn

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_hello_world():
    html_content = """
    <html>
        <head>
            <title>FastAPI Hello World</title>
            <style>
                body { font-family: sans-serif; display: grid; place-items: center; min-height: 90vh; background-color: #f4f4f4; }
                h1 { color: #333; }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)