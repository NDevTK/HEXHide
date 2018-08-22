#!/usr/bin/env python3
from PIL import Image
from sys import argv

# Get user input
# File2Image.py <filename> <output> <8K>
if len(argv) < 2:
    fname = input("File name: ")
else:
    fname = argv[1]
if len(argv) < 3:
    opname = input("Output image name: ")
else:
    opname = argv[2]

mode = "8K" # resolution to create image
# 8K allows for more data but takes longer

if len(argv) > 3: # Command line control for mode
    mode = argv[3]

size = 1 # Image2File only supports 1



if mode == "FHD":
    w = 1920
    h = 1080
if mode == "480P":
    w = 640
    h = 480
if mode == "UHD":
    w = 3840
    h = 2160
if mode == "HD":
    w = 1280
    h = 720
if mode == "4K":
    w = 3840
    h = 2160
if mode == "8K":
    w = 7680
    h = 4320

def AppendC(c):
    newimg = Image.new('RGB', (size, size), c)
    (width1, height1) = main.size
    (width2, height2) = newimg.size
    result_width = width1 + width2
    result_height = max(height1, height2)
    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=main, box=(0, 0))
    result.paste(im=newimg, box=(width1, 0))
    return result

main = Image.new('RGB', (h, w))
print("MODE: "+mode)
with open(fname, 'r') as f:
    content = f.read().encode("utf-8").hex() # File to hex

#Convert from HEX into HEX colors
print("Converting into colors...")
lines = [content[i:i+6] for i in range(0, len(content), 6)]
for line in lines:
    l = len(line)
    if l < 6:
        line += ('0'*(6 - l)) # Padding
    c = '#' + line
    print(c)
    main = AppendC(c) # Append color into image

print("Saving image...")
main.save(opname)
print("Done :-)")
