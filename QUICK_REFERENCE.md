# 🚀 Quick Reference Card

Essential commands for everyday use of the Screenshot to Text Extractor.

## ⚡ Setup (Run Once)
```bash
# Activate virtual environment (do this every time you start)
source text_extractor/bin/activate
```

## 🎯 Most Common Commands

### Single Image → Clipboard
```bash
python ocr_extractor.py image.png --clipboard
```

### Single Image → File
```bash
python ocr_extractor.py document.jpg -o extracted.txt
```

### Process Folder
```bash
python batch_processor.py /path/to/images/
```

### Different Language
```bash
python ocr_extractor.py spanish_doc.png -l spa --clipboard
```

## 🔥 One-Liners for Common Tasks

| Task | Command |
|------|---------|
| **Screenshot to clipboard** | `python ocr_extractor.py screenshot.png -c` |
| **Document to file** | `python ocr_extractor.py doc.jpg -o text.txt` |
| **Spanish text** | `python ocr_extractor.py doc.png -l spa -c` |
| **Folder processing** | `python batch_processor.py ./images/` |
| **High quality scan** | `python ocr_extractor.py scan.png --no-enhance -c` |
| **Poor quality photo** | `python ocr_extractor.py blurry.jpg -c` |

## 📱 Languages Quick Codes
- `eng` - English
- `spa` - Spanish  
- `fra` - French
- `deu` - German
- `chi_sim` - Chinese
- `jpn` - Japanese

## 🛠️ File Formats
✅ PNG, JPG, TIFF, BMP, GIF, WebP

## 💡 Pro Tips
- Always use `--clipboard` (`-c`) for quick copy-paste
- PNG images give best results
- Add `-l spa` for Spanish, `-l fra` for French, etc.
- Use `batch_processor.py` for multiple images
- Image enhancement is automatic (disable with `--no-enhance`)

## 🚨 Troubleshooting
```bash
# If command not found:
source text_extractor/bin/activate

# If tesseract error:
brew install tesseract

# Check everything works:
python ocr_extractor.py --help
```

---
*For complete commands, see CLI_COMMANDS.md*
