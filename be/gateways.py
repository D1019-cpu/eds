from services.services import app 
import uvicorn 
from fastapi.middleware.cors import CORSMiddleware 


if __name__ == '__main__':
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://localhost:8001"],
        allow_methods=['*'],
        allow_headers=['*']
    )

    uvicorn.run(app, host="0.0.0.0", port=8000)
