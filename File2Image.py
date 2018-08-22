#!/usr/bin/env python3
from PIL import Image
from sys import argv
from binascii import hexlify

# Get user input
# File2Image.py <filename> <output> <8K> silent
if len(argv) < 2:
    fname = input("File name: ")
else:
    fname = argv[1]
if len(argv) < 3:
    opname = input("Output file name (Large files may get split up): ")
else:
    opname = argv[2]

mode = "8K" # resolution to create image
# 8K allows for more data but takes longer

MSG = True

if len(argv) > 3: # Command line control for mode
    mode = argv[3]

if len(argv) > 4: # Command line control for silent
    if argv[4] == "silent":
        MSG = False


size = 1 # Image2File only supports 1
counter = 0

def msg(content):
    if(MSG):
        print(content)

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
maxpixels = w * h

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
msg("MODE: "+mode)
with open(fname, 'rb') as f:
    content = hexlify(f.read()).decode("utf-8") # File to hex

#Convert from HEX into HEX colors
msg("Converting into colors...")
lines = [content[i:i+6] for i in range(0, len(content), 6)]
for line in lines:
    l = len(line)
    if l < 6:
        line += ('0'*(6 - l)) # Padding
    if line != "000000":
        c = '#' + line
        msg(c)
        counter += 1
        if(counter == maxpixels):
            counter2 += 1
            msg("Saving image "+counter2)
            main.save(opname+"_"+counter2)
            main = Image.new('RGB', (h, w))
        main = AppendC(c) # Append color into image

msg("Saving final image...")
main.save(opname)
msg("Done :-)")

