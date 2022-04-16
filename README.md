# image-palette-forcer

forces an image into a specific color palette

requires pillow and python

probably breaks all python style guides (sorry)

## example conversion

![bird](https://user-images.githubusercontent.com/39038795/163659369-5ffe7458-5086-49c1-a698-a1098c0ca8de.jpeg)

![converted_bird](https://user-images.githubusercontent.com/39038795/163659380-af532d73-df84-40cc-b553-9777bd527cdd.png)

## usage

```bash
python convert_to_palette.py [image] [palette] [dithering]
```
set dithering to true or false to enable or disable it (true uses floyd steinberg)


example
```bash
python convert_to_palette.py demo/bird.jpeg demo/crimson-1x.png true
```

## license
do whatever i dont care

## credits

bird image from here:
https://www.goodfreephotos.com/animals/birds/blue-bird.jpg.php

demo color palette (crimson-1x.png) from WildLeoKnight
https://lospec.com/palette-list/crimson

