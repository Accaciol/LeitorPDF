import PyPDF2

# Especifique o caminho do arquivo PDF de entrada e do arquivo de texto de saída
pdf_file = r"C:\Users\Lucas\Desktop\backup HD antigo\3primeiros meses.pdf"
txt_file = r"C:\Users\Lucas\Desktop\backup HD antigo\arquivoTxt.xlsx"

# Abra o arquivo PDF em modo leitura binária
with open(pdf_file, 'rb') as pdf:
    # Crie um objeto de leitura do PDF
    pdf_reader = PyPDF2.PdfReader(pdf)
    # Crie uma string vazia para armazenar o conteúdo do arquivo de texto
    content = ""
    # Itere sobre as páginas do PDF
    for page in range(len(pdf_reader.pages)):
        # Obtenha o texto da página
        page_text = pdf_reader.pages[page].extract_text()
        # Adicione o texto da página à string de conteúdo
        content += page_text
    # Salve o conteúdo em um arquivo de texto
    with open(txt_file, 'w', encoding='utf-8') as txt:
        txt.write(content)
