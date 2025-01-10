import io
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
from PIL import Image
from rembg import remove
from io import BytesIO
from enhance import enhance_image

app = FastAPI()

@app.post("/enhance")
async def enhance_photo(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()

        enhanced_image_bytes = enhance_image(image_bytes)

        return StreamingResponse(
            io.BytesIO(enhanced_image_bytes),
            media_type="image/png",
            headers={"Content-Disposition": "attachment; filename=enhanced_image.png"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error enhancing image: {str(e)}")

@app.post("/remove_bg/")
async def remove_bg(file: UploadFile = File(...)):

    try:
        contents = await file.read()

        output = remove(contents)

        # Convert output to an image
        output_image = Image.open(BytesIO(output))

        # Save the image to an in-memory buffer
        buffer = BytesIO()
        output_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Return the PNG file as a response
        return StreamingResponse(buffer, media_type="image/png", headers={
            "Content-Disposition": f"attachment; filename=background_removed.png"
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/say_hello/")
async def say_hello(data: dict):

    try:
        name = data.get("name")
        return {"out": f"hello {name}"}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
