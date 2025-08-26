# Passo 1: Crie uma tupla
tupla_original = ('Maçã', 'Banana', 'Cereja', 'Morango')
print(f"Tupla original: {tupla_original}")

# Passo 2: Percorra a tupla
print("Percorrendo a tupla:")
for fruta in tupla_original:
    print(f"- {fruta}")

# Passo 3: Converta a tupla em uma lista
# Lembre-se: tuplas são imutáveis, então precisamos convertê-la para modificar seus itens.
lista_de_frutas = list(tupla_original)
print(f"Lista convertida: {lista_de_frutas}")

# Passo 4: Altere a lista (adicionando um item)
lista_de_frutas.append('Manga')
print(f"Lista alterada: {lista_de_frutas}")

# Passo 5 (Opcional): Converta a lista de volta para uma tupla, se precisar
nova_tupla = tuple(lista_de_frutas)
print(f"Nova tupla: {nova_tupla}")

# Passo 6: Imprima as tuplas para comparar
print(f"Tupla original (não alterada): {tupla_original}")
print(f"Nova tupla (com item adicionado): {nova_tupla}")