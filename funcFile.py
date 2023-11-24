import json
import csv
import funcFile as ff
from funcCRUD import input_attribute, obter_opcoes
from funcStatistics import return_statistics_avarage, max_min, input_max_min

# definindo função para leitura de arquivo .json (precisa carregar o .json aqui no colab)
def open_json_file(filepath: str = 'petshop.json') -> list:
    try:
        with open(filepath, "r") as f:
            # lendo e desserializando o conteúdo do arquivo
            return json.load(f)
    # caso não encontre o arquivo, para o programa
    except FileNotFoundError as e:
        raise e

# definindo função para salvar dados
def save_json_file(data: list, filepath: str = 'petshop.json'):
    try:
        with open(filepath, 'w') as f:
            f.write(json.dumps(data))
            return print('Your changes were saved.')
    except Exception as e:
        return print(f'Not able to save your changes. Error {e}')
    
# função para executar as estatisticas
def run_statistics(data, attribute, max_or_min):
    try:
        average = return_statistics_avarage(data, attribute)
        max_min_statistic = max_min(max_or_min, attribute, data)
        return [average, max_min_statistic]
    except Exception as e:
        raise e
        
# função para salvar csv
def save_csv(data: list, attribute: str, max_or_min: str, filename: str = 'petshop.csv'):
    try:
        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f, delimiter=';', lineterminator='\n')
        
            writer.writerow(['Chosen attribute:', attribute])
            writer.writerow(['Average:', round(data[0],2)])
            writer.writerow(['Name', max_or_min + ' ' + attribute])  
            writer.writerows(data[1])
            return print('Your csv is ready!') 
    except Exception as e:
        return print(f'Not able to save your csv. Error {e}')

# função para sair do programa e retornar as estatisticas no csv
def func_exit(data):
    try:
        attribute = input_attribute({'AGE': "Pet's age", 'WEIGHT': "Pet's weight"})
        max_or_min = input_max_min()
        statistics_list = ff.run_statistics(data, attribute, max_or_min)
        if obter_opcoes({'S': 'Sim', 'N': 'Não'}, 'Deseja Sair') == 'S':
            return ff.save_csv(statistics_list, attribute, max_or_min)
    except Exception as e:
        raise e
