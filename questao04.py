#recebe os valores
hora = int(input('Insira a hora: '))
minuto = int(input('Insira os minutos: '))
segundo = int(input('Insira os segundos: '))

# atribui à variável o calculos dos segundos
segundos = (hora * 3600) + (minuto * 60) + segundo

# exibe na tela os valores
print(f'Passaram-se {segundos} segundos desde a última meia noite.')
