import turtle
t = turtle.Pen()
turtle.bgcolor("green")
# Peça ao usuario que fornese o numero de circulos em sua roseta, com # default igual a 6
number_of_circles = int(turtle.numinput("Number of circles","How many circle in your rosette?" , 6))
for x in range(number_of_circles):
    t.circle(100)
    t.left(360/number_of_circles)
    
