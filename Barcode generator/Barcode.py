#Importing the libraries
import barcode
from barcode.writer import ImageWriter
from PIL import Image

# Prompt user for the number to generate the barcode
number = input("Enter the code to generate the barcode: ")

# Generate the barcode using the 'upc' format
barcode_format = barcode.get_barcode_class('upc')
my_barcode = barcode_format(number, writer=ImageWriter())

# Save the barcode as a PNG file
my_barcode.save("generated_barcode")

# Open and display the generated barcode image
image = Image.open("generated_barcode.png")
image.show()
