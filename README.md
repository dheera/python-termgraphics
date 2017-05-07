# TermGraphics.py

A library to draw graphics in a terminal using Unicode braille art.

Sample usage:

```
from TermGraphics import TermGraphics

g = TermGraphics()

g.clear()
for i in range(100):
    g.point((i,i))

g.draw()
```

