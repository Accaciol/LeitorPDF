import pandas as pd

# dados fornecidos
dados = "15/02/2023	TEF CREDITO SALARIO	1.779,36	Unnamed: 0	14/02/2023	SEGURO CARTAO	-7,90	13/02/2023	INT PRE-PAGOXXXXX 0601	-60,00	10/02/2023	DA NET SERVICOS 0112572	-235,15	REND PAGO APLIC AUT MAIS	0,04	08/02/2023	0,03	SALDO DO DIA	645,91	06/02/2023	859,88	02/02/2023	0,01	31/01/2023	TBI 1595.03627-6/500	-2.807,36	999,95	30/01/2023	1.472,09	26/01/2023	24/01/2023	INT PAG TIT BANCO 237	-1.344,96	23/01/2023	2.817,04	18/01/2023	2.897,04	17/01/2023	INT MULTIPLO MC	-102,97	PIX TRANSF Lucas A17/01	15.000,00	16/01/2023	4.916,44	PIX TRANSF Lucas A16/01	4.424,34	13/01/2023	1.629,00	12/01/2023	330,53	11/01/2023	PIX QRS DEMERGE11/01	-79,99	PIX TRANSF LUCINET11/01	200,00	10/01/2023	270,52	09/01/2023	PIX QRS Alipay/AliE08/01	-64,23	05/01/2023	569,90"

# separar as informações em linhas distintas
dados = dados.split("\t")

# criar um dicionário para armazenar os dados em colunas
dic = {
    "Data": [],
    "Descricao": [],
    "Valor": []
}

# loop para preencher o dicionário com as informações
for i, d in enumerate(dados):
    if i % 4 == 0:
        dic["Data"].append(d)
    elif i % 4 == 1:
        dic["Descricao"].append(d)
    elif i % 4 == 2:
        if d.isnumeric():
            dic["Valor"].append(float(d.replace(".", "").replace(",", ".")))
        
# criar um dataframe a partir do dicionário
df = pd.DataFrame(dic)

# ordenar o dataframe por data
df["Data"] = pd.to_datetime(df["Data"], format="%
