1.Introdução

Este é o README do projeto de API web "Gestão de Carros", desenvolvido para a disciplina programação para web. A API é uma ferramenta para gerenciamento de informações de veículos, permitindo a inclusão de carros em um banco de dados com as informações de marca, modelo e ano do veículo.

2.Funcionalidades

● Adicionar Carros: Permite a inclusão de um novo carro no banco de dados, fornecendo informações de marca, modelo e ano.

● Editar Carros: Edita Informações de cadastro de um carro em uma lista no banco de dados.

● Exclui Carros: Permite a exclusão de um carro no banco de dados.

3.Requisitos

● Python 3.8+: Necessário para rodar a aplicação FastAPI.

● PostgreSQL: Banco de dados utilizado para armazenar as informações dos veículos.

● Visual Studio Code ou programa semelhante: Usado para construção do código.

4.Instalação e configuração do ambiente

•	Clone o repositório do projeto:
   
git clone https://github.com/Litlledark/Projeto_Carros
   

•	Crie um ambiente virtual e ative-o:

venv\Scripts\activate
   

•	Instale as dependências:

   	pip install -r requirements.txt
      
5. Inicie a aplicação:

   uvicorn main:app --reload
   

6.Endpoints

•	Adicionar Carro
   	Endpoint: `POST /carros/`
   	Descrição: Adiciona um novo carro ao banco de dados.
   
•	Listar Carros
   	Endpoint: `GET /carros/`
   	Descrição: Retorna a lista de todos os carros cadastrados.

•	Editar Carro
Endpoint: PUT /carros/
Descrição: Atualiza as informações de um carro específico.

•	Excluir Carro
Endpoint: DELETE /carros/
Descrição: Remove um carro específico do banco de dados.

7.Parâmetros

•	Adicionar Carro
   
   - Marca (string): Marca do carro.
   - Modelo (string): Modelo do carro.
   - Ano (int): Ano do carro.


● Teste de Adição de Carro: Verifica se um carro pode ser adicionado com sucesso ao banco de dados.

● Teste de Edição de Carro: Verifica se um Carro é adicionado ao banco de dados.

● Teste de Exclusão: Verifica se a consulta de um carro específico pelo ID retorna as informações corretas.

