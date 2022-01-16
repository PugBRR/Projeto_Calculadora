class calculos():
    def __init__(self):
        self.funcoes = {
            "soma": self.soma,
            "subtracao": self.subtracao,
            "multiplicacao": self.multiplicacao,
            "divisao": self.divisao,
            "quadrado": self.quadrado,
            "raiz_quadrada": self.raiz_quadrada,
            "porcentagem": self.porcentagem
        }
        
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

    def multiplicacao(self, x, y):
        return x * y

    def divisao(self, x, y):
        return x / y

    def quadrado(self, x):
        return x ** 2

    def raiz_quadrada(self, x):
        return x ** (1/2)

    def porcentagem(self, x, y):
        return (x * y) / 100

if __name__ == '__main__':
    calculos = calculos()
    resultado = calculos.funcoes['soma'](1, 4)
    print(resultado)