# Constraints ou Restrições

!!! warning
    Lembrando que o protocolo é livre para ser utilizado da forma que melhor lhe atender. Porém, seguindo essas constraints, você irá aproveitar melhor a arquitetura

## Cliente / Servidor

Separação de responsabilidade é uma tecnicas mais utilizadas em desenvolvimento. E separando cliente de servidor, você consegue definir sua regra de negócio e sua camada de apresentação mais simples e com focos em suas atividades (servidor se preocupa com banco de dados, validações de regras, rotas e etc. Já o cliente se preocupa com apresentação, validação de entrada, apresentação de erros e etc).

Com isso podemos até hospedar e desenvolver as camadas separadamente. Isso gera uma flexibilidade de escalabilidade de aplicação e uma facilidade de manutenção.

## Stateless (sem estado)

Leva em consideração que cada requisição como uma transação independente que não está relacionada a qualquer requisição anterior, de forma que a comunicação consista de pares de requisição e resposta independentes.

Geralmente o proprio cliente inclui a informação de estado da requisição para que ele seja enviada ao servidor.

## Cache

Algumas informações podem ser cacheadas para ganhar velocidade na resolução das requisições. (Isso pode facilitar, porém, pode atrapalhar)

## Interface uniforme

Define como cliente e servidor irão se comunicar, padronizando a entrada e saida de informações. Exemplo:

Uma aplicação de vendas, precisa fazer um cadastro de clientes. Então, sabemos que nessa RESTFul vai rodar um contrato (cliente) e nele vão ser necessários as informações de código, nome, razão social, cnpj e etc. Também é sabido que será necessário listar, adicionar, editar e apagar clientes.

Isso cria uma interface, onde o cliente e o servidor precisam cumprir essas regras, deixando-a uniforme para ambos os lados.

## Sistemas em camada

Um cliente, podera se conectar a vários servidores. Seguindo nosso exemplo de clientes, podemos acessar nossa camada do cliente para salvar as informações, porém, antes disso, podemos acessar uma outra camada para efetuar validação do cnpj, por exemplo, no site da receita.