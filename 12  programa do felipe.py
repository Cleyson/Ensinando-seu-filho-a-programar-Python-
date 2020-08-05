# AtlantaPizza.py - uma calculadora simples do custo de pizzas
#Pergunte quantas pizzas a pessoa vai querer e obtenha o numero com eval()
number_of_pizzas = eval(input("How many pizzas do you want? "))
#Pergunte o preço de cada pizza, conforme esta no cardapai
cost_per_pizza = eval(input("How mach does each pizza cost? "))
# Calcule o custo total das pizzas como o nosso subtotal
subtotal = number_of_pizzas * cost_per_pizza
# Calcule o imposto sobre vendas devido, como 8% do subtotal
tax_rate = 0.08 # Armazena 8% como o valor decimal 0.08
sales_tax = subtotal * tax_rate
#  Some o imposto sobre vendas ao subtotal para obter o total final
total = subtotal + sales_tax
# Mostra ao usuario o total devido, incluindo o imposto
print("The total cost is $" ,total)
print("This includes $" ,subtotal, "for the pizza and")
print("$" , sales_tax, "in sales tax. ")
