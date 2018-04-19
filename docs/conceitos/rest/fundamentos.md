# Fundamentos

## Tudo é um recurso

Para entender esse princípio, é preciso conceber a idéia de representar dados por um formato específico e não por um arquivo físico. 

Cada dado disponível na Internet possui um formato que poderia ser descrito por um tipo de conteúdo.

Por exemplo, imagens JPEG, Vídeos MPEG, HTML, XML, documentos de texto, e dados binários são todos os recursos com o seguinte conteúdo : imagem / jpeg, video / mpeg, texto/html, texto/xml e stream.

## Cada recurso é identificável por um único identificador

Como a Internet contém tantos recursos diferentes, todos eles devem ser acessíveis através de URIs e devem ser identificados de forma exclusiva. Além disso, as URIs podem ser legíveis por humanos, apesar do fato de que seus consumidores são mais propensos a ser programas de software.

As URI legíveis por humanos mantêm os dados auto-descritivos e facilitam o desenvolvimento e isso ajuda você a reduzir ao mínimo o risco de erros lógicos em seus programas.

A seguir temos alguns exemplos de exemplos de URIs:

http://www.macoratti.net/teste.jpg

http://microsoft.com/data/video.mp3

http://www.uol.com.br/futebol.xml

http://mediafire.com/WaO4OcaWwATIzL-gDg

Essas URIs expõem diferentes tipos de recursos de forma direta.

No exemplo, é bastante claro que os tipos de mídia desses recursos são : imagens, videos, documentos XML e, de documentos de arquivos binários.

## Utiliza os métodos HTTP padrão

O protocolo HTTP (RFC 2616) define oito ações também conhecidos como verbos HTTP:  GET, POST,  PUT,  DELETE, HEAD, OPTIONS, TRACE e CONNECT.

Os quatro primeiros (GET, POST, PUT e DELETE) atuam no contexto dos recursos, especialmente ao definir ações para manipulação de dados de recursos.
