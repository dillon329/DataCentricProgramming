y5.circle(x_screen, y_screen, 12)  # highlight
        py5.stroke(0, 255, 0)
        py5.line(x_screen, y_screen, py5.mouse_x, py5.mouse_y)  # line to mouse
        py5.no_stroke()