import pandas as pd
import py5

#function to to take in data from csv file
def loaddata(df):
    datafile = pd.read_csv(df,encoding="latin-1")
    return datafile


def setup():
    global df 
    df = loaddata("HabHYG15ly.csv")
    
setup()

dist = df['Distance'][1]
display_name = df['Display Name'][1]

col = df['HabHyg']

print("the number of stars in the data set is:",len(col))
print(dist)
print(display_name)

#for loop for the info of the first 5 stars   
for i in range(5):
    display_name = df['Display Name'][i]
    dist = df['Distance'][i]
    coordinates_x = df['Xg'][i]
    coordinates_y = df['Yg'][i]
    coordinates_z = df['Zg'][i]
    print("This is the info for star number:",i+1)
    print(display_name)
    print(dist)
    print(coordinates_x, ",", coordinates_y,",", coordinates_z)

#range loop to check what stars are habitable
hab_count = 0  
for i in range(len(col)):
    if df["Hab?"][i] == 1:
        print(df["Display Name"][i],"is habitibal")
        hab_count += 1
print("There are",hab_count,"habitable stars")

def key_pressed():
    global mode
    mode = 1
    if py5.mouse_is_pressed:
        border = 50
        for i in range(len(col)):
            py5.fill(255,0,0)
            x = df['Xg'][i]
            y = df['Yg'][i]
            
            x_screen = py5.remap(x,-5,5,border, py5.width - border)
            y_screen = py5.remap(y,-5,5,border,py5.height - border)
            
            if py5.mouse_x == x_screen and py5.mouse_y == y_screen:
                py5.fill(255)
                py5.line = (x_screen,y_screen,py5.mouse_x,py5.mouse_y)
                if py5.mouse_is_pressed:
                    border = 50
                    for i in range(len(col)):
                        py5.fill(255,0,0)
                        x = df['Xg'][i]
                        y = df['Yg'][i]
                        
                        x_screen_2 = py5.remap(x,-5,5,border, py5.width - border)
                        y_screen_2 = py5.remap(y,-5,5,border,py5.height - border)
                        
                        if py5.mouse_x == x_screen_2 and py5.mouse_y == y_screen_2:
                            py5.fill(255)
                            py5.line = (x_screen,y_screen,x_screen_2,x_screen_2)
                        
                        
                            
                
            
            
 
def draw_grid():
    py5.stroke(128, 0, 128)
    border = 50
    for i in range(-5, 6):
        x = py5.remap(i, -5, 5, border, py5.width - border)
        py5.line(x, border, x, py5.height - border)
    for i in range(-5, 6):
        y = py5.remap(i, -5, 5, border, py5.height - border)
        py5.line(border, y, py5.width - border, y)

#function to plot the stars and their names
def stars():
    border = 50
    for i in range(len(col)):
        py5.fill(255,255,0)
        x = df['Xg'][i]
        y = df['Yg'][i]
        
        x_screen = py5.remap(x,-5,5,border, py5.width - border)
        y_screen = py5.remap(y,-5,5,border,py5.height - border)
        
        py5.circle(x_screen, y_screen,10)
        py5.circle(x_screen, y_screen,10)
        py5.fill(255)
        name = df["Display Name"][i]
        py5.text_size(5)
        py5.text_align(py5.RIGHT)
        py5.text(name,x_screen,y_screen)
        

def setup():
    py5.size(500, 500)
                    
def draw():
    global mode
    mode = 0
    py5.background(0)
    py5.fill(0,255,0)
    draw_grid()
    stars()
    print(mode)
    if mode == 1:
        py5.circle(50)
    
        
py5.run_sketch() 