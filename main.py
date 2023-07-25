from PIL import Image

# Open the PNG image
image = Image.open('font.bmp').convert('RGB')

for y in range(0, 8):
    for x in range(0, 32):
        for yy in range(0, 16):
            thisbyte = 0
            for xx in range(0, 8):
                r, g, b = image.getpixel((x * 8 + xx, y * 16 + yy))
                assert (r, g, b) in [(0, 0, 0), (255, 255, 255)]
                if (r, g, b) == (255, 255, 255):
                    thisbyte += 1 << xx
            print(f'"{bin(thisbyte)[2:].zfill(8)}", ', end='')
        print()
