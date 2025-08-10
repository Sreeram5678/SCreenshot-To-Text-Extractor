# Screenshot to Text Extractor

A powerful Python-based OCR (Optical Character Recognition) tool that converts screenshots, images, and scanned documents into editable text. Perfect for extracting text from PDFs, presentations, lecture slides, research papers, and handwritten notes.

## Features

- **Multiple Interface Options**: GUI and command-line interfaces
- **High Accuracy OCR**: Uses Google's Tesseract OCR engine with image enhancement
- **Multi-language Support**: Supports 100+ languages including English, Spanish, French, German, Chinese, Japanese, and more
- **Flexible Input**: Single images, multiple files, or entire directories
- **Smart Image Enhancement**: Automatic contrast, sharpness, and noise reduction for better text recognition
- **Multiple Output Options**: Save to files, copy to clipboard, or display in GUI
- **Batch Processing**: Process hundreds of images with detailed reports
- **Cross-platform**: Works on Windows, macOS, and Linux

## Project Structure

```
Screenshot To Text Extractor/
├── src/                    # Source code
│   ├── __init__.py        # Package initialization
│   ├── ocr_extractor.py   # Core OCR functionality
│   ├── gui_extractor.py   # GUI interface
│   ├── batch_processor.py # Batch processing
│   └── example_usage.py   # Usage examples
├── main.py                 # Main entry point
├── test_installation.py    # Installation test script
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
├── install.sh             # Installation script
├── CLI_COMMANDS.md        # Command-line reference
├── QUICK_REFERENCE.md     # Quick usage guide

├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Requirements

### System Requirements
- Python 3.7 or higher
- Tesseract OCR engine

### Python Dependencies
- pytesseract (Tesseract Python wrapper)
- Pillow (Image processing)
- opencv-python (Advanced image processing)
- pyperclip (Clipboard operations)
- tkinter (GUI - usually included with Python)
- numpy (Numerical operations)

## Installation

### 1. Install Tesseract OCR

#### macOS (using Homebrew)
```bash
brew install tesseract
```

#### Windows
1. Download the installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer and add Tesseract to your PATH

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install tesseract-ocr
```

#### Additional Language Packs (Optional)
For languages other than English, install additional language packs:

**macOS:**
```bash
brew install tesseract-lang
```

**Ubuntu/Debian:**
```bash
sudo apt install tesseract-ocr-[language-code]
# Examples:
sudo apt install tesseract-ocr-spa  # Spanish
sudo apt install tesseract-ocr-fra  # French
sudo apt install tesseract-ocr-deu  # German
```

### 2. Set Up Python Environment

1. **Clone or download this project**
2. **Navigate to the project directory**
   ```bash
   cd "Screenshot To Text Extractor"
   ```

3. **Activate the virtual environment**
   ```bash
   # The virtual environment is already created as 'text_extractor'
   source text_extractor/bin/activate  # macOS/Linux
   # or on Windows:
   text_extractor\Scripts\activate
   ```

4. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### 3. Verify Installation

Test that everything is working:
```bash
python test_installation.py
```

## Usage

### 1. Main Entry Point (Recommended)

Use the main entry point for easy access:
```bash
python main.py --help
python main.py image.png
```

### 2. GUI Interface (Recommended for Beginners)

Launch the user-friendly graphical interface:
```bash
python src/gui_extractor.py
```

**GUI Features:**
- Drag-and-drop or browse for image files
- Select single images, multiple images, or entire directories
- Choose OCR language
- Enable/disable image enhancement
- View extracted text in real-time
- Copy to clipboard or save to file
- Progress tracking for batch operations

### 3. Command Line Interface

#### Basic Usage
```bash
# Extract text from a single image
python src/ocr_extractor.py image.png

# Save to file
python src/ocr_extractor.py image.png -o extracted_text.txt

# Copy to clipboard
python src/ocr_extractor.py image.png --clipboard

# Use different language (Spanish)
python src/ocr_extractor.py image.png -l spa

# Process all images in a directory
python src/ocr_extractor.py /path/to/images/
```

#### Advanced Options
```bash
# Disable image enhancement
python src/ocr_extractor.py image.png --no-enhance

# Custom page segmentation mode
python src/ocr_extractor.py image.png --psm 8

# Custom OCR engine mode
python src/ocr_extractor.py image.png --oem 1
```

### 4. Batch Processing

For processing large numbers of images:
```bash
# Process all images in a directory
python src/batch_processor.py /path/to/images/

# Custom output directory
python src/batch_processor.py /path/to/images/ -o /path/to/output/

# Different language
python src/batch_processor.py /path/to/images/ -l fra

# Don't process subdirectories
python src/batch_processor.py /path/to/images/ --no-recursive

# Only create summary file (no individual files)
python src/batch_processor.py /path/to/images/ --no-individual
```

## Supported File Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- TIFF (.tiff, .tif)
- BMP (.bmp)
- GIF (.gif)
- WebP (.webp)

## Language Codes

Common language codes for the `-l` parameter:
- `eng` - English (default)
- `spa` - Spanish
- `fra` - French
- `deu` - German
- `ita` - Italian
- `por` - Portuguese
- `rus` - Russian
- `chi_sim` - Chinese (Simplified)
- `chi_tra` - Chinese (Traditional)
- `jpn` - Japanese
- `kor` - Korean
- `ara` - Arabic
- `hin` - Hindi

For a complete list, run: `tesseract --list-langs`

## Tips for Better OCR Results

1. **Image Quality**: Use high-resolution images with clear, sharp text
2. **Contrast**: Ensure good contrast between text and background
3. **Orientation**: Keep text horizontal and properly oriented
4. **Lighting**: Use images with even lighting and minimal shadows
5. **File Format**: PNG usually gives better results than JPEG
6. **Enhancement**: Enable image enhancement for low-quality images
7. **Language**: Always specify the correct language for better accuracy

## Troubleshooting

### Common Issues

1. **"Tesseract not found" error**
   - Ensure Tesseract is installed and in your PATH
   - On Windows, you might need to set the tesseract command path

2. **Poor OCR accuracy**
   - Try enabling image enhancement
   - Experiment with different PSM (Page Segmentation Mode) values
   - Ensure the correct language is selected
   - Check image quality and resolution

3. **GUI not starting**
   - Ensure tkinter is installed: `python -m tkinter`
   - Try running with: `python src/gui_extractor.py`

4. **Memory issues with large images**
   - Resize images before processing
   - Process images in smaller batches

### Configuration

For advanced users, you can modify OCR parameters in the scripts:
- **PSM (Page Segmentation Mode)**: Controls how Tesseract segments the page
- **OEM (OCR Engine Mode)**: Controls which OCR engine to use
- **Image preprocessing**: Adjust enhancement parameters for your specific use case

## Examples

### Extract Text from Screenshot
```bash
python main.py screenshot.png --clipboard
```

### Process Research Papers
```bash
python src/batch_processor.py /path/to/pdf_pages/ -l eng -o research_text/
```

### Multi-language Document
```bash
python src/ocr_extractor.py multilang_doc.png -l eng+fra+deu
```

## API Usage

You can also use the OCR extractor in your own Python scripts:

```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ocr_extractor import OCRExtractor

# Initialize extractor
extractor = OCRExtractor(language='eng')

# Extract text from image
text = extractor.extract_text_from_image('image.png')
print(text)

# Process multiple images
images = ['img1.png', 'img2.png', 'img3.png']
combined_text = extractor.extract_text_from_multiple_images(images)

# Save to file
extractor.save_text_to_file(text, 'output.txt')

# Copy to clipboard
extractor.copy_to_clipboard(text)
```

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## Licensing

For licensing information, please contact Sreeram at sreeram.lagisetty@gmail.com

## Author

**Sreeram** - [GitHub](https://github.com/Sreeram5678) - [Instagram](https://www.instagram.com/sreeram_3012?igsh=N2Fub3A5eWF4cjJs&utm_source=qr)

## Acknowledgments

- Google Tesseract OCR Team
- Python Pillow Team
- OpenCV Contributors
- Python Community

---

**Made with ❤️ for researchers, students, and anyone who needs to convert images to text quickly and accurately.**
