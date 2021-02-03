# Pede o nome do usuario

name = input("What is your name? ")

# Continua exibindo os nomes ate pedirmos que pare
while name != "":
    # Exibe o nome do usuario 100 vazes
    for x in range(100):
        # Exibe o nome do usuario seguido de um espaço, e nao de uma # quebra de linha
     print(name, end = " ")
     print()
        # Apos o laço for , pula para a proxima linha
        #Pede outro nome, ou termina
        name = input("Type another name, or just hit [ENTER] to quit: ")
print("Thanks for playing!")
        
