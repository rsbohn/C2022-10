from js import document
from js import setInterval, clearInterval
from pyodide import create_proxy

DISPLAY=document.getElementById("display")
top_group = None
renderer_id = None

@create_proxy
def update():
    if top_group is not None:
        context = DISPLAY.getContext('2d')
        for item in top_group:
            item.render(context)

def show(group, auto_update=False):
    global renderer_id
    global top_group
    top_group = group
    if renderer_id is not None:
        clearInterval(renderer_id)
    if auto_update:
        renderer_id = setInterval(update, 1000)

DISPLAY.show = show
DISPLAY.update = update
def halt():
    clearInterval(renderer_id)