"""
Batch OCR Processor - Command-line tool for processing multiple images
"""

import os
import sys
import argparse
import json
import time
from pathlib import Path
from typing import List, Dict, Any
from ocr_extractor import OCRExtractor
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BatchProcessor:
    """Batch processor for OCR text extraction"""
    
    def __init__(self, language: str = 'eng', output_dir: str = None):
        """
        Initialize batch processor
        
        Args:
            language (str): Tesseract language code
            output_dir (str): Output directory for text files
        """
        self.extractor = OCRExtractor(language=language)
        self.output_dir = output_dir or "extracted_texts"
        self.results = []
        
        # Create output directory if it doesn't exist
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def process_directory(self, input_dir: str, recursive: bool = True, 
                         save_individual: bool = True, create_summary: bool = True) -> Dict[str, Any]:
        """
        Process all images in a directory
        
        Args:
            input_dir (str): Input directory path
            recursive (bool): Process subdirectories recursively
            save_individual (bool): Save text for each image individually
            create_summary (bool): Create a summary file with all results
            
        Returns:
            Dict: Processing results
        """
        logger.info(f"Starting batch processing of directory: {input_dir}")
        
        # Find all image files
        image_files = self.find_image_files(input_dir, recursive)
        
        if not image_files:
            logger.warning("No image files found in directory")
            return {"status": "error", "message": "No image files found"}
        
        logger.info(f"Found {len(image_files)} image files to process")
        
        # Process each image
        results = {
            "total_files": len(image_files),
            "processed": 0,
            "failed": 0,
            "files": [],
            "summary_text": "",
            "processing_time": 0
        }
        
        start_time = time.time()
        
        for i, image_path in enumerate(image_files):
            logger.info(f"Processing {i+1}/{len(image_files)}: {os.path.basename(image_path)}")
            
            try:
                # Extract text
                text = self.extractor.extract_text_from_image(image_path)
                
                file_result = {
                    "file_path": image_path,
                    "file_name": os.path.basename(image_path),
                    "status": "success",
                    "text_length": len(text),
                    "extracted_text": text
                }
                
                # Save individual file if requested
                if save_individual and text.strip():
                    output_file = self.get_output_filename(image_path)
                    self.save_text_file(text, output_file, image_path)
                    file_result["output_file"] = output_file
                
                results["files"].append(file_result)
                results["processed"] += 1
                
                # Add to summary
                if text.strip():
                    results["summary_text"] += f"\n--- {os.path.basename(image_path)} ---\n{text}\n"
                
            except Exception as e:
                logger.error(f"Failed to process {image_path}: {e}")
                file_result = {
                    "file_path": image_path,
                    "file_name": os.path.basename(image_path),
                    "status": "failed",
                    "error": str(e)
                }
                results["files"].append(file_result)
                results["failed"] += 1
        
        # Calculate processing time
        results["processing_time"] = time.time() - start_time
        
        # Create summary file if requested
        if create_summary and results["summary_text"]:
            summary_file = os.path.join(self.output_dir, "batch_summary.txt")
            self.save_text_file(results["summary_text"], summary_file)
            results["summary_file"] = summary_file
        
        # Save processing report
        report_file = os.path.join(self.output_dir, "processing_report.json")
        self.save_processing_report(results, report_file)
        results["report_file"] = report_file
        
        logger.info(f"Batch processing completed: {results['processed']}/{results['total_files']} files processed successfully")
        
        return results
    
    def find_image_files(self, directory: str, recursive: bool = True) -> List[str]:
        """
        Find all image files in directory
        
        Args:
            directory (str): Directory to search
            recursive (bool): Search subdirectories
            
        Returns:
            List[str]: List of image file paths
        """
        image_files = []
        supported_formats = {'.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp'}
        
        if recursive:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if os.path.splitext(file)[1].lower() in supported_formats:
                        image_files.append(os.path.join(root, file))
        else:
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if (os.path.isfile(file_path) and 
                    os.path.splitext(file)[1].lower() in supported_formats):
                    image_files.append(file_path)
        
        return sorted(image_files)
    
    def get_output_filename(self, image_path: str) -> str:
        """
        Generate output filename for extracted text
        
        Args:
            image_path (str): Original image path
            
        Returns:
            str: Output text file path
        """
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        return os.path.join(self.output_dir, f"{base_name}_extracted.txt")
    
    def save_text_file(self, text: str, output_path: str, source_image: str = None):
        """
        Save extracted text to file with metadata
        
        Args:
            text (str): Extracted text
            output_path (str): Output file path
            source_image (str): Source image path (optional)
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                if source_image:
                    f.write(f"Extracted from: {source_image}\n")
                    f.write(f"Extraction time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("-" * 50 + "\n\n")
                f.write(text)
            
            logger.info(f"Text saved to: {output_path}")
            
        except Exception as e:
            logger.error(f"Failed to save text file {output_path}: {e}")
    
    def save_processing_report(self, results: Dict[str, Any], report_path: str):
        """
        Save processing report as JSON
        
        Args:
            results (Dict): Processing results
            report_path (str): Report file path
        """
        try:
            # Create a simplified report for JSON serialization
            report = {
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "total_files": results["total_files"],
                "processed_successfully": results["processed"],
                "failed": results["failed"],
                "processing_time_seconds": round(results["processing_time"], 2),
                "output_directory": self.output_dir,
                "language": self.extractor.language,
                "files": [
                    {
                        "file_name": f["file_name"],
                        "status": f["status"],
                        "text_length": f.get("text_length", 0),
                        "error": f.get("error", None)
                    }
                    for f in results["files"]
                ]
            }
            
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Processing report saved to: {report_path}")
            
        except Exception as e:
            logger.error(f"Failed to save processing report: {e}")

def main():
    """Command line interface for batch processing"""
    parser = argparse.ArgumentParser(description='Batch OCR text extraction from images')
    parser.add_argument('input_dir', help='Input directory containing images')
    parser.add_argument('-o', '--output', default='extracted_texts',
                       help='Output directory for extracted text files (default: extracted_texts)')
    parser.add_argument('-l', '--language', default='eng',
                       help='Tesseract language code (default: eng)')
    parser.add_argument('--no-recursive', action='store_true',
                       help='Do not process subdirectories recursively')
    parser.add_argument('--no-individual', action='store_true',
                       help='Do not save individual text files for each image')
    parser.add_argument('--no-summary', action='store_true',
                       help='Do not create summary file with all extracted text')
    
    args = parser.parse_args()
    
    # Validate input directory
    if not os.path.isdir(args.input_dir):
        print(f"Error: {args.input_dir} is not a valid directory")
        sys.exit(1)
    
    try:
        # Initialize batch processor
        processor = BatchProcessor(language=args.language, output_dir=args.output)
        
        # Process directory
        results = processor.process_directory(
            input_dir=args.input_dir,
            recursive=not args.no_recursive,
            save_individual=not args.no_individual,
            create_summary=not args.no_summary
        )
        
        # Print summary
        print("\nBatch Processing Summary:")
        print("-" * 40)
        print(f"Total files found: {results['total_files']}")
        print(f"Successfully processed: {results['processed']}")
        print(f"Failed: {results['failed']}")
        print(f"Processing time: {results['processing_time']:.2f} seconds")
        print(f"Output directory: {processor.output_dir}")
        
        if results.get('summary_file'):
            print(f"Summary file: {results['summary_file']}")
        
        if results.get('report_file'):
            print(f"Detailed report: {results['report_file']}")
        
        # Show failed files if any
        if results['failed'] > 0:
            print("\nFailed files:")
            for file_info in results['files']:
                if file_info['status'] == 'failed':
                    print(f"  - {file_info['file_name']}: {file_info.get('error', 'Unknown error')}")
    
    except Exception as e:
        logger.error(f"Batch processing failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
