"""
Example usage of the OCR Text Extractor
Demonstrates various ways to use the OCR functionality programmatically
"""

import os
from ocr_extractor import OCRExtractor

def example_basic_usage():
    """Basic OCR text extraction example"""
    print("=== Basic OCR Usage Example ===")
    
    # Initialize the OCR extractor
    extractor = OCRExtractor(language='eng')
    
    # Example with a hypothetical image file
    image_path = "sample_image.png"
    
    # Note: This is just an example - you'll need an actual image file
    if os.path.exists(image_path):
        try:
            # Extract text from image
            text = extractor.extract_text_from_image(image_path)
            
            print(f"Extracted text from {image_path}:")
            print("-" * 40)
            print(text)
            print("-" * 40)
            
            # Save to file
            output_file = "extracted_text.txt"
            if extractor.save_text_to_file(text, output_file):
                print(f"Text saved to {output_file}")
            
            # Copy to clipboard
            if extractor.copy_to_clipboard(text):
                print("Text copied to clipboard")
                
        except Exception as e:
            print(f"Error processing image: {e}")
    else:
        print(f"Sample image {image_path} not found. Please provide a real image file.")

def example_multiple_images():
    """Example of processing multiple images"""
    print("\n=== Multiple Images Example ===")
    
    extractor = OCRExtractor(language='eng')
    
    # List of image files (replace with actual image paths)
    image_files = [
        "image1.png",
        "image2.jpg", 
        "image3.tiff"
    ]
    
    # Filter to only existing files
    existing_files = [f for f in image_files if os.path.exists(f)]
    
    if existing_files:
        try:
            # Extract text from multiple images
            combined_text = extractor.extract_text_from_multiple_images(existing_files)
            
            print("Combined text from multiple images:")
            print("-" * 50)
            print(combined_text)
            print("-" * 50)
            
        except Exception as e:
            print(f"Error processing multiple images: {e}")
    else:
        print("No sample images found. Please add some image files to test this example.")

def example_different_languages():
    """Example of OCR with different languages"""
    print("\n=== Multi-language OCR Example ===")
    
    # English OCR
    en_extractor = OCRExtractor(language='eng')
    
    # Spanish OCR
    es_extractor = OCRExtractor(language='spa')
    
    # French OCR
    fr_extractor = OCRExtractor(language='fra')
    
    sample_image = "multilang_sample.png"
    
    if os.path.exists(sample_image):
        try:
            print("Extracting text with different language models:")
            
            # English
            en_text = en_extractor.extract_text_from_image(sample_image)
            print(f"English OCR result:\n{en_text[:100]}...\n")
            
            # Spanish  
            es_text = es_extractor.extract_text_from_image(sample_image)
            print(f"Spanish OCR result:\n{es_text[:100]}...\n")
            
            # French
            fr_text = fr_extractor.extract_text_from_image(sample_image)
            print(f"French OCR result:\n{fr_text[:100]}...\n")
            
        except Exception as e:
            print(f"Error with multi-language OCR: {e}")
    else:
        print("Sample multilingual image not found.")

def example_image_enhancement():
    """Example showing the effect of image enhancement"""
    print("\n=== Image Enhancement Example ===")
    
    extractor = OCRExtractor(language='eng')
    
    sample_image = "low_quality_image.png"
    
    if os.path.exists(sample_image):
        try:
            # Without enhancement
            text_no_enhance = extractor.extract_text_from_image(sample_image, enhance=False)
            
            # With enhancement
            text_enhanced = extractor.extract_text_from_image(sample_image, enhance=True)
            
            print("OCR without enhancement:")
            print(f"Length: {len(text_no_enhance)} characters")
            print(f"Preview: {text_no_enhance[:100]}...\n")
            
            print("OCR with enhancement:")
            print(f"Length: {len(text_enhanced)} characters") 
            print(f"Preview: {text_enhanced[:100]}...\n")
            
            if len(text_enhanced) > len(text_no_enhance):
                print("✓ Enhancement improved text extraction!")
            
        except Exception as e:
            print(f"Error testing image enhancement: {e}")
    else:
        print("Sample low-quality image not found.")

def example_custom_preprocessing():
    """Example of custom OCR settings"""
    print("\n=== Custom OCR Settings Example ===")
    
    extractor = OCRExtractor(language='eng')
    
    sample_image = "document_page.png"
    
    if os.path.exists(sample_image):
        try:
            # Try different page segmentation modes
            psm_modes = [6, 8, 11, 13]  # Different segmentation strategies
            
            for psm in psm_modes:
                text = extractor.extract_text_from_image(sample_image, psm=psm)
                print(f"PSM {psm} result length: {len(text)} characters")
                print(f"Preview: {text[:50]}...\n")
                
        except Exception as e:
            print(f"Error testing custom settings: {e}")
    else:
        print("Sample document image not found.")

def create_sample_images_info():
    """Information about creating sample images for testing"""
    print("\n=== Sample Images for Testing ===")
    print("To test these examples, create or add the following image files:")
    print("1. sample_image.png - Any image with text")
    print("2. image1.png, image2.jpg, image3.tiff - Multiple test images")
    print("3. multilang_sample.png - Image with text in multiple languages")
    print("4. low_quality_image.png - Poor quality or low resolution image")
    print("5. document_page.png - Scanned document or book page")
    print("\nYou can:")
    print("- Take screenshots of text from your screen")
    print("- Use photos of documents, books, or signs")
    print("- Download sample images from the internet")
    print("- Scan documents or handwritten notes")

def main():
    """Run all examples"""
    print("OCR Text Extractor - Usage Examples")
    print("=" * 50)
    
    # Run examples
    example_basic_usage()
    example_multiple_images()
    example_different_languages()
    example_image_enhancement()
    example_custom_preprocessing()
    
    # Show sample images info
    create_sample_images_info()
    
    print("\n" + "=" * 50)
    print("Examples completed!")
    print("For more advanced usage, see the README.md file.")

if __name__ == "__main__":
    main()
