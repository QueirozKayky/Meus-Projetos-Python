# Conversor de Moedas por Linha de Comando em Python

Este projeto é um conversor de moedas interativo que utiliza uma API online para obter taxas de câmbio em tempo real. O objetivo foi praticar a comunicação do código com a internet, um passo fundamental para a criação de aplicações mais complexas.

## Funcionalidades

- Converte um valor de uma moeda para outra usando taxas de câmbio ao vivo.
- Interage com uma API externa para buscar dados.
- Exibe o resultado da conversão de forma clara e formatada.
- Garante que o programa só funcione se houver uma conexão bem-sucedida com a API.

## Como Executar

1.  Certifique-se de ter o Python instalado.
2.  Instale a biblioteca `requests` no terminal com o seguinte comando:
    ```bash
    pip install requests
    ```
3.  Navegue até a pasta do projeto no seu terminal.
4.  Execute o script com o comando:
    ```bash
    python seu_conversor.py
    ```

## Conceitos Avançados Aprendidos

- **Requisições HTTP (`requests`):** Usar a biblioteca `requests` para enviar um pedido de dados a um servidor web.
- **API e JSON:** Entender o que é uma API e como processar dados em formato JSON, transformando-os em um dicionário Python.
- **Tratamento de Conexão:** Verificar o `status_code` de uma resposta para garantir que a conexão foi bem-sucedida antes de manipular os dados.
