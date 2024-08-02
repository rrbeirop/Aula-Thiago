from classes import*
from views import*

dog = []
rcs =["Vira-lata", "Shih Tzu", "Yorkshire", "Poodle", "Buldogue Francês", "Pinscher"]

human = []

def rc():
  
  for i in(rcs):
    print(f"{i}")

def criar_cao():
        nome = input("DEFINA UM NOME AO CÃO:")
        rc()
        raca = input("ESCOLHA UMA RAÇA:")
        tamanho = input("QUAL TAMANHO:")
        cor = input("DEFINA UMA COR:")
        cao = Dog(nome,tamanho, raca, cor)
        dog.append(cao) 
        
      
def criar_humano():
    
        nome = input("DEFINA UM NOME:")
        sexo = input("DEFINA O SEXO:")
        idade = input("DEFINA UMA IDADE:")
        hm = Humano(nome, sexo, idade)
        human.append(hm)

        return menu
# def sair():
#         print("SAIIIIIIIIR")
    

while True:
    print(menu())
    op = input("INFORME SUA OPÇÃO:")
    if op == "1":
        criar_cao()
        

    elif op == "2":
        criar_humano()
    
    # elif op == "3":
    #     sair()

