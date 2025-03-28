#Gerador_OS

##Objetivo

Automatizar a criação de ordens de serviço em formato PDF, facilitando a organização e documentação dos serviços prestados aos clientes.

##Descrição

O Gerador_OS é uma aplicação desenvolvida em Python que gera ordens de serviço de forma prática e profissional. O projeto utiliza a biblioteca pylatex para compor documentos LaTeX que, posteriormente, são convertidos em arquivos PDF. A interface gráfica, construída com tkinter, permite a entrada de dados como informações do cliente, detalhes do veículo e serviços realizados, integrando-se a um banco de dados MySQL para armazenamento e recuperação de informações.

##Tecnologias Utilizadas

Python: Linguagem principal para o desenvolvimento do projeto.

pylatex: Biblioteca utilizada para a geração de documentos LaTeX e criação dos PDFs.

LaTeX: Sistema de preparação de documentos utilizado para formatar a ordem de serviço.

MySQL: Banco de dados utilizado para armazenar informações dos clientes, veículos e serviços.

tkinter: Biblioteca para a criação da interface gráfica do usuário (GUI).


##Como Usar

1. Clone o repositório:

'git clone https://github.com/Joao-Pedro-m/Gerador_OS.git'


2. Instale as dependências: Certifique-se de ter o Python instalado e, em seguida, instale as dependências necessárias com:

'pip install -r requirements.txt'

> Caso o arquivo requirements.txt não esteja presente, verifique na documentação quais bibliotecas precisam ser instaladas (como pylatex, tkinter e o conector MySQL para Python).




3. Configure o banco de dados MySQL:

Atualize as configurações de conexão com o banco de dados diretamente no código ou em um arquivo de configuração, conforme a estrutura do projeto.

Certifique-se de que o banco de dados está ativo e acessível.



4. Execute a interface gráfica: Inicie a aplicação executando:

'python interface.py'

A interface permitirá inserir os dados do cliente, do veículo e dos serviços realizados.


5. Geração da Ordem de Serviço: Após preencher os dados e confirmar a ação, o sistema gerará automaticamente um documento PDF com a ordem de serviço, utilizando a função definida no gerador_os.py.



##Contribuição

Contribuições são bem-vindas! Caso deseje colaborar, siga os passos abaixo:

Faça um fork deste repositório.

Crie uma branch com a sua feature: git checkout -b minha-feature

Commit suas alterações: git commit -m 'Minha nova feature'

Envie para a branch: git push origin minha-feature

Abra um Pull Request detalhando as alterações realizadas.


##Licença

Este projeto está licenciado sob a MIT License.
