from fastapi import APIRouter, UploadFile, File
from app.utils.enhance import enhance_image
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/enhance")
async def enhance(file: UploadFile = File(...)):

    output_path = await enhance_image(file)
    return FileResponse(output_path, media_type="image/png")