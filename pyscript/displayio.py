# SPDX-FileCopyrightText: Copyright (c) 2022 Randall Bohn (dexter)
#
# SPDX-License-Identifier: MIT
from typing import Union, Tuple
from dataclasses import dataclass

# largely based on https://github.com/adafruit/Adafruit_Blinka_Displayio

class Group:
    "A container of renderable items."
    def __init__(self, scale=1):
        self._content = []
    def __iter__(self):
        yield from self._content
    def __str__(self):
        return f"Group([{self._content.__str__}])"
    def append(self, item):
        self._content.append(item)
    def render(self, canvas):
        for item in self:
            item.render(canvas)

class TileGrid:
    """A renderable grid consisting of a bitmap and a pixel shader."""
    def __init__(self, bitmap, *, pixel_shader, width=1, height=1,
        tile_width=None, tile_height=None,
        default_tile=0,
        x=0,y=0):
        self._bitmap = bitmap
        self._pixel_shader = pixel_shader
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._tile_width = tile_width or bitmap.width
        self._tile_height = tile_height or bitmap.height
    def render(self, context):
        cc=["rgb(128,0,128)","rgb(255,255,0)"]
        for x in range(0,self._width, self._tile_width):
            for y in range(0,self._height, self._tile_height):
                context.fillStyle = cc[x%2]
                context.fillRect(x,y,self._tile_width,self._tile_height)


class Palette:
    """A list of color values.
    Size is set when the Palette is created."""
    def __init__(self, color_count:int):
        self._colors = [0 for _ in range(color_count)]
            
    def __setitem__(self, index: int, value):
        self._colors[index] = value
    def __getitem__(self, index:int):
        return self._colors[index]
    def make_transparent(self, index: int):
        pass
    def make_opaque(self, index: int):
        pass

class Bitmap:
    """A renderable bitmap. 
    Each cell has a single value which is usually interpreted using a Palette."""
    def __init__(self, width: int, height: int, value_count: int):
        self._width = width
        self._height = height
        if value_count < 0: raise ValueError("value_count must be a positive int")
        if value_count > 2**32: raise NotImplemented("Invalid bits per value")
        # avoid the 24 bit void
        if value_count > 2**16: self._bits_per_value = 32
        elif value_count > 2**8: self._bits_per_value = 16
        else:
            bits = 1
            while (value_count-1) >> bits:
                bits *= 2
            self._bits_per_value = bits
        self._image = None
        self._dirty_area = RectangleStruct(0,0,width, height)

    def __getitem__(self, index) -> int:
        x,y = self._unflex(index)
        return 0
    def __setitem__(self, index, value) -> None:
        x,y = self._unflex(index)

    @property
    def width(self) -> int:
        return self._width
    @property
    def height(self) -> int:
        return self._height

    def _unflex(self, index: Union[Tuple[int,int],int]):
        if isinstance(index, (tuple,list)):
            x = index[0]
            y = index[1]
        elif isinstance(index, int):
            x = index % self._width
            y = inded // self._height
        return x,y
# %% _structs
@dataclass
class RectangleStruct:
    # pylint: disable=invalid-name
    """Rectangle Struct Dataclass. To eventually be replaced by Area."""
    x1: int
    y1: int
    x2: int
    y2: int
