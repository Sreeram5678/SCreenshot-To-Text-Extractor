#!/bin/bash

# Screenshot to Text Extractor Installation Script
# This script automates the installation process

echo "=========================================="
echo "Screenshot to Text Extractor Installation"
echo "=========================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check if Tesseract is installed
if ! command -v tesseract &> /dev/null; then
    echo "Warning: Tesseract OCR is not installed."
    echo "Please install Tesseract OCR:"
    echo ""
    echo "macOS: brew install tesseract"
    echo "Ubuntu/Debian: sudo apt install tesseract-ocr"
    echo "Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki"
    echo ""
    read -p "Continue anyway? (y/N): " continue_install
    if [[ ! $continue_install =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✓ Tesseract OCR found: $(tesseract --version | head -n1)"
fi

# Check if virtual environment exists
if [ ! -d "text_extractor" ]; then
    echo "Creating virtual environment 'text_extractor'..."
    python3 -m venv text_extractor
    if [ $? -eq 0 ]; then
        echo "✓ Virtual environment created successfully"
    else
        echo "Error: Failed to create virtual environment"
        exit 1
    fi
else
    echo "✓ Virtual environment 'text_extractor' already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source text_extractor/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "Error: Failed to install dependencies"
    exit 1
fi

# Test installation
echo "Testing installation..."
python ocr_extractor.py --help > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✓ Installation test passed"
else
    echo "Warning: Installation test failed. Some components may not work properly."
fi

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "To get started:"
echo "1. Activate the virtual environment:"
echo "   source text_extractor/bin/activate"
echo ""
echo "2. Launch the GUI:"
echo "   python gui_extractor.py"
echo ""
echo "3. Or use the command line:"
echo "   python ocr_extractor.py your_image.png"
echo ""
echo "4. For batch processing:"
echo "   python batch_processor.py /path/to/images/"
echo ""
echo "For more information, see README.md"
echo ""
