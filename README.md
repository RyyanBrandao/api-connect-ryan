API Connect - MVP Back-end
1. Objetivo da API
A API Connect é um MVP (Minimum Viable Product) desenvolvido em arquitetura REST para o gerenciamento de usuários de uma startup. O sistema atua como o back-end responsável por processar requisições HTTP, aplicar validações de dados rigorosas e gerenciar o ciclo de vida dos registros de forma estruturada.

2. Tecnologias Utilizadas
Linguagem: Python 3.12+

Microframework: Flask (para o roteamento e gerenciamento de requisições HTTP)

Persistência: Em memória (RAM) estruturada via listas e dicionários para fins de MVP

Controle de Versão: Git e GitHub

3. Passo a Passo para Execução Local
Siga as instruções abaixo para clonar, configurar e executar a aplicação em seu ambiente de desenvolvimento local (Windows):

Clone o repositório:


git clone https://github.com/ryan/api-connect-ryan.git
cd api-connect-ryan
Crie e ative um ambiente virtual:


python -m venv venv
.\venv\Scripts\activate
Instale as dependências:


pip install flask
Execute a aplicação:


python main.py
O servidor estará acessível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

4. Documentação de Endpoints

| Método | Rota | Descrição | Status de Sucesso | Status de Erro |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/users` | Lista todos os usuários cadastrados no sistema. | `200 OK` | - |
| **POST** | `/users` | Cadastra um novo usuário (exige `nome` e `email` no corpo JSON). | `201 Created` | `400 Bad Request` |
| **GET** | `/users/<id>` | Retorna os dados de um usuário específico buscando pelo ID. | `200 OK` | `404 Not Found` |
