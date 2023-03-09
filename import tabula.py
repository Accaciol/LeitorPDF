import tabula
import pandas as pd

# Especifique o caminho do arquivo PDF e as páginas que deseja extrair
pdf_file = r"C:\Users\Lucas\Desktop\backup HD antigo\3primeiros meses.pdf"
pages = "all"

# Extraia as tabelas das páginas especificadas usando a função "read_pdf" da biblioteca "tabula-py"
df_list = tabula.read_pdf(pdf_file, pages=pages, encoding='utf-8', multiple_tables=True)

# Separe as colunas utilizando o separador " - "
df = pd.concat(df_list)
df[['coluna1', 'coluna2']] = df['Coluna'].str.split(' - ', expand=True)

# Salve a tabela extraída em um arquivo do Excel usando a biblioteca pandas
excel_file = r"C:\Users\Lucas\Desktop\backup HD antigo\arquivo.xlsx"
df.to_excel(excel_file, index=False)

print(df) # Imprime o conteúdo do DataFrame
