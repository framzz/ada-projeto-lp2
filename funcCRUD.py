from funcoes import valida_opcoes, obter_opcoes, obter_valor

# opter opções 
def input_name() -> str:
    return input('Entre com nome:').title()

def obter_idade() -> int:
    return obter_valor('Entre com idade:', func=int)

def obter_sexo() -> str:
    return input('Entre com sexo').capitalize()

def obter_altura() -> float:
    return obter_valor('Entre com a altura (m):')

def obter_disciplina() -> str:
    return input('Entre com Disciplina: ').capitalize()

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
    
def insert_new(pets: list[dict]) -> bool:
    pets.append({
        'nome': input_name(),
        'idade': obter_idade(),
        'sexo': obter_sexo(),
        'altura': obter_altura(),
        'disciplina': obter_disciplina()
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
    opc = {
        'N': 'Nome',
        'I': 'Idade',
        'A': 'Altura',
        'S': 'Sexo',
        'D': 'Disciplina',
        'F': 'Finalizar'
    }
    
    opc_e = {
        'N' : ('nome', input_name),
        'I' : ('idade', obter_idade),
        'A' : ('altura', obter_altura),
        'S' : ('sexo', obter_sexo),
        'D' : ('disciplina', obter_disciplina),
    }
    
    while True:
        o = obter_opcoes(opc, 'Escolha o campo')
        
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