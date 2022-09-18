import uvicorn
import requests
from fastapi import FastAPI, status
from starlette.responses import JSONResponse
app = FastAPI()


@app.get("/")
async def root():
    url = 'https://metals-api.com/api/latest?access_key=4033gl3s72b3k5ztkj54inf2vi3pqy2v22x05o6g040jq025z4eypp67dkbp'
    headers = {'Accept': 'application/json'}

    try:
        res = requests.get(url, headers=headers)
        content = {
            'result': res.json()
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)
    except:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={'error': 'There is a problem with the server, please come back later'})


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
