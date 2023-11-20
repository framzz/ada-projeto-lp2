from functools import reduce

# criando função com filter
def filter_data(data: dict, filter_function) -> list:
    return list(filter(filter_function, data))

# função para passar dentro do filter - filtrando apenas os cachorros
def filter_dogs(data: dict):
    return data['species'] == 'Dog'

# função para calcular a soma de idades dos animais
def sum_age(data: dict, attribute: str) -> float:
    return reduce(lambda x, pet: x + pet[attribute], data, 0)

# função para calcular a média de idade dos animais
def average_age(data: dict, reduce_function) -> float:
    return (reduce_function / len(data))

# Função para processar cada pet
def process_pet(pet):
    # Adicionar 5kg ao peso do pet
    pet['weight_plus'] = pet['weight'] + 5
    return pet

def return_statistics_avarage(data, att):
    return average_age(data, sum_age(data, att))