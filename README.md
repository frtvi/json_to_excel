# JSON to Excel Converter

![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green)

Este projeto transforma arquivos JSON em planilhas Excel (.xlsx), facilitando o manuseio de dados estruturados em um formato amplamente usado.

## 🚀 Recursos
- Converte JSON diretamente para Excel
- Suporte a grandes volumes de dados com a biblioteca `pandas`

## 🛠️ Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/frtvi/json_to_excel.git
   cd json_to_excel
   ```
Instale as dependências:
   ```bash
   pip install pandas openpyxl
   ```
## ⚙️ Uso
Coloque o caminho do seu JSON nessa linha:.<br>
   ```bash
   json_file_path = 'C:/Users/random/data.json'  # ONDE ESTÁ O JSON
   ```
Depois, coloque o caminho onde deseja salvar o xlsx:
   ```bash
   excel_file_path = 'C:/Users/random/data.xlsx'  # ONDE DESEJA SALVAR O EXCEL
   ```
## 📈 Exemplo
Suponha que você tenha um arquivo data.json com o conteúdo:
```[
  {"nome": "Alice", "idade": 25},
  {"nome": "Bob", "idade": 30}
]
```
O script irá gerar um arquivo data.xlsx com o conteúdo estruturado em uma tabela.

## 🎉 Contribua
Sugestões e melhorias são bem-vindas!
