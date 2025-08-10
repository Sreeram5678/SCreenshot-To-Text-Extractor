"""
OCR Text Extractor - Extract text from images and screenshots
Supports multiple image formats and languages
"""

import os
import sys
import argparse
import cv2
import numpy as np
import pytesseract
import pyperclip
from PIL import Image, ImageEnhance, ImageFilter
from typing import Optional, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OCRExtractor:
    """Main OCR text extraction class"""
    
    def __init__(self, language: str = 'eng'):
        """
        Initialize OCR extractor
        
        Args:
            language (str): Tesseract language code (default: 'eng')
        """
        self.language = language
        self.supported_formats = {'.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp'}
        
        # Verify Tesseract installation
        try:
            pytesseract.get_tesseract_version()
            logger.info("Tesseract OCR is properly installed")
        except Exception as e:
            logger.error(f"Tesseract not found: {e}")
            logger.error("Please install Tesseract OCR: https://github.com/tesseract-ocr/tesseract")
            sys.exit(1)
    
    def preprocess_image(self, image_path: str, enhance: bool = True) -> Image.Image:
        """
        Preprocess image for better OCR accuracy
        
        Args:
            image_path (str): Path to the image file
            enhance (bool): Whether to apply image enhancement
            
        Returns:
            PIL.Image: Preprocessed image
        """
        try:
            # Load image
            image = Image.open(image_path)
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            if enhance:
                # Enhance contrast
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(1.5)
                
                # Enhance sharpness
                enhancer = ImageEnhance.Sharpness(image)
                image = enhancer.enhance(2.0)
                
                # Apply slight blur to reduce noise
                image = image.filter(ImageFilter.MedianFilter(size=3))
            
            return image
            
        except Exception as e:
            logger.error(f"Error preprocessing image: {e}")
            raise
    
    def extract_text_from_image(self, image_path: str, enhance: bool = True, 
                              psm: int = 6, oem: int = 3) -> str:
        """
        Extract text from image using Tesseract OCR
        
        Args:
            image_path (str): Path to the image file
            enhance (bool): Whether to enhance image before OCR
            psm (int): Page segmentation mode (default: 6 - uniform block of text)
            oem (int): OCR engine mode (default: 3 - LSTM only)
            
        Returns:
            str: Extracted text
        """
        try:
            # Check if file exists
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image file not found: {image_path}")
            
            # Check file format
            file_ext = os.path.splitext(image_path)[1].lower()
            if file_ext not in self.supported_formats:
                raise ValueError(f"Unsupported file format: {file_ext}")
            
            # Preprocess image
            image = self.preprocess_image(image_path, enhance)
            
            # Configure Tesseract
            custom_config = f'--oem {oem} --psm {psm} -l {self.language}'
            
            # Extract text
            extracted_text = pytesseract.image_to_string(image, config=custom_config)
            
            # Clean up text
            cleaned_text = self.clean_text(extracted_text)
            
            logger.info(f"Successfully extracted text from: {image_path}")
            return cleaned_text
            
        except Exception as e:
            logger.error(f"Error extracting text from {image_path}: {e}")
            raise
    
    def clean_text(self, text: str) -> str:
        """
        Clean extracted text by removing extra whitespace and formatting
        
        Args:
            text (str): Raw extracted text
            
        Returns:
            str: Cleaned text
        """
        # Remove excessive whitespace
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line:  # Only keep non-empty lines
                cleaned_lines.append(cleaned_line)
        
        return '\n'.join(cleaned_lines)
    
    def extract_text_from_multiple_images(self, image_paths: List[str], 
                                        combine: bool = True) -> str:
        """
        Extract text from multiple images
        
        Args:
            image_paths (List[str]): List of image file paths
            combine (bool): Whether to combine all text into one string
            
        Returns:
            str: Combined extracted text or individual results
        """
        all_text = []
        
        for i, image_path in enumerate(image_paths):
            try:
                text = self.extract_text_from_image(image_path)
                if combine:
                    all_text.append(f"--- Image {i+1}: {os.path.basename(image_path)} ---\n{text}\n")
                else:
                    all_text.append(text)
            except Exception as e:
                logger.warning(f"Failed to process {image_path}: {e}")
                continue
        
        return '\n'.join(all_text) if combine else all_text
    
    def save_text_to_file(self, text: str, output_path: str) -> bool:
        """
        Save extracted text to a file
        
        Args:
            text (str): Text to save
            output_path (str): Output file path
            
        Returns:
            bool: Success status
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            logger.info(f"Text saved to: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving text to file: {e}")
            return False
    
    def copy_to_clipboard(self, text: str) -> bool:
        """
        Copy text to clipboard
        
        Args:
            text (str): Text to copy
            
        Returns:
            bool: Success status
        """
        try:
            pyperclip.copy(text)
            logger.info("Text copied to clipboard")
            return True
        except Exception as e:
            logger.error(f"Error copying to clipboard: {e}")
            return False

def main():
    """Command line interface for OCR extraction"""
    parser = argparse.ArgumentParser(description='Extract text from images using OCR')
    parser.add_argument('input_path', help='Path to image file or directory')
    parser.add_argument('-o', '--output', help='Output text file path')
    parser.add_argument('-l', '--language', default='eng', 
                       help='Tesseract language code (default: eng)')
    parser.add_argument('-c', '--clipboard', action='store_true',
                       help='Copy extracted text to clipboard')
    parser.add_argument('--no-enhance', action='store_true',
                       help='Disable image enhancement')
    parser.add_argument('--psm', type=int, default=6,
                       help='Page segmentation mode (default: 6)')
    parser.add_argument('--oem', type=int, default=3,
                       help='OCR engine mode (default: 3)')
    
    args = parser.parse_args()
    
    # Initialize OCR extractor
    extractor = OCRExtractor(language=args.language)
    
    try:
        # Handle single file or directory
        if os.path.isfile(args.input_path):
            # Single file
            text = extractor.extract_text_from_image(
                args.input_path, 
                enhance=not args.no_enhance,
                psm=args.psm,
                oem=args.oem
            )
        elif os.path.isdir(args.input_path):
            # Directory - find all image files
            image_files = []
            for root, dirs, files in os.walk(args.input_path):
                for file in files:
                    if os.path.splitext(file)[1].lower() in extractor.supported_formats:
                        image_files.append(os.path.join(root, file))
            
            if not image_files:
                print("No supported image files found in directory")
                return
            
            text = extractor.extract_text_from_multiple_images(image_files)
        else:
            print(f"Error: {args.input_path} is not a valid file or directory")
            return
        
        # Output results
        if text.strip():
            print("Extracted Text:")
            print("-" * 50)
            print(text)
            print("-" * 50)
            
            # Save to file if specified
            if args.output:
                extractor.save_text_to_file(text, args.output)
            
            # Copy to clipboard if requested
            if args.clipboard:
                extractor.copy_to_clipboard(text)
        else:
            print("No text could be extracted from the image(s)")
    
    except Exception as e:
        logger.error(f"Error during extraction: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
