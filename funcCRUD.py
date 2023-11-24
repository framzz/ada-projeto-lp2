# função para validar opções 
def valida_opcoes(valor: str, opcoes: list) -> bool:
    return valor in opcoes

# função para obter opções 
def obter_opcoes(opcoes, msg='Opções'):
    msg = f"{msg} ({' | '.join([f'{key} - {values}' for key, values in opcoes.items()])}):" 
    
    while True:
        valor = input(msg).upper()
    
        if valida_opcoes(valor, opcoes.keys()):
            break
        
        msg = f'Entrada Inválida! As opções validas são {", ".join(opcoes.keys())} \n' + msg
        
    return valor

# função para obter valor 
def obter_valor(msg='', func=float):
    
    while True:
        valor = input(msg)
        try:
            return list(map(func, [valor]))[0]
        except ValueError:
            msg = f'Entrada Inválida! {msg}'

# funções para receber o input de opções 
def input_name() -> str:
    return input("Enter the pet's name: ").title()

def input_age() -> int:
    return obter_valor("Enter the pet's age: ", func=int)

def input_species() -> str:
    return input("Enter the pet's species: ").capitalize()

def input_breed() -> str:
    return input("Enter the pet's breed: ").title()

def input_weight() -> float:
    return obter_valor("Enter the pet's weight: ", func=float)

def input_fur() -> str:
    return input("Enter the pet's fur color: ").title()

def input_attribute(options) -> str:
    return obter_opcoes(options, 'Choose an attribute: ').lower()

def entering_func(data) -> str:
    return print(f'Entering filter on {data}...')

# formata um pet
def formatting_pet_data(pet: dict) -> str:
    return '\n'.join([f'{key.title()}: {value}' for key, value in pet.items()])

# formata todos os pets - USANDO MAP
def formatting_all_pets(pets: dict):
    return '\n\n'.join(list(map(formatting_pet_data, pets)))

# procurando o nome do animal dentro dos dados
def find_pet(data: dict, name: str) -> list:
    try:
        return [pet for pet in data if pet['name'] == name]
    except Exception:
        return []

# retorna todos os pets
def show_all(data: dict)-> bool:
    print(formatting_all_pets(data))
    return True

# insere novo pet
def insert_new(data: dict) -> bool:
    data.append({
        'name': input_name(),
        'age': input_age(),
        'species': input_species(),
        'breed': input_breed(),
        'weight': input_weight(),
        'fur_color': input_fur()
    })

    return True

# deletando um pet
def delete(data: dict) -> bool:
    try:
        deleted = find_pet(data, input_name())

        if len(deleted) == 0:
            print(f'{deleted} does not exist in our database!')
            return False

        deleted = deleted[0]

        msg = f'Are you sure you want to delete the following pet: [{formatting_pet_data(deleted)}]?'

        if obter_opcoes({'Y': 'Yes', 'N': 'No'}, msg) == 'Y':
            data.remove(deleted)
            return True
        else:
            return False
    except Exception as e:
        print(f'Could not delete the pet. Error {e}')

def exec_alteration_update(data: dict) -> None:
    opc = {
        'N': 'name',
        'A': 'age',
        'S': 'species',
        'B': 'breed',
        'W': 'weight',
        'F': 'fur_color',
        'E': 'end'
    }
    
    while True:
        match obter_opcoes(opc, 'Escolha o campo'):
            case 'E':
                break
            case 'N':
                data['name'] = input_name()
            case 'A':
                data['age'] = input_age()
            case 'S':
                data['species'] = input_species()
            case 'B':
                data['breed'] = input_breed()
            case 'W':
                data['weight'] = input_weight()
            case 'F':
                data['fur_color'] = input_fur()

def update(pets: dict) -> bool:
    try:
        updated = find_pet(pets, input_name())

        if len(updated) == 0:
            print(f'{updated} does not exist in our database!')
            return False

        updated = updated[0]
        msg = f'Are you sure you want to update the following pet: [{formatting_pet_data(updated)}]'

        if obter_opcoes({'Y': 'Yes', 'N': 'No'}, msg) == 'Y':
            exec_alteration_update(updated)
            return True
        else:
            return False
    except Exception as e:
        print(f'Could not update the pet. Error {e}')
    
