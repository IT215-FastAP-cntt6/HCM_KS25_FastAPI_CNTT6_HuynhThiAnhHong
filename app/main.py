from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.config import settings
from app.core.response import error_response
from app.routers.health import router as health_router


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Event Management API",
    debug=settings.DEBUG
)


# HTTP EXCEPTION
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(
            message=str(exc.detail),
            status_code=exc.status_code
        )
    )


# VALIDATION ERROR
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content=error_response(
            message="Validation error",
            status_code=422,
            data=exc.errors()
        )
    )


# GLOBAL EXCEPTION
@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content=error_response(
            message="Internal server error",
            status_code=500
        )
    )


# ROOT
@app.get("/")
def root():
    return {
        "success": True,
        "message": "Event Management API is running"
    }


# HEALTH CHECK
app.include_router(
    health_router,
    prefix="/api/v1"
)