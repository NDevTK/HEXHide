#!/usr/bin/env python3
import os
from PIL import Image
from sys import argv


MSG = True
output = ""
def msg(content):
    if(MSG):
        print(content)

# Get user input
# Image2File.py <filename> <output> silent
if len(argv) < 2:
    fname = input("File name (Keep split files in same place): ")
else:
    fname = argv[1]
if len(argv) < 3:
    opname = input("Output file name: ")
else:
    opname = argv[2]

if len(argv) > 3: # Command line control for silent
    if argv[3] == "silent":
        MSG = False

def rgb2hex(r,g,b):
    hex = "{:02x}{:02x}{:02x}".format(r,g,b)
    return hex

def ImgProcess(filename):
    output = ""
    im = Image.open(filename, "r") # Open image
    msg("Loading pixels...")
    ListPix = list(im.getdata()) # List all pixels
    msg("Decoding...")
    for p in ListPix:
        out = rgb2hex(p[0],p[1],p[2])  # RGB to HEX
        if out != "000000":
            output += bytes.fromhex(out).decode('utf-8') # Decode HEX
    return output

path = os.path.dirname(fname)
basename = os.path.basename(fname)
if(path == ""):
    path = os.getcwd()
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and basename in i:
        output += ImgProcess(i)


        
msg("Saving final file...") # save to opname
file = open(opname,"w")
file.write(output)
file.close()
msg("Done :-)")
