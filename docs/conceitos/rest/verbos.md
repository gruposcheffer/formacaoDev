# Verbos

O protocolo HTTP define métodos (às vezes referidos como verbos) para indicar a ação desejada a ser realizada no recurso identificado. O que este recurso representa, se são dados pré-existentes ou dados gerados dinamicamente, depende da implementação do servidor. Muitas vezes, o recurso corresponde a um arquivo ou a saída de um executável residente no servidor. (fonte Wikipedia)
Em resumo, os verbos HTTP são os métodos de requisição que utilizamos para acessar os endpoints de uma RESTful API.


## POST

O verbo POST é mais frequentemente utilizado para criar novos recursos. Na criação bem-sucedida, retornar o status HTTP 201.

Ele não é um método seguro, pois altera o estado do recurso no servidor. Ele também não é idempotente, o que quer dizer que se ele for executado duas vezes de forma idêntica serão criados dois itens diferentes com o mesmo conjunto de dados.

## GET

O método HTTP GET é usado para ler ou recuperar uma representação de um recurso. Em caso de sucesso, retorna uma representação em JSON e um código de resposta HTTP de 200 (OK). Em caso de erro, ele geralmente retorna um 404 (NOT FOUND) ou 400 (BAD REQUEST).

De acordo com o design da especificação HTTP, requisições GET (juntamente com HEAD) são usadas apenas para ler dados e jamais alterá-los. Portanto, quando usados dessa forma, são considerados seguros.

Além disso, GET (e HEAD) é idempotente, o que significa que fazer várias solicitações idênticas acaba tendo o mesmo resultado de uma única solicitação.

## PUT

PUT é mais utilizado para substituir (ou atualizar) recursos, executando a requisição para uma URI de recurso conhecido, com o corpo da requisição contendo a representação recém-atualizada do recurso original.

Na atualização bem-sucedida, retorna 200 (ou 204 se não retornar qualquer conteúdo no corpo). Retornar os dados do recurso no corpo é opcional, lembrando que fazer isso causa maior consumo de banda.

PUT não é uma operação segura, pois modifica estado no servidor, mas é idempotente. Em outras palavras, se você atualizar um recurso usando PUT e, em seguida, fazer essa mesma chamada novamente, o recurso ainda está lá e ainda tem o mesmo estado.

Obs: Se, por exemplo, executar uma requisição PUT em um recurso incrementar um contador (dentro do recurso), a chamada não é mais idempotente. É recomendado manter as solicitações PUT idempotentes. Use o POST para solicitações não idempotentes.

## PATCH

PATCH é usado para modificar parcialmente os recursos. A requisição só precisa conter as alterações específicas para o recurso, não o recurso completo.

Se parece com PUT, mas o corpo contém um conjunto de instruções descrevendo como um recurso no servidor deve ser modificado para produzir uma nova versão.

PATCH não é nem seguro, nem idempotente.

## DELETE

DELETE é bastante fácil de entender. Ele é usado para excluir um recurso identificado por um URI.

Na exclusão bem-sucedida, devolve o status HTTP 200 (OK) ou o status HTTP 204 (NO CONTENT) sem corpo de resposta.

Operações DELETE são idempotentes.

Há uma advertência sobre idempotência no DELETE. Chamar DELETE em um recurso uma segunda vez geralmente retornará um 404 (NOT FOUND) já que ele já foi removido e, portanto, não é mais encontrável. Isso, por algumas opiniões, faz operações DELETE não mais idempotente, no entanto, o estado final do recurso é o mesmo. Retornar um 404 é aceitável e comunica com precisão o status da chamada.

Obs: Se a requisição DELETE decrementa um contador (dentro do recurso), a chamada DELETE não é mais idempotente. É recomendável usar o POST para solicitações de recursos não idempotentes.