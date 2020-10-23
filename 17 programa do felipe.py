print("MathHomework.py")
# Pede ao usuario que forneça um problema matemateco
problem = input("Enter a math problem, or 'q' to quit: ")
# Continua ate que o usuario entre com 'q' para sair (quit)
while (problem != "q"):
    # Apresenta o problema, e mostra a resposta usando eval()
    print("The answer to " , problem, "is:" ,eval(problem) )
    # Pede outro probema matematico
    problem = input("Enter another math problem, or 'q' to quit: ")
    # Este laço while continuara ate voce entra com 'q' para sair (quit)
    
    
 
