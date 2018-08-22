#!/usr/bin/env python3
from PIL import Image
from sys import argv

output = ""

# Get user input
# Image2File.py <filename> <output>
if len(argv) < 2:
    fname = input("File name: ")
else:
    fname = argv[1]
if len(argv) < 3:
    opname = input("Output image name: ")
else:
    opname = argv[2]

im = Image.open(fname, "r") # Open image
print("Loading pixels...")
ListPix = list(im.getdata()) # List all pixels

def rgb2hex(r,g,b):
    hex = "{:02x}{:02x}{:02x}".format(r,g,b)
    return hex
print("Decoding...")
for p in ListPix: # Foreach pixel
    out = rgb2hex(p[0],p[1],p[2]) # RGB to HEX
    if out != "000000":
        output += bytes.fromhex(out).decode('utf-8') # Decode HEX
        
print("Saving file...") # save to opname
file = open(opname,"w")
file.write(output)
file.close()
print("Done :-)")
