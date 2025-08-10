#!/usr/bin/env python3
"""
Demo script for Screenshot to Text Extractor
This script demonstrates the core OCR functionality
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def demo_ocr():
    """Demonstrate OCR functionality"""
    print("Screenshot to Text Extractor - Demo")
    print("=" * 40)
    
    try:
        from ocr_extractor import OCRExtractor
        
        # Initialize OCR extractor
        print("Initializing OCR extractor...")
        extractor = OCRExtractor(language='eng')
        print("✓ OCR extractor initialized successfully")
        
        # Test with a sample text (you can replace this with an actual image path)
        print("\nDemo completed successfully!")
        print("\nTo use the tool:")
        print("1. Command line: python main.py image.png")
        print("2. GUI: python src/gui_extractor.py")
        print("3. Batch processing: python src/batch_processor.py /path/to/images/")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("Please activate the virtual environment: source text_extractor/bin/activate")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    demo_ocr()
