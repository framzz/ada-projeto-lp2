# importando libs necessária para o projeto
from funcoesProfessor import obter_opcoes
import funcFile as ff
from funcCRUD import show_all, insert_new, delete, update, formatting_all_pets, find_pet, input_name

opc_pet = {
    'NAME': "Pet's name",
    'AGE': "Pet's age" ,
    'SPC': "Pet's species",
    'BREED': "Pet's breed",
    'WEIGHT': "Pet's weight",
    'FUR': "Pet's fur color",
}

opc = {
    'I': 'Insert', #OK 
    'U': 'Update', 
    'D': 'Delete', #OK
    'F': 'Find', #OK
    'SA': 'Show All', #OK
    #'EX': 'Sair'
}

opc_func = {
    'I': insert_new,
    'D': delete,
    'U': update,
    'SA': show_all,
    'F': lambda data: print(formatting_all_pets(find_pet(data, input_name())))
}

while True:
    data = ff.open_json_file()
    opc_func[obter_opcoes(opc, 'Escolha uma ação')](data)
    ff.save_json_file(data)
    

    if obter_opcoes({'S': 'Sim', 'N': 'Não'}, 'Deseja Sair') == 'S':
        ff.save_csv(ff.run_statistics(data))
        break