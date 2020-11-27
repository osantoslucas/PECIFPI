#recebe nas variáveis os valores inteiros
numero1 = int(input('Insira um número: '))
numero2 = int(input('Insira outro número: '))
numero3 = int(input('Insira mais um número: '))

#variável com a média dos três valores inseridos acima
media = (numero1 + numero2 + numero3) / 3

#imprime na tela o resultado da variável media
print(f'A média dos três números é {media:.2f}')
