from PIL import Image, ImagePalette
import os
import sys

image = sys.argv[1]
pal = sys.argv[2]
dither_arg = sys.argv[3]

if dither_arg == 'true':
    dither_arg = True
if dither_arg == 'false':
    dither_arg = False

pal_image = Image.open(str(pal))
pal_image = pal_image.convert("RGB")

# get all the colors into a list
pal_col = pal_image.getcolors()
palette_array = []
i = 0

for color in pal_col:
   palette_array = palette_array + (list(pal_col[i][1]))
   i += 1

# fill extra spots because for some reason PIL automatically fills it weird random colors
# that aren't in the palette when it is too small

print(len(palette_array))
while len(palette_array) != 768:
   palette_array = palette_array + (list(pal_col[0][1])) 

# make an image and add the palette to it
pal_image2 = Image.new("P", (1,1))
pal_image2.putpalette(palette_array,"RGB")

def main(img_name):
    print(img_name)
    print('this is the img name!')
    with Image.open(str(img_name)) as img:
        # if rgba convert to rgb
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        out = img.quantize(palette=pal_image2,dither=dither_arg)
        out = out.convert('RGB')
        if img_name.find('/'):
            img_name = img_name[img_name.find('/') + 1:]
            print(img_name[-img_name.find('.') - 1:])
            img_name = img_name.replace(img_name[-img_name.find('.') - 1:], "")
            print(img_name)
        
        out.save("converted_" + img_name + '.png', 'PNG')


main(image)


