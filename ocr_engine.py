"""
OCR engine — extracts text from result images (PNG/JPG) and PDFs.
Uses pytesseract (Tesseract OCR) with image pre-processing for better accuracy.
"""

import os
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

# If running locally on Windows, set explicit path. On Linux (Render), it's in the system PATH.
if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def _preprocess_image(image: Image.Image) -> Image.Image:
    """
    Convert to greyscale, upscale if it's a small/compressed image,
    and apply simple thresholding/contrast.
    """
    grey = image.convert('L')
    
    # Upscale ONLY if width is very small (to save Render free tier RAM)
    if grey.width < 1000:
        grey = grey.resize((grey.width * 2, grey.height * 2), Image.Resampling.LANCZOS)
    # Downscale heavily to save Render free tier CPU time, but keep enough resolution for OCR (1600px)
    elif grey.width > 1600:
        ratio = 1600 / grey.width
        grey = grey.resize((1600, int(grey.height * ratio)), Image.Resampling.LANCZOS)
        
    # Pad with 20px white border
    padded = ImageOps.expand(grey, border=20, fill='white')
    # Simple contrast boost
    enhanced = ImageEnhance.Contrast(padded).enhance(2.0)
    return enhanced


def extract_text_from_file(file_path: str) -> str:
    """
    Accept a PDF or image file and return the OCR-extracted text.
    Raises ValueError for unsupported formats.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()
    text = ""

    if ext == '.pdf':
        # pdf2image requires poppler to be installed
        from pdf2image import convert_from_path
        if os.name == 'nt':
            images = convert_from_path(
                file_path,
                dpi=150,
                poppler_path=r'C:\Users\gupta\AppData\Local\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin'
            )
        else:
            images = convert_from_path(file_path, dpi=150)
            
        for img in images:
            processed = _preprocess_image(img)
            text += pytesseract.image_to_string(processed, config='--psm 6') + "\n"

    elif ext in ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp'):
        image = Image.open(file_path)
        processed = _preprocess_image(image)
        text = pytesseract.image_to_string(processed, config='--psm 6')

    else:
        raise ValueError(
            f"Unsupported file format '{ext}'. "
            "Please provide a PDF or image (PNG/JPG/BMP/TIFF)."
        )

    return text
