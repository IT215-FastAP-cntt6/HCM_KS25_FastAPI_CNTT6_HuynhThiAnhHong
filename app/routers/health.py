from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.response import success_response


router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("")
def health_check(
    db: Session = Depends(get_db)
):
    try:
        db.execute(text("SELECT 1"))

        return success_response(
            message="System is healthy",
            data={
                "api": "running",
                "database": "connected"
            }
        )

    except Exception:
        return JSONResponse(
            status_code=503,
            content={
                "success": False,
                "message": "Database connection failed",
                "status_code": 503,
                "data": {
                    "api": "running",
                    "database": "disconnected"
                }
            }
        )