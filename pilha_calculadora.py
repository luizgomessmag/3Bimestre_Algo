# Leia um caractere da notação.
# Se for um operando, empilhe-o, isto é, coloque-o no topo da
# pilha.
# Mas se ele for um operador, retire o penúltimo e o último
# operando da pilha. Faça a operação que se pede entre eles e
# coloque o resultado de volta na pilha.
# Repita todos os passos acima até que toda a notação seja lida.
# O resultado será o que sobrou na pilha


class No: 
    def __init__(self, valor):
        self.valor = valor
        self.next = None
#elemento que define
class Pilha:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
#elemento que adiciona valores na pilha
    def push(self, no):
        no.next = self.top
        self.top = no
        self.size += 1
        print(f"elemento {no.valor} inserido")
#elemento que retorna a situação da lista
    def __str__(self):
        if self.top is not None:
            no = self.top
            pilha_listagem = []
            while no is not None:
                pilha_listagem.append(f"{no.valor}")
                no = no.next
            return "\n-----\n".join(pilha_listagem)
        else:
            return "a pilha está vazia"
            
    #Pop() = altera o valor do topo   
    def pop(self):
        if(self.size > 0):
            self.top = self.top.next
            self.size -= 1

    def topo(self):
        if self.top is not None:
            return self.top.valor
        else:
            return "a pilha está vazia"
        
    def tamanho(self):
        return self.size

if __name__ == "__main__":
    pilha = Pilha()
    # print(pilha)
    # #Push = entrada de dado no sistema
    # pilha.push(No(1))
    # print("O tamanho da pilha: ", pilha.tamanho())
    # print("Elemento topo: ", pilha.topo())
    # pilha.push(No(3))
    # print("O tamanho da pilha: ", pilha.tamanho())
    # print("Elemento topo: ", pilha.topo())
    # pilha.push(No(4))
    # print("O tamanho da pilha: ", pilha.tamanho())
    # print("Elemento topo: ", pilha.topo())
    # pilha.pop()
    # print("O tamanho da pilha: ", pilha.tamanho())
    # print("Elemento topo: ", pilha.topo())
    # print(pilha)

    sair = ""
    

    while sair != "x":

        opcao = input("Deseja adicionar qual tipo de valor? (Operando/Operador)\n").lower()

        if opcao == "operando":

            pilha.push(No(int(input("Insira o valor\n"))))
            sair = input("deseja continuar? (s/x)\n")

        elif opcao == "operador":

            print("escolha um dos seguintes: (+, -, *, /, ^, !, %)")
            pilha.push(No(str(input("Escolha um dos seguintes valores fornecidos\n"))))
            sair = input("deseja continuar? (s/x)\n")
            if len(pilha)>=2: self.top 

    else: 
        print("pilha finalizada")
        print(pilha)



#FINALIZAR


    
