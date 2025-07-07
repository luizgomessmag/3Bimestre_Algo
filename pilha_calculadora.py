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
            auxiliar = self.top
            self.top = self.top.next
            self.size -= 1
            return auxiliar

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

    opcao = ""
    

    while opcao != "x":

        opcao = input("Deseja adicionar qual tipo de valor? (Operando/Operador) ou x para sair\n").lower()

        if opcao == "operando":
            operando = int(input("Insira o operando\n"))
            pilha.push(No(operando))

        elif opcao == "operador":
            
            if pilha.tamanho()>=2:
            
                operador = input("escolha um dos seguintes: (+, -, *, /, ^, !, %)\n")

                b = pilha.pop().valor
                a = pilha.pop().valor

                # b = pilha.top.valor
                # a = pilha.top.next.valor
                resultado = None

                if operador == "+":
                    resultado = a+b

                elif operador == "-":
                    resultado = a-b

                elif operador == "*":
                    resultado = a*b

                elif operador == "/":
                    if b != 0:
                        resultado = a/b
                    else:
                        pilha.push(No(a))
                        pilha.push(No(b))

                elif operador == "^":
                    resultado = a^b

                elif operador == "%":
                    resultado = a%b
                
                else:
                    print("Erro na sintaxe")

                
                if resultado is not None:
                    pilha.push(No(resultado))
                    print(f"{a} {operador} {b} = {resultado}")


        elif opcao == "x": 
            print("pilha finalizada")
            print(pilha)

        else:
            print("Erro")



#FINALIZAR
