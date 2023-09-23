import tkinter as tk

def animate_square(square, dx, dy):
    canvas.move(square, dx, dy)
    canvas.after(10, animate_square, square, dx, dy)

app = tk.Tk()
app.title("Assigment animacija kvadrata")

canvas = tk.Canvas(app, width=500, height=500)
canvas.pack()

square1 = canvas.create_rectangle(200, 200, 300, 300, fill="yellow")
square2 = canvas.create_rectangle(200, 200, 300, 300, fill="yellow")
square3 = canvas.create_rectangle(200, 200, 300, 300, fill="blue")
square4 = canvas.create_rectangle(200, 200, 300, 300, fill="blue")

dx = 2  
dy = 2  

animate_square(square1, -dx, -dy)  
animate_square(square2, dx, -dy)   
animate_square(square3, -dx, dy)   
animate_square(square4, dx, dy)    

app.mainloop()







