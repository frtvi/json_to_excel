import pandas as pd
import json

# função pra ler o json e carregar excel
def json_to_excel(json_file, excel_file):
    # carrega o json
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    results = json_data['d']['results']

    # criar o dataframe
    df = pd.DataFrame(results)

    # salva o dataframe em excel
    df.to_excel(excel_file, index=False)
    print(f"Arquivo Excel salvo em: {excel_file}")

# especificar o caminho dos arquivos
json_file_path = 'C:/Users/random/data.json'  # ONDE ESTÁ O JSON
excel_file_path = 'C:/Users/random/data.xlsx'  # ONDE DESEJA SALVAR O EXCEL

# chama função
json_to_excel(json_file_path, excel_file_path)
