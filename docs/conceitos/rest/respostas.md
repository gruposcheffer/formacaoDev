# Os códigos de resposta (status codes) HTTP

Nas descrições dos verbos HTTP foram citados diversas vezes os status code do protocolo HTTP.

Esse é outro item importante para a arquitetura de uma API REST, porque, da mesma maneira que acontece como os verbos HTTP, elas formam um padrão facilmente reconhecido por quem for consumir o web service.

Os principais códigos utilizados para as respostas de um endpoint são o 200 (OK), o 201 (CREATED), o 204 (NO CONTENT), o 404 (NOT FOUND) e o 400 (BAD REQUEST).

Todos os códigos tem nomes autoexplicativos, portanto é muito simples lembrar o que utilizar em cada situação.

Existe uma lista enorme de códigos de resposta do protocolo HTTP que podem ser utilizados, como o 301 (MOVED PERMANETLY) e o 304 (NOT MODIFIED). Sendo o segundo para conteúdos em cache, por exemplo.

Os códigos de sucesso tem o padrão 20x, os de redirecionamento 30x, os de erro do cliente 40x e os de erro de servidor 50x.

Lembrando mais uma vez, os padrões facilitam qualquer desenvolvedor de entender facilmente o que aconteceu com o retorno da requisição que ele executou.

No caso de erros, mesmo tendo esses padrões, é importante devolver ao cliente uma mensagem clara do que aconteceu com a requisição e qual o motivo do erro.

Para ver mais detalhes sobre os códigos HTTP e também a lista completa deles, acesse o link https://httpstatuses.com/.

<div markdown="1" class="three-column">

| Código | Description |
|---|---|
| 1×× | Informational| 
| 100 | Continue| 
| 101 | Switching Protocols| 
| 102 | Processing| 

</div>

<div markdown="1" class="three-column">

| Código | Description |
|---|---|
| 2×× | Success| 
| 200 | OK| 
| 201 | Created| 
| 202 | Accepted| 
| 203 | Non-authoritative Information| 
| 204 | No Content| 
| 205 | Reset Content| 
| 206 | Partial Content| 
| 207 | Multi-Status| 
| 208 | Already Reported| 
| 226 | IM Used| 

</div>

<div markdown="1" class="three-column">

| Código | Description |
|---|---|
| 3×× | Redirection| 
| 300 | Multiple Choices| 
| 301 | Moved Permanently| 
| 302 | Found| 
| 303 | See Other| 
| 304 | Not Modified| 
| 305 | Use Proxy| 
| 307 | Temporary Redirect| 
| 308 | Permanent Redirect| 

</div>

<div markdown="1" class="two-column">

| Código | Description |
|---|---|
| 4×× | Client Error| 
| 400 | Bad Request| 
| 401 | Unauthorized| 
| 402 | Payment Required| 
| 403 | Forbidden| 
| 404 | Not Found| 
| 405 | Method Not Allowed| 
| 406 | Not Acceptable| 
| 407 | Proxy Authentication Required| 
| 408 | Request Timeout| 
| 409 | Conflict| 
| 410 | Gone| 
| 411 | Length Required| 
| 412 | Precondition Failed| 
| 413 | Payload Too Large| 
| 414 | Request-URI Too Long| 
| 415 | Unsupported Media Type| 
| 416 | Requested Range Not Satisfiable| 
| 417 | Expectation Failed| 
| 418 | I'm a teapot| 
| 421 | Misdirected Request| 
| 422 | Unprocessable Entity| 
| 423 | Locked| 
| 424 | Failed Dependency| 
| 426 | Upgrade Required| 
| 428 | Precondition Required| 
| 429 | Too Many Requests| 
| 431 | Request Header Fields Too Large| 
| 444 | Connection Closed Without Response| 
| 451 | Unavailable For Legal Reasons| 
| 499 | Client Closed Request| 

</div>

<div markdown="1" class="two-column">

| Código | Description |
|---|---|
| 5×× | Server Error| 
| 500 | Internal Server Error| 
| 501 | Not Implemented| 
| 502 | Bad Gateway| 
| 503 | Service Unavailable| 
| 504 | Gateway Timeout| 
| 505 | HTTP Version Not Supported| 
| 506 | Variant Also Negotiates| 
| 507 | Insufficient Storage| 
| 508 | Loop Detected| 
| 510 | Not Extended| 
| 511 | Network Authentication Required| 
| 599 | Network Connect Timeout Error|

</div>