# Car Marketplace

## Descrição
Aplicação web para registrar entrada de carros.

## Tecnologias
- Python
- FastAPI
- PostgreSQL
- HTML
- CSS

## Instalação

1. Clone o repositório:

    git clone https://github.com/Litlledark/Projeto_Carros
  

2. Crie e ative um ambiente virtual:
    
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    

3. Instale as dependências:
    
    pip install -r requirements.txt
    

4. Execute a aplicação:

    uvicorn main:app --reload


5. Acesse `http://127.0.0.1:8000` no seu navegador.]

## Funcionalidades

1. Registro de Usuário: Os usuários podem se registrar fornecendo um nome de usuário e senha. 

2. Login de Usuário: Os usuários podem fazer login com seu nome de usuário e senha. Se as credenciais forem válidas, eles são redirecionados para a página inicial, onde podem ver os carros disponíveis.

3. Visualização de Carros Disponíveis: Os carros disponíveis são exibidos na página inicial após o login do usuário. Cada carro exibido inclui a marca, modelo, ano e preço.

4. Registro de Novo Carro: Os usuários podem registrar um novo carro fornecendo detalhes como marca, modelo, ano e preço. Após o registro, o novo carro é adicionado à lista de carros disponíveis e exibido na página inicial.

5. Detalhes do Carro: Os usuários podem clicar em um carro na página inicial para ver os detalhes completos desse carro, incluindo sua marca, modelo, ano e preço.
