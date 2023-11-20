from funcoesProfessor import obter_opcoes

# função para retornar o registro maximo de um atributo 
def max_attribute_value(data: dict, attribute: str) -> list:
    max_value = max(data, key=lambda x: x[attribute])[attribute]
    return [(pet['name'], pet[attribute]) for pet in data if pet[attribute] == max_value]

# função para retornar o registro minimo de um atributo 
def min_attribute_value(data: dict, attribute: str) -> list:
    min_value = min(data, key=lambda x: x[attribute])[attribute]
    return [(pet['name'], pet[attribute]) for pet in data if pet[attribute] == min_value]


def max_min(opc_max_min: dict, opc_att: dict, data) -> list:
    option = obter_opcoes(opc_max_min, 'Choose an input: ')
    att = obter_opcoes(opc_att, 'Choose an input: ').lower()
    if option == 'MAX':
        return max_attribute_value(data, att)
    elif option == 'MIN':
        return min_attribute_value(data, att)
    else:
        return []