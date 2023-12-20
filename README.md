# Locadora_VHS

## Titulo do projeto

- Sistema de locação de filmes VHS online.

Autores:

- Cauê Trajano
- Douglas Carneiro
- Lauro Stephan

Projeto de um aplicativo Server/Clients para as disciplinas:

- Estrutura de dados - Professor Gustavo Wagner
- Sistemas operacionais - Professor Alex
- Protocolos de interconexão de redes - Professor Leonidas

## Detalhes da aplicação

Se trata de uma locadora de fitas VHS....
Para rodar o projeto você pode ir ao diretório pelo terminal e rodar o
server.py, e em seguida em outro terminal rodar o client.py
No menu inicial do client temos as seguintes opções:

- Digite `catalogo` para visualizar todas as fitas disponíveis ou não
- Digite `alugar` para poder digitar o nome do filme que voce deseja alugar
- Digite `histórico` para poder visualizar o histórico de aluguéis do usuário
- Um filme só pode ser alugado caso esteja disponível no catalogo
- Digite s ou sair para encerrar o client
- Ao acessar o catalogo voce pode digitar v para voltar ao menu inicial
- Para encerrar o Server.py basta pressionar ctrl + break

## Arquivos do projeto

- filmes.json: contém um json com uma lista inicial de filmes do catálogo
- catalogo.py é responsável por administrar a arvore binaria e a comunicação do server com os filmes na arvore, e também é ele quem monta a arvore no inicio do programa
- filme.py é o objeto filme que é instanciado e armazenado na arvore
- BinarySearchTree.py é o arquivo da arvore, criamos alguns métodos adicionais nela, mas focando na reutilizabilidade dela em outros projetos, sem prender a arvore a este projeto.
- server.py é o arquivo servidor que recebe clientes e cria uma nova thread para cada novo cliente
- client.py é o arquivo onde o cliente pode acessar o programa e alugar uma fita caso disponível
- historico.py é responsável por administrar o histórico de aluguéis de cada usuário
- env.py é responsável por armazenar e servir ao client.py e servidor.py as constantes de endereço de IP do servidor e PORTA

## Pré-requisitos para execução

- informar os pacotes/bibliotecas que precisam ser instalados, o propósito de cada um deles e como instalá-los antes de executar o código

## Informações de conexão

Utilizamos o protocolo TCP para a comunicação cliente/servidor

## Protocolo de Aplicação

- "902" > "Filme alugado com sucesso!"
- "904" > "Este filme não está disponível para locação"
- "906" > "Filme não encontrado... tente novamente"
- "908" > "Filme devolvido com sucesso"
- "909" > "Erro ao carregar o catálogo"
- "910" > "Não foi possível devolver o filme"


## Detalhes sobre região crítica

primeiro vamos fazer as funções rodarem...
...
