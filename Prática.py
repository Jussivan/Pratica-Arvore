class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if valor is None:
            return
        if self.raiz is None:
            self.raiz = No(valor)
            return
        fila = [self.raiz]
        while fila:
            no_atual = fila.pop(0)
            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = No(valor)
                    return
                else:
                    fila.append(no_atual.esquerda)
            else:
                if no_atual.direita is None:
                    no_atual.direita = No(valor)
                    return
                else:
                    fila.append(no_atual.direita)

    def altura(self, no):
        if no is None:
            return 0
        altura_esquerda = self.altura(no.esquerda)
        altura_direita = self.altura(no.direita)
        return max(altura_esquerda, altura_direita) + 1

    def contar_int(self, no):
        if no is None:
            return 0
        if no.esquerda or no.direita:
            return 1 + self.contar_int(no.esquerda) + self.contar_int(no.direita)
        else:
            return 0

    def folhas(self, no):
        if no is None:
            return 0
        if no.esquerda is None and no.direita is None:
            return 1
        else:
            return self.folhas(no.esquerda) + self.folhas(no.direita)

    def buscar(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if valor < no.valor:
            return self.buscar(no.esquerda, valor)
        else:
            return self.buscar(no.direita, valor)