# TermGraphics.py

A library to draw graphics in a terminal using Unicode braille art.

Sample usage:

```
#!/usr/bin/env python3
import time
from TermGraphics import TermGraphics

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
import TermGraphics

g = TermGraphics.TermGraphics(mode = TermGraphics.MODE_EASCII)

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
g = TermGraphics.TermGraphics()

g.clear()

g.set_color(TermGraphics.COLOR_RED)

for x in range(g.shape[0]):
    y = int(0.5 * g.shape[1] * ((2*x/g.shape[0]-1)**3 + 1))
    g.point((x,y))

g.set_color(TermGraphics.COLOR_BLUE)

for x in range(g.shape[0]):
    y = int(0.5 * g.shape[1] * (-(2*x/g.shape[0]-1)**3 + 1))
    g.point((x,y))

g.draw()
time.sleep(5)
```

![screenshot](/screenshot2.png?raw=true "screenshot")
