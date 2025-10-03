import py5

mode = 0

def key_pressed():
    global mode
    if py5.key >= '0' and py5.key <= '9':
        mode = int(py5.key) - int('0')
        print(mode)

def setup():
    py5.size(600, 600)  

def draw():
    global mode
    print(mode)
    if mode == 0:
        py5.background(255)
        py5.stroke(0,255,0)
        py5.fill(0,255,0)
        py5.circle(py5.mouse_x, py5.mouse_y, 60)
        
        py5.fill(255,255,0)
        py5.circle(py5.mouse_x-10, py5.mouse_y-10, 10)
        py5.circle(py5.mouse_x+10, py5.mouse_y-10, 10)
        
        py5.fill(255,255,0)
        py5.stroke(255, 255, 0)
        py5.stroke_weight(1)
        py5.arc(py5.mouse_x, py5.mouse_y + 5, 40, 20, 0, py5.PI, py5.CHORD)
    elif mode ==1:
        py5.background(255)
        py5.stroke(0,255,0)
        py5.fill(0,255,0)
        py5.circle(py5.mouse_x, py5.mouse_y, 60)
        
    
    

    
py5.run_sketch()  