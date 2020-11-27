# recebe os valores correspondentes a largura, altura e comprimento da sala
largura = float(input('Insira a largura da sala: '))
altura = float(input('Insira a altura da parede da sala: '))
comprimento = float(input('Insira o comprimento da sala: '))

# calcula os valores de área e volume
area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_paredes = (2 * altura * largura) + (2 * altura * comprimento)

#exibe na tela os valores
print(f'A área do piso é igual a {area_piso}m².')
print(f'O volume da sala é igual {volume_sala}m³.')
print(f'A área das paredes é igual a {area_paredes}m².')
                    
