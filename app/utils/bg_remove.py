from rembg import remove
from PIL import Image
import os

async def remove_background(file):

    input_path = f"temp_{file.filename}"
    output_path = f"output_{file.filename}.png"

    # Save the uploaded file
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Process the image
    with open(input_path, "rb") as img_file:
        result = remove(img_file.read())

    # Save the result
    with open(output_path, "wb") as output_file:
        output_file.write(result)

    # Cleanup input file
    os.remove(input_path)

    return output_path
