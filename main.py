from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
from PIL import Image
from rembg import remove
from io import BytesIO

app = FastAPI()

@app.post("/remove_bg/")
async def remove_bg(file: UploadFile = File(...)):
    """
    Removes the background from an uploaded image file.
    """
    try:
        # Read the uploaded file
        contents = await file.read()
        input_image = Image.open(BytesIO(contents))

        # Ensure image is in a format rembg can handle
        input_image = input_image.convert("RGBA")

        # Remove the background
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
