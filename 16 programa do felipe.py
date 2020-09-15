import turtle                   # Importa os graficos tartaruga
t = turtle.Pen()

turtle.bgcolor("black")
# Cria uma lista com 8 nomes de cores validas quaisquer em python
colors = ["red" , "yellow" , "blue" , "green" , "orange" , "purple" , "white" , "gray"]
# Pede ao usuario o numero de lados, entre 1 e 8, com um default igual a 4
sides = int(turtle.numinput("Nuber of sides" ,
                            "Hot many sides do you want (1-8)?" , 4, 1, 8))
# Desenhe uma espiral colorida com o numero de lados especificado pelo usuario
for x in range(360):
    t.pencolor(colors[x % sides]) # Utiliza somente a quantidade certa de cores
    t.forward(x * 3 / sides + x)  # Muda o tamanho para que correponda ao # numero de lados
    t.left(360 / sides + 1)       # Gira 360² / numero de lados, mais 1
    t.width(x * sides / 200)      # Aumenta alargura da caneta a medida # que avaçamos para a parte mais externa
