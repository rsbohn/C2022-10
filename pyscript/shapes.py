from js import console
class Rect:
    def __init__(self, x, y, width, height, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = "rgb(200,0,0)"
        self.outline = "white"

    def __str__(self):
        return f"A Rect shape at ({self.x},{self.y})"

    def render(self, context):
        console.log("Render "+str(self))
        context.fillStyle=self.fill
        context.fillRect(self.x, self.y, self.width, self.height)
        context.strokeStyle=self.outline
        context.strokeRect(self.x, self.y, self.width, self.height)