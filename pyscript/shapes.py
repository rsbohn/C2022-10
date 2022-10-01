class Rect:
    def __init__(self, x, y, width, height, *, fill=None, outline=None, stroke=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = "black"
        if fill is not None: self.fill = fill
        self.outline = "white"
        if outline is not None: self.outline = outline
        self.stroke = stroke

    def __str__(self):
        return f"A Rect shape at ({self.x},{self.y})"

    def render(self, context):
        context.fillStyle=self.fill
        context.fillRect(self.x, self.y, self.width, self.height)
        context.strokeStyle=self.outline
        context.strokeRect(self.x, self.y, self.width, self.height)