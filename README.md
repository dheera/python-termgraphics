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

