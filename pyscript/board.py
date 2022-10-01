from js import document, console
from js import setInterval, clearInterval
from pyodide import create_proxy

class CanvasDisplay:
    def __init__(self, canvas):
        self._canvas = canvas
        self._renderer = None
        self.root_group = None
        self.T = 250 # milliseconds
    def refresh(self):
        if self.root_group is not None:
            context = self._canvas.getContext('2d')
            context.clearRect(0,0,self._canvas.width, self._canvas.height)
            self.root_group.render(context)
    def show(self, group, auto_refresh=True):
        self.root_group = group
        if self._renderer is not None:
            clearInterval(self._renderer)
        if auto_refresh:
            console.log("auto_refresh=ON")
            self._renderer = setInterval(create_proxy(lambda: self.refresh()), self.T)
    def halt(self):
        console.log("auto_refresh=OFF")
        clearInterval(self._renderer)
        self._renderer = None
    
    @property
    def width(self):
        return self._canvas.width
    @property
    def height(self):
        return self._canvas.height

DISPLAY=CanvasDisplay(document.getElementById("display"))