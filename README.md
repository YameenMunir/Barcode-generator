# Barcode Generator
This project generates a barcode image from a user-provided code using Python. The code utilizes the python-barcode library for generating the barcode and Pillow for handling image files.

## Features
Generates a barcode in UPC (Universal Product Code) format.
Saves the barcode as a .png image file.
Opens and displays the generated barcode image using the Pillow library.

## Prerequisites
Before running the project, make sure to install the required libraries:
python-barcode: Used to generate barcodes in various formats.
Pillow: A popular Python library for opening, manipulating, and saving image files.

### Install the dependencies:
Copy code
pip install -r requirements.txt

## Usage
Clone or download the project.
Run the script barcode_generator.py.
Input a valid number (UPC standard requires a 12-digit number) when prompted.
The barcode will be saved as a PNG file (generated_barcode.png) and displayed.

## Running the Script:
Copy code
python barcode_generator.py
### Example:
Copy code
Enter the code to generate the barcode: 123456789012.

This will generate a file named generated_barcode.png in the project directory, and the image will also open automatically.

## File Information
barcode_generator.py: The main script that prompts the user for input, generates the barcode, saves it as an image, and opens the image.

## Troubleshooting
Ensure that the input code is a valid 12-digit number for the UPC format.
If you encounter issues with displaying the image, verify that Pillow is installed correctly and supports the png format.

