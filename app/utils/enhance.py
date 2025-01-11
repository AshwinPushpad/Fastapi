from PIL import Image, ImageEnhance
import os

async def enhance_image(file):

    input_path = f"temp_{file.filename}"
    output_path = f"enhanced_{file.filename}.png"

    # Save the uploaded file
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Open and enhance the image
    with Image.open(input_path) as img:

        enhance_brightness = ImageEnhance.Brightness(img)
        enhanced_image = enhance_brightness.enhance(1.1)
        enhance_contrast = ImageEnhance.Contrast(enhanced_image)
        enhanced_image = enhance_contrast.enhance(1.1)
        enhance_sharpness = ImageEnhance.Sharpness(enhanced_image)
        enhanced_image = enhance_sharpness.enhance(1.7)
        enhance_color = ImageEnhance.Color(enhanced_image)
        enhanced_image = enhance_color.enhance(1.7)
        enhanced_image.save(output_path)

    # Cleanup input file
    os.remove(input_path)

    return output_path
