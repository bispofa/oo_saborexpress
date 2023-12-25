class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

status = 'ativo' if {restaurante_praca.ativo} else 'inativo'

print(f'restaurante {restaurante_praca.nome} esta {status}')

restaurante_praca.nome = 'Bistro'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

if restaurante_pizza.categoria == 'Fast Food':
    print ('Categoria validada')
else:
    print ('categotia invalida')

restaurante_pizza.ativo = True

print(f'{restaurante_pizza.nome} pertence a categoria {restaurante_pizza.categoria}')

print('teste')

