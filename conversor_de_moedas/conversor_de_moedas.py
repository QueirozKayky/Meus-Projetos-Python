import requests

resposta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

if resposta.status_code == 200:
    dados = resposta.json()
    
    valor_de_compra = float(dados['USDBRL']['bid'])
    valor_converter = float(input('Digite um valor para converter em Dolar: '))
    valor_convertido = valor_converter * valor_de_compra

    

    print(f'o Valor {valor_converter} convertido para dolar fica {valor_convertido}')
   

else:
    print(f"Erro ao obter dados. Código: {resposta.status_code}")

