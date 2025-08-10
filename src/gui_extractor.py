"""
GUI OCR Text Extractor - User-friendly interface for text extraction
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import threading
import os
from ocr_extractor import OCRExtractor
import pyperclip

class OCRExtractorGUI:
    """GUI application for OCR text extraction"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot to Text Extractor")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize OCR extractor
        self.extractor = None
        self.current_text = ""
        
        # Setup GUI
        self.setup_gui()
        
        # Initialize OCR with default language
        self.initialize_ocr()
    
    def setup_gui(self):
        """Setup the GUI layout"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Screenshot to Text Extractor", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # File selection section
        file_frame = ttk.LabelFrame(main_frame, text="Select Image File(s)", padding="10")
        file_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        file_frame.columnconfigure(1, weight=1)
        
        ttk.Button(file_frame, text="Select Single Image", 
                  command=self.select_single_file).grid(row=0, column=0, padx=(0, 10))
        
        ttk.Button(file_frame, text="Select Multiple Images", 
                  command=self.select_multiple_files).grid(row=0, column=1, padx=(0, 10))
        
        ttk.Button(file_frame, text="Select Directory", 
                  command=self.select_directory).grid(row=0, column=2)
        
        # Selected files display
        self.files_var = tk.StringVar(value="No files selected")
        files_label = ttk.Label(file_frame, textvariable=self.files_var, 
                               foreground='blue', wraplength=700)
        files_label.grid(row=1, column=0, columnspan=3, pady=(10, 0), sticky=(tk.W, tk.E))
        
        # Options section
        options_frame = ttk.LabelFrame(main_frame, text="OCR Options", padding="10")
        options_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Language selection
        ttk.Label(options_frame, text="Language:").grid(row=0, column=0, sticky=tk.W)
        self.language_var = tk.StringVar(value="eng")
        language_combo = ttk.Combobox(options_frame, textvariable=self.language_var, 
                                     values=["eng", "spa", "fra", "deu", "ita", "por", "rus", "chi_sim", "jpn"])
        language_combo.grid(row=0, column=1, padx=(10, 20), sticky=tk.W)
        
        # Enhancement option
        self.enhance_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Enhance image quality", 
                       variable=self.enhance_var).grid(row=0, column=2, sticky=tk.W)
        
        # Process button
        process_frame = ttk.Frame(main_frame)
        process_frame.grid(row=3, column=0, columnspan=3, pady=(0, 10))
        
        self.process_button = ttk.Button(process_frame, text="Extract Text", 
                                        command=self.start_extraction, style='Accent.TButton')
        self.process_button.pack(pady=5)
        
        # Progress bar
        self.progress_var = tk.StringVar(value="Ready")
        self.progress_label = ttk.Label(process_frame, textvariable=self.progress_var)
        self.progress_label.pack(pady=(5, 0))
        
        self.progress_bar = ttk.Progressbar(process_frame, mode='indeterminate')
        self.progress_bar.pack(pady=(5, 0), fill=tk.X, padx=50)
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Extracted Text", padding="10")
        results_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Text display
        self.text_display = scrolledtext.ScrolledText(results_frame, wrap=tk.WORD, 
                                                     width=80, height=15)
        self.text_display.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Action buttons
        button_frame = ttk.Frame(results_frame)
        button_frame.grid(row=1, column=0, columnspan=3, pady=(10, 0))
        
        ttk.Button(button_frame, text="Copy to Clipboard", 
                  command=self.copy_to_clipboard).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Save to File", 
                  command=self.save_to_file).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Clear Text", 
                  command=self.clear_text).pack(side=tk.LEFT)
        
        # Status bar
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        status_frame.columnconfigure(0, weight=1)
        
        self.status_var = tk.StringVar(value="Ready - Select images to extract text")
        status_label = ttk.Label(status_frame, textvariable=self.status_var, 
                                foreground='green')
        status_label.grid(row=0, column=0, sticky=tk.W)
    
    def initialize_ocr(self):
        """Initialize OCR extractor with error handling"""
        try:
            self.extractor = OCRExtractor(language=self.language_var.get())
            self.status_var.set("OCR engine initialized successfully")
        except Exception as e:
            messagebox.showerror("OCR Initialization Error", 
                               f"Failed to initialize OCR engine:\n{str(e)}\n\n"
                               "Please ensure Tesseract OCR is properly installed.")
            self.status_var.set("OCR initialization failed")
    
    def select_single_file(self):
        """Select a single image file"""
        file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.tiff *.bmp *.gif *.webp"),
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.selected_files = [file_path]
            self.files_var.set(f"Selected: {os.path.basename(file_path)}")
            self.status_var.set(f"Selected 1 file")
    
    def select_multiple_files(self):
        """Select multiple image files"""
        file_paths = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.tiff *.bmp *.gif *.webp"),
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("All files", "*.*")
            ]
        )
        
        if file_paths:
            self.selected_files = list(file_paths)
            if len(file_paths) == 1:
                self.files_var.set(f"Selected: {os.path.basename(file_paths[0])}")
            else:
                self.files_var.set(f"Selected {len(file_paths)} files: {', '.join([os.path.basename(f) for f in file_paths[:3]])}" + 
                                  ("..." if len(file_paths) > 3 else ""))
            self.status_var.set(f"Selected {len(file_paths)} files")
    
    def select_directory(self):
        """Select a directory containing images"""
        dir_path = filedialog.askdirectory(title="Select Directory with Images")
        
        if dir_path:
            # Find all image files in directory
            image_files = []
            supported_formats = {'.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp'}
            
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    if os.path.splitext(file)[1].lower() in supported_formats:
                        image_files.append(os.path.join(root, file))
            
            if image_files:
                self.selected_files = image_files
                self.files_var.set(f"Selected directory: {os.path.basename(dir_path)} ({len(image_files)} images)")
                self.status_var.set(f"Found {len(image_files)} image files in directory")
            else:
                messagebox.showwarning("No Images Found", 
                                     "No supported image files found in the selected directory.")
                self.status_var.set("No images found in directory")
    
    def start_extraction(self):
        """Start text extraction in a separate thread"""
        if not hasattr(self, 'selected_files') or not self.selected_files:
            messagebox.showwarning("No Files Selected", "Please select image files first.")
            return
        
        if not self.extractor:
            self.initialize_ocr()
            if not self.extractor:
                return
        
        # Update language if changed
        if self.extractor.language != self.language_var.get():
            self.extractor.language = self.language_var.get()
        
        # Disable process button and show progress
        self.process_button.configure(state='disabled')
        self.progress_bar.start()
        self.progress_var.set("Processing images...")
        self.status_var.set("Extracting text...")
        
        # Start extraction in separate thread
        thread = threading.Thread(target=self.extract_text_thread)
        thread.daemon = True
        thread.start()
    
    def extract_text_thread(self):
        """Extract text in a separate thread"""
        try:
            if len(self.selected_files) == 1:
                # Single file
                text = self.extractor.extract_text_from_image(
                    self.selected_files[0], 
                    enhance=self.enhance_var.get()
                )
            else:
                # Multiple files
                text = self.extractor.extract_text_from_multiple_images(
                    self.selected_files, 
                    combine=True
                )
            
            # Update GUI in main thread
            self.root.after(0, self.extraction_complete, text, None)
            
        except Exception as e:
            # Update GUI in main thread with error
            self.root.after(0, self.extraction_complete, None, str(e))
    
    def extraction_complete(self, text, error):
        """Handle extraction completion"""
        # Stop progress bar and re-enable button
        self.progress_bar.stop()
        self.process_button.configure(state='normal')
        
        if error:
            self.progress_var.set("Extraction failed")
            self.status_var.set(f"Error: {error}")
            messagebox.showerror("Extraction Error", f"Failed to extract text:\n{error}")
        elif text and text.strip():
            self.current_text = text
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(1.0, text)
            self.progress_var.set("Extraction completed successfully")
            self.status_var.set(f"Extracted {len(text)} characters from {len(self.selected_files)} file(s)")
        else:
            self.progress_var.set("No text found")
            self.status_var.set("No text could be extracted from the selected images")
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(1.0, "No text could be extracted from the selected images.")
    
    def copy_to_clipboard(self):
        """Copy extracted text to clipboard"""
        text = self.text_display.get(1.0, tk.END).strip()
        if text:
            try:
                pyperclip.copy(text)
                self.status_var.set("Text copied to clipboard")
                messagebox.showinfo("Success", "Text copied to clipboard!")
            except Exception as e:
                messagebox.showerror("Clipboard Error", f"Failed to copy text to clipboard:\n{str(e)}")
        else:
            messagebox.showwarning("No Text", "No text to copy. Please extract text first.")
    
    def save_to_file(self):
        """Save extracted text to a file"""
        text = self.text_display.get(1.0, tk.END).strip()
        if text:
            file_path = filedialog.asksaveasfilename(
                title="Save Extracted Text",
                defaultextension=".txt",
                filetypes=[
                    ("Text files", "*.txt"),
                    ("All files", "*.*")
                ]
            )
            
            if file_path:
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(text)
                    self.status_var.set(f"Text saved to {os.path.basename(file_path)}")
                    messagebox.showinfo("Success", f"Text saved to:\n{file_path}")
                except Exception as e:
                    messagebox.showerror("Save Error", f"Failed to save text:\n{str(e)}")
        else:
            messagebox.showwarning("No Text", "No text to save. Please extract text first.")
    
    def clear_text(self):
        """Clear the text display"""
        self.text_display.delete(1.0, tk.END)
        self.current_text = ""
        self.status_var.set("Text cleared")

def main():
    """Run the GUI application"""
    root = tk.Tk()
    app = OCRExtractorGUI(root)
    
    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
