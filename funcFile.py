import json
import csv
from funcMaxMin import max_min
from funcMapRedFilter import return_statistics_avarage

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
def save_json_file(data: list, filepath: str = 'petshop.json') -> bool:
    try:
        with open(filepath, 'w') as f:
            f.write(json.dumps(data))
            return True
    except Exception:
        return False
    
# função para executar as estatisticas
def run_statistics(data):
    try:
        avarage = return_statistics_avarage(data)
        max_min_statistic = max_min(data)
        return avarage, max_min_statistic
    except Exception:
        return False
        

# função para salvar csv
def save_csv(data: list, filepath: str = 'petshop.csv'):
  try:
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
        return True
  except Exception:
    return False