import py5

def setup():
    py5.size(500,500)
    
def draw():
    py5.fill(0.255,0)
    py5.rect(py5.mouse_x, py5.mouse_y,py5.width/2,py5.height/2)
