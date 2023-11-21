from functools import reduce
from funcCRUD import input_attribute, obter_opcoes

# função para filtrar 
def filter_data(data):
    option = input('Choose what attribute you want to filter: name, age, species, breed, weight, fur_color: ').lower()
    filter_value = input(f'Enter the value for {option}: ').strip().capitalize()  # Capturar o valor a ser filtrado
    
    if option in ('name', 'species', 'breed', 'fur_color'):
        filter_value = filter_value.capitalize()  # Garantir que as strings sejam capitalizadas para comparação
        return list(filter(lambda pet: str(pet.get(option)).strip().capitalize() == filter_value, data))
    elif option == 'age':
        filter_value = int(filter_value)  # Converter a entrada para inteiro
        return list(filter(lambda pet: int(pet.get(option)) == filter_value, data))
    elif option == 'weight':
        filter_value = float(filter_value)  # Converter a entrada para float
        return list(filter(lambda pet: float(pet.get(option)) == filter_value, data))
    else:
        return []

# função para calcular a soma de idades dos animais
def sum_age(data: list[dict], attribute: str) -> float:
    return reduce(lambda x, pet: x + pet[attribute], data, 0)

# função para calcular a média de idade dos animais
def average_age(data: dict, reduce_function) -> float:
    return (reduce_function / len(data))

def return_statistics_avarage(data, att):
    return average_age(data, sum_age(data, att))

# função para retornar o registro maximo de um atributo 
def max_attribute_value(data: dict, attribute: str) -> list:
    max_value = max(data, key=lambda x: x[attribute])[attribute]
    return [(pet['name'], pet[attribute]) for pet in data if pet[attribute] == max_value]

# função para retornar o registro minimo de um atributo 
def min_attribute_value(data: dict, attribute: str) -> list:
    min_value = min(data, key=lambda x: x[attribute])[attribute]
    return [(pet['name'], pet[attribute]) for pet in data if pet[attribute] == min_value]

opc_max_min = {
    'MAX': 'Máximo', #salvando dados 
    'MIN': 'Mínimo'
}
opc_att = {'AGE': "Pet's age", 'WEIGHT': "Pet's weight"}

def input_max_min() -> str:
    return obter_opcoes(opc_max_min, 'Choose an input: ')

def max_min(opc_max_min: str = input_max_min , att: str = input_attribute, data = dict) -> list:
    if opc_max_min == 'MAX':
        return max_attribute_value(data, att)
    elif opc_max_min == 'MIN':
        return min_attribute_value(data, att)
    else:
        return []