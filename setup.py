"""
Setup script for Screenshot to Text Extractor
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh.readlines() if line.strip() and not line.startswith("#")]

setup(
    name="screenshot-text-extractor",
    version="1.0.0",
    author="Sreeram",
    author_email="sreeram.lagisetty@gmail.com",
    description="A powerful OCR tool for extracting text from screenshots and images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sreeram5678/SCreenshot-To-Text-Extractor",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
        "Topic :: Text Processing",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ocr-extract=ocr_extractor:main",
            "ocr-gui=gui_extractor:main",
            "ocr-batch=batch_processor:main",
        ],
    },
    include_package_data=True,
    keywords="ocr, tesseract, text extraction, image processing, screenshot, pdf",
)
