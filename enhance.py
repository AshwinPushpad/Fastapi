from PIL import Image, ImageEnhance
import io

def enhance_image(image_bytes: bytes) -> bytes:
    image = Image.open(io.BytesIO(image_bytes))

    enhance_brightness = ImageEnhance.Brightness(image)
    enhanced_image = enhance_brightness.enhance(1.1)
    enhance_contrast = ImageEnhance.Contrast(enhanced_image)
    enhanced_image = enhance_contrast.enhance(1.1)
    enhance_sharpness = ImageEnhance.Sharpness(enhanced_image)
    enhanced_image = enhance_sharpness.enhance(2.0)
    enhance_color = ImageEnhance.Color(enhanced_image)
    enhanced_image = enhance_color.enhance(2.0)

    output_buffer = io.BytesIO()
    enhanced_image.save(output_buffer, format="PNG")
    return output_buffer.getvalue()