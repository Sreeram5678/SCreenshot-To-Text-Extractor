#!/usr/bin/env python3
"""
Test script to verify Screenshot to Text Extractor installation
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        # Add src to path
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
        
        # Test core imports
        from ocr_extractor import OCRExtractor
        print("✓ OCRExtractor imported successfully")
        
        from gui_extractor import OCRExtractorGUI
        print("✓ OCRExtractorGUI imported successfully")
        
        from batch_processor import BatchProcessor
        print("✓ BatchProcessor imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_tesseract():
    """Test if Tesseract is available"""
    print("\nTesting Tesseract installation...")
    
    try:
        import pytesseract
        version = pytesseract.get_tesseract_version()
        print(f"✓ Tesseract version {version} found")
        return True
    except Exception as e:
        print(f"✗ Tesseract not available: {e}")
        print("Please install Tesseract OCR engine")
        return False

def test_dependencies():
    """Test if all Python dependencies are available"""
    print("\nTesting Python dependencies...")
    
    dependencies = [
        'cv2',
        'numpy', 
        'PIL',
        'pyperclip'
    ]
    
    all_good = True
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✓ {dep} imported successfully")
        except ImportError:
            print(f"✗ {dep} not available")
            all_good = False
    
    return all_good

def main():
    """Run all tests"""
    print("Screenshot to Text Extractor - Installation Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_tesseract,
        test_dependencies
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    if all(results):
        print("🎉 All tests passed! Installation is successful.")
        print("\nYou can now use the tool with:")
        print("  python main.py --help")
        print("  python src/gui_extractor.py")
        print("  python src/batch_processor.py --help")
    else:
        print("❌ Some tests failed. Please check the installation.")
        print("\nCommon solutions:")
        print("1. Install Tesseract OCR engine")
        print("2. Activate virtual environment: source text_extractor/bin/activate")
        print("3. Install dependencies: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
