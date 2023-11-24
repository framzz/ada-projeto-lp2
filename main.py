# importando libs necessária para o projeto
import funcFile as ff
import funcCRUD as fc
from funcStatistics import filter_data

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
    'U': 'Update', #OK
    'D': 'Delete', #OK
    'F': 'Find', #OK
    'SA': 'Show All', #OK
    'FI': 'Filter',
    'EX': 'Exit' #OK
}

opc_func = {
    'I': fc.insert_new,
    'D': fc.delete,
    'U': fc.update,
    'SA': fc.show_all,
    'FI': fc.entering_func,
    'F': lambda data: print(fc.formatting_all_pets(fc.find_pet(data, fc.input_name()))),
    'EX': ff.func_exit
}

s = True
while s == True:
    try:
        data = ff.open_json_file()   
    except Exception as e:
        print(f'File not found. Error: {e}') 
        break  
    option = fc.obter_opcoes(opc, 'Choose and action: ')
    opc_func[option](data)
    ff.save_json_file(data)

    if option == 'FI':
        print("Here's your filtered data: ")
        print(filter_data(data))
    elif option == 'EX':
        s = False