"""
Screenshot to Text Extractor Package

A powerful Python-based OCR tool for extracting text from images and screenshots.
"""

__version__ = "1.0.0"
__author__ = "Sreeram"
__email__ = "sreeram.lagisetty@gmail.com"

from .ocr_extractor import OCRExtractor
from .gui_extractor import OCRExtractorGUI
from .batch_processor import BatchProcessor

__all__ = [
    "OCRExtractor",
    "OCRExtractorGUI", 
    "BatchProcessor"
]
