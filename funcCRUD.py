from funcoesProfessor import valida_opcoes, obter_opcoes, obter_valor

# opter opções 
def input_name() -> str:
    return input('Entre com nome: ').title()

def input_age() -> int:
    return obter_valor('Entre com idade: ', func=int)

def input_species() -> str:
    return input('Entre com a especie: ').capitalize()

def input_breed() -> str:
    return input('Entre com a raça: ').title()

def input_weight() -> float:
    return input('Entre com o peso: ')

def input_fur() -> str:
    return input('Entre com nome: ').title()

def input_attribute() -> str:
    return obter_opcoes({'AGE': "Pet's age", 'WEIGHT': "Pet's weight"}, 'Choose an input: ').lower()

# formata um pet
def formatting_pet_data(pet: dict) -> str:
    return '\n'.join([f'{key.title()}: {value}' for key, value in pet.items()])

# formata todos os pets
def formatting_all_pets(pets: dict):
    return '\n\n'.join(list(map(formatting_pet_data, pets)))

# procurando o nome do animal dentro dos dados
def find_pet(data: dict, name: str) -> list:
  return [pet for pet in data if pet['name'] == name]

# retorna todos os pets
def show_all(pets: dict)-> bool:
    print(formatting_all_pets(pets))
    return True
    
def insert_new(pets: dict) -> bool:
    pets.append({
        'name': input_name(),
        'age': input_age(),
        'spc': input_species(),
        'breed': input_breed(),
        'weight': input_weight(),
        'fur': input_fur()
    })
    
    return True
    
def delete(pets: dict) -> bool:
    apagado = find_pet(pets, input_name())
    
    if len(apagado) == 0:
        print('Não foi encontrado!')
        return False
    
    apagado = apagado[0]
    
    msg = f'Tem certeza que deseja excluir [{formatting_pet_data(apagado)}]'
    
    if obter_opcoes({'S': 'Sim', 'N': 'Não'}, msg) == 'S':
        pets.remove(apagado)
        return True
    else:
        return False

def exec_alteration(prof: dict) -> None:
    opc_pet = {
        'NAME': "Pet's name",
        'AGE': "Pet's age" ,
        'SPC': "Pet's species",
        'BREED': "Pet's breed",
        'WEIGHT': "Pet's weight",
        'FUR': "Pet's fur color",
    }
    
    opc_e = {
        'N' : ('name', input_name),
        'A' : ('age', input_age),
        'S' : ('spc', input_species),
        'B' : ('breed', input_breed),
        'W' : ('weight', input_weight),
        'F' : ('fur', input_fur),
    }
    
    while True:
        o = obter_opcoes(opc_pet, 'Escolha o campo')
        
        if o == 'F':
            break
        
        prof[opc_e[o][0]] = opc_e[o][1]()

def update(profs: dict) -> bool:
    alterado = find_pet(profs, input_name())
    
    if len(alterado) == 0:
        print('Não foi encontrado!')
        return False
    
    alterado = alterado[0]
    
    msg = f'Tem certeza que deseja alterar [{formatting_pet_data(alterado)}]'
    
    if obter_opcoes({'S': 'Sim', 'N': 'Não'}, msg) == 'S':
        exec_alteration(alterado)    
        return True
    else:
        return False