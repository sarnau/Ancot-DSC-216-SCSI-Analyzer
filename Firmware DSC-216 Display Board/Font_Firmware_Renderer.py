#!/usr/bin/env python3

import binascii
from PIL import Image, ImageDraw

ch_fontcount = 4 # number of fonts in the file
ch_count = 256 # number of characters in the font file
ch_width = 8 # width of a single character in the font file in pixel
ch_height = 16 # height of a single character in the font file in pixel
ch_dheight = 16 # destination height (8 = for color screens)
ch_perLine = 16 # number of characters per line

def processFile(filename):
	data = open(filename,'rb').read()[0x4000:]
	for font in range(0,ch_fontcount):
		fontOffset = font * ch_count * ch_height
		img = Image.new('RGB', (ch_width * ch_perLine, int(ch_count * ch_dheight / ch_perLine)), color = 'white')
		draw = ImageDraw.Draw(img)
		for character in range(0,ch_count):
			cd = data[fontOffset+character * ch_height:fontOffset+(character + 1) * ch_height]
			#print('%02x %s' % (character, binascii.hexlify(cd).decode('utf8')))
			chy = int(character / ch_perLine) * ch_dheight
			chx = (character % ch_perLine) * ch_width
			cy = 0
			for ci in range(0, 16):
				for cx in range(0,ch_width):
					if cd[ci] & (1 << (8-cx)):
						color = (0,0,0)
					else:
						color = (255,255,255)
					draw.point([(cx + chx, cy + chy)], color)
				cy = cy + 1
		img.save('DSC_FONT_%d.png' % font)

processFile('DSC-216EL REV1.30A.BIN')
