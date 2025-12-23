# Aplicativo de Notas Simples (File I/O) em Python

Este projeto é um aplicativo de notas que roda no terminal e tem como foco principal o aprendizado da **persistência de dados**. O programa salva as notas em um arquivo (`notas.txt`), permitindo que as informações sejam mantidas mesmo após o programa ser fechado.

## Funcionalidades

- **[1] Escrever Nota:** Adiciona uma nova nota ao arquivo (`notas.txt`) sem apagar as notas existentes.
- **[2] Ver Notas:** Lê e exibe todas as notas salvas no arquivo.
- **[3] Deletar Notas:** Permite ao usuário escolher e remover uma nota específica, reescrevendo o arquivo com o conteúdo restante.
- **[4] Sair:** Encerra o programa.

## Conceitos Avançados Praticados

- **File I/O (Entrada/Saída de Arquivos):** Uso dos modos de leitura (`'r'`), adição (`'a'`) e escrita (`'w'`).
- **Segurança de Arquivos:** Uso do `with open()` para garantir que os arquivos sejam fechados automaticamente, mesmo em caso de erro.
- **Algoritmo de Exclusão (Overwrite):** Implementação da lógica de ler o arquivo, deletar o item em uma lista (na memória) e **reescrever o arquivo do zero** com o novo conteúdo.
- **Tratamento de Erros:** Uso de `try-except` para lidar com erros de arquivo (`FileNotFoundError`) e entradas inválidas.

## Como Executar

1.  Certifique-se de ter o Python instalado.
2.  Execute o script com o seguinte comando no terminal:
    ```bash
    python seu_arquivo_de_notas.py
    ```
