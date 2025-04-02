def soma_lista(numeros):
    soma = 0
    for num in numeros:
        soma += num  # Ponto de parada aqui
    return soma

def media_lista(numeros):
    total = soma_lista(numeros)  # Chama a função soma_lista
    return total / len(numeros)  # Possível erro se lista estiver vazia

# Lista de números
valores = [10, 20, 30, 40, 50]

# Chamando as funções
soma = soma_lista(valores)
print(f"Soma: {soma}")

media = media_lista(valores)
print(f"Média: {media}")

# Teste com lista vazia para ver erro no debug
teste_vazio = [5, 12, 17, 21]
print(f"Média da lista vazia: {media_lista(teste_vazio)}")  # Isso vai gerar um erro # Alterei a lista vazia e adicionei os números 5, 12, 17, 21.
