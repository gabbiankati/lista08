def maior_numero(n1: int, n2: int) -> int:
   """

   :type n2: object
   """
   return n1 if n1 > n2 else n2

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
valor = maior_numero(n1,n2)
print(f'O maior número informado é {valor}')
