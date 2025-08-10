# 📋 CLI Commands Reference

Complete command reference for the Screenshot to Text Extractor CLI tools.

## 🔧 Initial Setup

### Activate Virtual Environment
```bash
# Always run this first before using any commands
source text_extractor/bin/activate
```

### Verify Installation
```bash
# Check if Tesseract OCR is installed
tesseract --version

# Check available languages
tesseract --list-langs

# Test CLI tools
python ocr_extractor.py --help
python batch_processor.py --help
```

---

## 🖼️ Single Image Processing

### Basic Text Extraction
```bash
# Extract text from a single image and display in terminal
python ocr_extractor.py image.png

# Extract text from different image formats
python ocr_extractor.py document.jpg
python ocr_extractor.py screenshot.tiff
python ocr_extractor.py scan.bmp
```

### Save to File
```bash
# Extract text and save to a text file
python ocr_extractor.py document.png -o extracted_text.txt

# Save with custom filename
python ocr_extractor.py receipt.jpg -o receipt_text.txt
```

### Copy to Clipboard
```bash
# Extract text and copy directly to clipboard
python ocr_extractor.py screenshot.png --clipboard

# Combine save and clipboard
python ocr_extractor.py image.png -o output.txt --clipboard
```

### Multi-language Processing
```bash
# Spanish text extraction
python ocr_extractor.py spanish_doc.png -l spa

# French text extraction
python ocr_extractor.py french_text.jpg -l fra

# German text extraction
python ocr_extractor.py german_document.png -l deu

# Chinese (Simplified) text extraction
python ocr_extractor.py chinese_text.png -l chi_sim

# Japanese text extraction
python ocr_extractor.py japanese_doc.png -l jpn
```

### Image Enhancement Options
```bash
# Default: with image enhancement (recommended for low-quality images)
python ocr_extractor.py blurry_image.png

# Disable enhancement (for high-quality images)
python ocr_extractor.py clear_image.png --no-enhance
```

### Advanced OCR Settings
```bash
# Different page segmentation modes
python ocr_extractor.py single_word.png --psm 8      # Single word
python ocr_extractor.py single_line.png --psm 7      # Single text line
python ocr_extractor.py text_block.png --psm 6       # Uniform block (default)
python ocr_extractor.py full_page.png --psm 3        # Fully automatic page segmentation

# Different OCR engine modes
python ocr_extractor.py document.png --oem 1         # Neural nets LSTM only
python ocr_extractor.py document.png --oem 2         # Legacy + LSTM engines
python ocr_extractor.py document.png --oem 3         # Default (LSTM only)
```

---

## 📁 Directory Processing

### Process All Images in Directory
```bash
# Process all images in current directory
python ocr_extractor.py ./images/

# Process images in specific directory
python ocr_extractor.py /path/to/images/

# Process and save combined output
python ocr_extractor.py ./photos/ -o all_text.txt
```

### Recursive Directory Processing
```bash
# Process images in directory and all subdirectories
python ocr_extractor.py /path/to/main_folder/
```

---

## 🔄 Batch Processing

### Basic Batch Operations
```bash
# Process all images in directory with individual output files
python batch_processor.py /path/to/images/

# Process with custom output directory
python batch_processor.py /path/to/images/ -o extracted_texts/

# Process with specific language
python batch_processor.py /path/to/spanish_docs/ -l spa -o spanish_output/
```

### Batch Processing Options
```bash
# Only create summary file (no individual files)
python batch_processor.py /path/to/images/ --no-individual

# Don't create summary file (only individual files)
python batch_processor.py /path/to/images/ --no-summary

# Process only current directory (not subdirectories)
python batch_processor.py /path/to/images/ --no-recursive

# Combine options
python batch_processor.py /path/to/images/ --no-recursive --no-summary -o results/
```

### Large Scale Processing
```bash
# Process hundreds of images with detailed reporting
python batch_processor.py /path/to/large_collection/ -o batch_results/

# Multi-language batch processing
python batch_processor.py /path/to/multilang_docs/ -l fra -o french_results/
```

---

## 🌍 Language Codes Reference

### Common Languages
```bash
eng     # English (default)
spa     # Spanish
fra     # French
deu     # German
ita     # Italian
por     # Portuguese
rus     # Russian
chi_sim # Chinese (Simplified)
chi_tra # Chinese (Traditional)
jpn     # Japanese
kor     # Korean
ara     # Arabic
hin     # Hindi
```

### Usage Examples by Language
```bash
# English (default)
python ocr_extractor.py document.png

# Spanish documents
python ocr_extractor.py documento.png -l spa

# French documents
python ocr_extractor.py document.png -l fra

# Multi-language document (English + Spanish)
python ocr_extractor.py mixed_doc.png -l eng+spa
```

---

## 📄 File Format Support

### Supported Input Formats
```bash
# Image formats supported
python ocr_extractor.py document.png    # PNG (recommended)
python ocr_extractor.py photo.jpg       # JPEG
python ocr_extractor.py scan.tiff       # TIFF (high quality)
python ocr_extractor.py image.bmp       # BMP
python ocr_extractor.py animation.gif   # GIF
python ocr_extractor.py modern.webp     # WebP
```

---

## 🛠️ Troubleshooting Commands

### Diagnostic Commands
```bash
# Check Python environment
python --version

# Verify virtual environment is active
which python

# Test Tesseract installation
tesseract --version

# Check available languages
tesseract --list-langs

# Test with verbose output
python ocr_extractor.py test_image.png --help
```

### Common Error Solutions
```bash
# If "tesseract not found" error:
brew install tesseract

# If virtual environment not active:
source text_extractor/bin/activate

# If language not available:
tesseract --list-langs
brew install tesseract-lang  # Install additional languages
```

---

## 💡 Practical Use Cases

### Academic/Research
```bash
# Extract text from research paper screenshots
python ocr_extractor.py research_paper.png -l eng -o paper_notes.txt

# Process multiple lecture slides
python batch_processor.py ./lecture_slides/ -o lecture_notes/

# Extract equations and text from academic papers
python ocr_extractor.py equation_image.png --psm 6 --clipboard
```

### Business/Office
```bash
# Process receipts and invoices
python batch_processor.py ./receipts/ -o expense_reports/

# Extract text from presentations
python ocr_extractor.py presentation_slide.png --clipboard

# Multi-language business documents
python ocr_extractor.py contract.png -l eng+spa -o contract_text.txt
```

### Personal Use
```bash
# Extract text from photos of documents
python ocr_extractor.py phone_photo.jpg --enhance --clipboard

# Process screenshots from social media
python ocr_extractor.py screenshot.png --clipboard

# Extract text from book pages
python ocr_extractor.py book_page.jpg --psm 3 -o book_excerpt.txt
```

### Automation Scripts
```bash
# Create a shell script for daily processing
#!/bin/bash
source text_extractor/bin/activate
python batch_processor.py ~/Desktop/daily_scans/ -o ~/Documents/extracted_text/

# Process with timestamp
python batch_processor.py ./input/ -o "./output_$(date +%Y%m%d)/"
```

---

## 🔧 Performance Optimization

### For High-Quality Images
```bash
# Disable enhancement for clear, high-resolution images
python ocr_extractor.py high_res_scan.png --no-enhance

# Use specific PSM for document types
python ocr_extractor.py clean_document.png --psm 3 --no-enhance
```

### For Low-Quality Images
```bash
# Enable enhancement (default) for poor quality images
python ocr_extractor.py blurry_photo.jpg

# Try different PSM modes for better results
python ocr_extractor.py difficult_image.png --psm 11
```

### For Large Batches
```bash
# Process large directories efficiently
python batch_processor.py /large_collection/ --no-individual -o summary_only/

# Parallel processing (if needed)
find ./images -name "*.png" -exec python ocr_extractor.py {} -o {}.txt \;
```

---

## 📊 Output Examples

### Terminal Output Format
```bash
# Standard output shows extracted text
python ocr_extractor.py sample.png
# Output:
# Extracted Text:
# --------------------------------------------------
# This is the extracted text from your image.
# Multiple lines are preserved.
# --------------------------------------------------
```

### File Output Format
```bash
# Text files include metadata
python ocr_extractor.py sample.png -o output.txt
# Creates: output.txt with content:
# This is the extracted text from your image.
# Multiple lines are preserved.
```

### Batch Processing Output
```bash
# Creates multiple files and reports
python batch_processor.py ./images/
# Creates:
# - extracted_texts/image1_extracted.txt
# - extracted_texts/image2_extracted.txt
# - extracted_texts/batch_summary.txt
# - extracted_texts/processing_report.json
```

---

## 🚀 Quick Start Commands

### Test Setup
```bash
# 1. Activate environment
source text_extractor/bin/activate

# 2. Test with any image
python ocr_extractor.py /path/to/test_image.png --clipboard

# 3. Verify text was copied to clipboard
# Paste (Cmd+V) in any text editor
```

### Daily Workflow
```bash
# Morning routine: process overnight scans
source text_extractor/bin/activate
python batch_processor.py ~/Desktop/scans/ -o ~/Documents/daily_extracts/

# Quick screenshot processing
python ocr_extractor.py ~/Desktop/screenshot.png --clipboard
```

---

## 📝 Notes

- Always activate the virtual environment before running commands
- PNG format generally gives the best OCR results
- Use `--clipboard` for quick copy-paste workflows
- Batch processing creates detailed JSON reports for tracking
- Image enhancement is enabled by default and usually improves results
- For programming code in images, try `--psm 6` or `--psm 8`
- Multi-language documents can use combined language codes like `eng+spa`

---

*For more detailed information, see README.md in the project directory.*
