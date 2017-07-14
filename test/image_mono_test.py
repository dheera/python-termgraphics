#!/usr/bin/env python3

import termgraphics
from PIL import Image, ImageOps
import requests
from io import BytesIO
import time

g = termgraphics.TermGraphics()

def get_image(url = 'https://imgs.xkcd.com/comics/estimation.png'):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

if __name__ == "__main__":
    img = get_image()
    img = ImageOps.invert(img).resize((200,280), Image.NEAREST)
    g.image(list(img.getdata()), img.width, img.height, (0, 0), image_type = termgraphics.IMAGE_UINT8)

g.draw()
time.sleep(2)
