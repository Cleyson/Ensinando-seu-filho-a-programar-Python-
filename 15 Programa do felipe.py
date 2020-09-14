# SpiralMyname.py - exibe espiral colorida com o nome do osuario

import turtle               # Importa os graficos tartaruga
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red" , "yellow" , "blue" , "green"]
# Pede o nome do usuario usando a janela pop-up do turtle para
# entrada de texto
your_name = turtle.textinput("Enter your name" , "What is your name?")

# Desenha uma espiral na tela usando o nome, escrevendo-o 100 vezes
for x in range(300):
    t.pencolor(colors[x%4]) # Circula pelas quatro cores
    t.penup()               # Nao desenha as linhas normais da espiral
    t.forward(x*4)          # Apenas move a tartaruga pela tela
    t.pendown()             # Escreve o nome do usuário, cada vez maior
    t.write(your_name, font = ("Arial" , int( (x + 4) / 4), "bold"))
    t.left(92)              # Vira a esquerda, como em nossas outras espirais
