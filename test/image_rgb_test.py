#!/usr/bin/env python3

import termgraphics
from PIL import Image, ImageOps
import requests
from io import BytesIO
import time

g = termgraphics.TermGraphics()

def get_image(url = 'https://devblogs.nvidia.com/parallelforall/wp-content/uploads/2016/07/cute.jpg'):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

if __name__ == "__main__":
    img = get_image().resize((200//2,150//4), Image.NEAREST)
    time.sleep(2)
    g.image(list(img.getdata()), img.width, img.height, (0, 0), image_type = termgraphics.IMAGE_RGB_2X4)

g.draw()
time.sleep(2)
