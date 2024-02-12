# Gerador de Tag Código de Barras

Este é um projeto Flask que cria tags de código de barrras em formato de imagem
utilizando o módulo `barcode`. O projeto possui uma estrutura organizada para lidar com solicitações HTTP, validação de dados, tratamento de erros e testes unitários.

## Estrutura do projeto

- `src/`: Contém o código-fonte do projeto.
  - `controllers/`: Controladores responsáveis pela lógica de negócio.
  - `drivers/`: Classes para interação com drives externos, como o `barcode`, para geração de códigos de barras.
  - `main/`: Criação das rotas e servidor.
  - `errors/`: Definições de tipos de erro e tratamento de erros.
  - `validators/`: Validadores para validar os dados de entrada.
  - `views/`: Classes para interagir com solicitações HTTP.
  