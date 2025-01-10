from PIL import Image, ImageEnhance
import io

def enhance_image(image_bytes: bytes) -> bytes:
    image = Image.open(io.BytesIO(image_bytes))

    enhance_brightness = ImageEnhance.Brightness(image)
    enhanced_image = enhance_brightness.enhance(1.1)
    enhancer_contrast = ImageEnhance.Contrast(enhanced_image)
    enhanced_image = enhancer_contrast.enhance(1.1)
    enhancer_sharpness = ImageEnhance.Sharpness(enhanced_image)
    enhanced_image = enhancer_sharpness.enhance(2.0)

    output_buffer = io.BytesIO()
    enhanced_image.save(output_buffer, format="PNG")
    return output_buffer.getvalue()