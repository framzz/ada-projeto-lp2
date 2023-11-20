from funcoesProfessor import obter_opcoes
from funcCRUD import input_attribute 

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

def input_max_min() -> str:
    return obter_opcoes(opc_max_min, 'Choose an input: ')

def max_min(opc_max_min: str = input_max_min , att: str = input_attribute, data = dict) -> list:
    if opc_max_min == 'MAX':
        return max_attribute_value(data, att)
    elif opc_max_min == 'MIN':
        return min_attribute_value(data, att)
    else:
        return []