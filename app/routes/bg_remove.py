from fastapi import APIRouter, UploadFile, File
from app.utils.bg_remove import remove_background
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/bg_remove")
async def remove_bg(file: UploadFile = File(...)):

    output_path = await remove_background(file)
    return FileResponse(output_path, media_type="image/png")
