__all__ = [
    'calcular',
    'fatorial',
    'historico',
    'lista_numeros',
    'pares',
    'impares',
    'velocidade',
    'cinetica',
    'celsius',
    'fahrenheit',
    'separar',
    'vogais',
    'letras',
    'espacos',
    'palavras_u',
    'proibido',
    'substituir',
    'numero_texto',
    'numero_palavra',
    'tipo_triangulo',
    'area_circulo',
    'area_triangulo'
]

class Calculadora:
    """
    \nimport Library as L
    \ncalculadora = L.Calculadora()
    \ncalculadora."FUNÇÃO"(args)
    """
    def __init__(self):
        self.historico: list[str] = []
        
    def calcular(self, ex: str, n1: float, n2: float) -> float:
        """Calcula um resultado

        Args:
            ex (str): Operação realizada
            n1 (float): Primeiro número
            n2 (float): Segundo número
            
        """
        if ex not in ['+', '-', '*', '/']:
            raise ValueError ('Operação inválida')
        if ex == '+':
            resultado = (n1+n2)
        elif ex == '-':
            resultado = (n1-n2)
        elif ex == '*':
            resultado = (n1*n2)
        elif ex == '/':
            if n2 == 0:    
                raise ZeroDivisionError ('Não pode dividir por 0')
            resultado = (n1/n2)
        

        self.historico.append(f'{n1} {ex} {n2} = {resultado}')
        return(resultado)
    
    def fatorial(self, número: int) -> int:
        """Calcular o fatorial de um número

        Args:
            número (int): Número que será calculado
        """
        fatorial = 1
        for i in range(número):
            fatorial *= i+1
        
        self.historico.append(f'{número}! = {fatorial}')
        return(fatorial)
    
    def retorno(self, n0: int, ex: str, n2: float) -> float:
        """
        """
        numero = self.historico[n0]
        resultado = calcular(ex, int(numero[-1]), n2)
        self.historico.append(f'{numero} {ex} {n2} = {resultado}')
        return(resultado)
    
    def pegar_historico(self) -> str:
        """Retorna o histórico da calculadora"""
        return '\n'.join(self.historico)
    
    def lista_numeros(self, n1: int, n2: int) -> list:
        """Cria uma lista com números de números randômicos
        
        Args:
            n1 (int): Tamanho da lista
            n2 (int): Valor máximo da lista
        """
        import random

        lista = [random.randrange(1, n2) for numero in range(n1)]
        return(lista)
        
    def par(self, lista: list) -> list:
        """Analisa uma lista e cria outra com os valores pares

        Args:
            numeros (list): Lista de números
        """
        return [numero for numero in lista if not numero %2 and numero != 0]
    
    def impar(self, lista: list) -> list:
        """Analisa uma lista e cria outra com os valores impares

        Args:
            numeros (list): Lista de números
        """
        return [numero for numero in lista if numero %2 and numero != 0]

class Física:
    def __init__(self):
        pass
    
    def velocidade(self, distancia: float, tempo: float):
        """Calcula a velocidade de um objeto
        Args:
        distancia (float): Distância percorrida
        tempo (float): Tempo gasto
        """
        velocidade = distancia / tempo
        return(f'{round(velocidade,2)}m/s')
    
    def energia_cinetica(self, velocidade: float, peso: float):
        """Calcula a energia cinética produzida por um objeto

        Args:
            velocidade (float): Velocidade em Km/H
            peso (float): Peso em Kg
        """
        mps = velocidade/3.6
        cinetica = ((peso/2)*(mps)**2)
        return(f'{round(cinetica,2)}J')
    
    def temperaturaC(self, temperatura: float):
        """Converte uma temperatura de ºC para ºF
        Args:
            temperatura (float): Temperatura em ºC
        """
        temp_f = (temperatura*1.8)+32
        return(f'{round(temp_f,2)}ºF')

    def temperaturaF(self, temperatura: float):
        """Converte uma temperatura de ºF para ºC
            Args:
        temperatura (float): Temperatura em ºF
        """
        temp_ºC = (temperatura-32)/1.8
        return(f'{round(temp_ºC,2)}ºC')
    
    def cilindro_agua(m: float, h: float, r: float) -> float:
        """Testa se um cilindro boia na água

        Args:
            m (float): Massa em g
            h (float): Altura em cm
            r (float): Raio em cm
        """
        v_lata = round(3.14*r**2*h,2)
        d_lata = round(m/v_lata,2)
        if d_lata >= 1:
            return('A lata irá afundar na água')
        elif d_lata == 1:
            return('A lata ficará suspensa no meio da água')
        else:
            return('A lata irá boiar na água')


class Texto:
    def __init__(self):
        self.relatorio = []

    def separar_letras(self, texto: str):
        """Separar as letras de um texto e
        Quebra uma lista em partes menores
        
        Args:
            texto (str): Texto que será separado
        """
        lista_quebrada = [k for p in texto for k in p]
        return(lista_quebrada)

    def quant_vogais(self, texto: str):
        """Conta quantas vogais estão presentes em um texto

        Args:
            texto (str): Texto a ser analisado
        """
        vogal = ['a', 'á', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'y']
        alterar = texto.lower().split()
        vogais_totais = 0
        for cédulas in alterar:
            for letra in cédulas:
                if letra in vogal:
                    vogais_totais += 1

        self.relatorio.append(f'O total de vogais é: {vogais_totais}')   
        return(vogais_totais)
    
    def quant_palavras(self, texto: str) -> int:
        """Conta quantas palavras estão presentes em um texto
        
        Args:
            texto (str): Texto a ser analisado
        """
        self.relatorio.append(f'O total de palavras é: {len(texto.split())}')   
        return(len(texto.split()))

    def quant_letras(self, texto: str):
        """Conta o total de letras presentes no texto

        Args:
            texto (str): Texto a ser analisado
        """
        letras_totais = 0
        for cédulas in texto:
            for letras in cédulas:
                if letras != ' ':
                    letras_totais += 1
        
        self.relatorio.append(f'O total de letras é: {letras_totais}')
        return(letras_totais)

    def quant_espacos(self, texto: str):
        """Conta o total de espaços presentes no texto

        Args:
            texto (str): Texto a ser analisado
        """
        espacos_totais = 0
        for espaço in range(len(texto)):
            if ' ' in texto[espaço]:
                espacos_totais += 1
        
        self.relatorio.append(f'O total de espaços é: {espacos_totais}')
        return(espacos_totais)

    def quant_palavras_unicas(self, texto: str):
        """Conta o número de palavras únicas presentes no texto

        Args:
            texto (str): Texto a ser analisado
        """
        alterar = texto.split()
        palavras = set(alterar)

        self.relatorio.append(f'O total de palavras únicas é: {len(palavras)}')
        return(len(palavras))
    
    def quant_letras_unicas(self, texto: str):
        """Conta o número de letras únicas presentes no texto

        Args:
            texto (str): Texto a ser analisado
        """
        letras = set(texto)

        self.relatorio.append(f'O total de letras únicas é: {len(letras)}')
        return(len(letras))

    def palavras_proibidas(self, entrada: str, proibido: list):
        """Barra um texto que contenha palavras indesejadas

        Args:
            entrada (str): Texto a ser analisado
            proibido (list): Lista de palavras indesejadas (.lower())
        """
        texto = entrada.lower().split()
        for palavra in texto:
            if palavra in proibido:
                return('Texto não autorizado')
        else:
            return(entrada)
        
    def substituir_palavra(self, entrada: str, substituida: str, substituidora: str):
        """Substitui uma palavra de um texto

        Args:
            entrada (str): Texto que sofrerá a mudança
            substituida (str): Palavra que será subistituída
            substituidora (str): Palavra nova
        """
        texto = entrada.lower().split()
        for i in range(len(texto)):
            texto[i] = texto[i].replace(substituida, substituidora)
        return(' '.join(texto).capitalize())
    
    def pegar_relatorio(self) -> str:
        """Gera um relatório com as informações do texto"""
        return '\n'.join(self.relatorio)
    
    def extrair_numero_de_texto(texto: str):
        """Extrai os números de um texto
        
        Args:
            texto (str): Texto que contém o número
        """
        numeros = [int(palavra) for palavra in texto.split() if palavra.isdigit()]
        return(numeros)

    def extrair_numero_de_palavra(palavra: str):
        """Extrai os números de palavras
        
        Args:
            texto (str): Texto que contém o número
        """
        letras = (palavra)
        numeros = [int(letra) for letra in letras if letra.isdigit()]
        return(numeros)

class Geometria:
    def __init__(self):
        self.relatorio = []
    
    def tipo_triangulo(self, lados: list) -> float:
        """Descobre o tipo do triângulo

        Args:
            lados (list): Lista com as medidas dos lados do triângulo
        """
        if lados[0]+lados[1]+lados[2] > 90:
            return('Não é triângulo')
        elif lados[0] == lados[1] and lados[0] == lados[2]:
            return('O triângulo é equilátero')
        elif lados[0] != lados[1] and lados[1] == lados[2] or lados[0] == lados[1] and lados[1] != lados[2] or lados[0] == lados[2] and lados[1] != lados[2]:
            return('O triângulo é isósceles')
        else:
            return('O triângulo é escaleno')
    def area_circulo(self, raio: float) -> float:
        """Calcula a área de um círculo

        Args:
            raio (float): Raio em m
        """
        return(round(3.14159*raio**2, 4))
    
    def area_triangulo(self, b: float, h: float) -> float:
        """Calcula a área de um triângulo

        Args:
            b (float): Base do triângulo em M
            h (float): Altura do triângulo em M
        """
        return(b*h)/2

_inst = Calculadora()
calcular = _inst.calcular
fatorial = _inst.fatorial
historico = _inst.pegar_historico()
retorno = _inst.retorno
lista_numeros = _inst.lista_numeros
pares = _inst.par
impares = _inst.impar

_inst = Física()
velocidade = _inst.velocidade
cinetica = _inst.energia_cinetica
celsius = _inst.temperaturaC
fahrenheit = _inst.temperaturaF
cilindro_agua = _inst.cilindro_agua

_inst = Texto()
separar = _inst.separar_letras
vogais = _inst.quant_vogais
letras = _inst.quant_letras
palavras = _inst.quant_palavras
espacos = _inst.quant_espacos
palavras_u = _inst.quant_palavras_unicas
letras_u = _inst.quant_letras_unicas
proibido = _inst.palavras_proibidas
substituir = _inst.substituir_palavra
numero_texto = _inst.extrair_numero_de_texto
numero_palavra = _inst.extrair_numero_de_palavra

_inst = Geometria()
tipo_triangulo = _inst.tipo_triangulo
area_circulo = _inst.area_circulo
area_triangulo = _inst.area_triangulo
#if __name__ == '__main__':