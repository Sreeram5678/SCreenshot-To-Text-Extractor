#!/usr/bin/env python3
"""
Main entry point for Screenshot to Text Extractor
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ocr_extractor import main

if __name__ == "__main__":
    main()
