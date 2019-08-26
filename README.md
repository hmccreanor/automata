# automata
Right now this is just a basic automata viewer with buggy zooming in and out.

## Usage
```python
from engine import CanvasViewer

canvas = np.random.randint(2, size = [y, x]) # Some 2 dimensional matrix populated with 1s and 0s

viewer = CanvasViewer(canvas, windowSize, topLeftOfCanvasSlice, canvasSliceDimensions)

exit = False

while not exit:
	viewer.draw()
	exit = viewer.respondToKeys(updateInterval)

```

The `CanvasViewer` class uses the concept of a "canvas" and a "slice", where a canvas is the overall grid matrix the automata exists on and a slice represents the area of that grid you want the `CanvasViewer` object to display.

## To do
* Fix zooming in and out
