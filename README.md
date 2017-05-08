# termgraphics.py

A library to draw graphics in a terminal using Unicode braille art.

Sample usage:

```
#!/usr/bin/env python3
import time
from termgraphics import termgraphics

g = TermGraphics()

g.clear()

for x in range(g.shape[0]):
    y = int(0.5 * g.shape[1] * ((2*x/g.shape[0]-1)**3 + 1))
    g.point((x,y))

g.draw()
time.sleep(5)
```

![screenshot](/screenshot0.png?raw=true "screenshot")

It also supports using ASCII art, in case you are inside a screen or something else that doesn't
support Unicode terminals.

```
#!/usr/bin/env python3
import time
import termgraphics

g = termgraphics.TermGraphics(mode = termgraphics.MODE_EASCII)

g.clear()

for x in range(g.shape[0]):
    y = int(0.5 * g.shape[1] * ((2*x/g.shape[0]-1)**3 + 1))
    g.point((x,y))

g.draw()
time.sleep(5)
```

![screenshot](/screenshot1.png?raw=true "screenshot")

It also supports changing colors as per ANSI terminal specifications. However, since it is only possible to set the color of a full character, if 2 points of different colors occur in the same character block, the latter color will be used.

```
#!/usr/bin/env python3
import math
import time
import termgraphics

g = termgraphics.TermGraphics()

g.clear()

# draw axes

g.set_color(termgraphics.COLOR_WHITE)

g.line((0, g.shape[1]/2), (g.shape[0], g.shape[1]/2))
g.line((g.shape[0]/2, 0), (g.shape[0]/2, g.shape[1]))

# draw a sin in red

g.set_color(termgraphics.COLOR_RED)

points = []
for x in range(g.shape[0]):
    y = g.shape[1]/2*(1+math.sin(2*math.pi*x/g.shape[0]))
    points.append((int(x), int(y)))

g.poly(points)

# draw a cos in blue

g.set_color(termgraphics.COLOR_BLUE)

points = []
for x in range(g.shape[0]):
    y = g.shape[1]/2*(1+math.cos(2*math.pi*x/g.shape[0]))
    points.append((int(x), int(y)))

g.poly(points)

g.draw()
time.sleep(5)
```

![screenshot](/screenshot2.png?raw=true "screenshot")

You can also display images (preliminary support):
```
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
```

![screenshot](/screenshot3.png?raw=true "screenshot")

# Planned features

* Reduce bandwidth by only drawing parts of the screen that have changed
* Draw text at (x,y)
* Draw color images at (x,y)
* Both inline and full-screen support
* Multiple canvases per screen
* 256-color terminal support
* Separate ASCII and Extended ASCII modes
