# is-wire
- [is-wire](https://github.com/labviros/is-wire-py)

## Publish

### Connect to the broker

Connect to the broker (ou "Conectar ao broker") é o processo de estabelecer uma conexão entre um cliente (dispositivo, serviço ou aplicação) e um broker, que é um intermediário responsável por gerenciar e distribuir mensagens em sistemas de comunicação. Esse conceito é amplamente utilizado em arquiteturas de mensageria, como o MQTT (Message Queuing Telemetry Transport), RabbitMQ, Kafka, entre outros.
O broker atua como o ponto central de um sistema de mensagens, facilitando a comunicação entre diferentes partes (publicadores e assinantes). Ele recebe mensagens de clientes que publicam dados (publishers) e as entrega para clientes que assinam tópicos específicos (subscribers). Além disso, ele pode oferecer funcionalidades como persistência, confiabilidade e ordenação na entrega das mensagens, dependendo da tecnologia utilizada.

```
channel = Channel("amqp://guest:guest@localhost:5672")
```
A variável channel inicializa uma conexão amqp no endereço da url passada e declara uma exchange("is") do tipo “topic”.

### Broadcast message to anyone interested (subscribed)

Broadcast message to anyone interested (subscribed), traduzido como "Transmitir mensagem para qualquer pessoa interessada (inscrita)", refere-se ao processo de envio de uma mensagem para todos os clientes ou sistemas que demonstraram interesse em recebê-la, geralmente por meio de inscrição (ou assinatura) em um tópico ou canal específico. Esse conceito é central em sistemas baseados na arquitetura publish/subscribe (publicação/assinatura), como MQTT, RabbitMQ ou Kafka.

```
channel.publish(message, topic="MyTopic.SubTopic")
```
O método “publish” irá publicar uma mensagem no tópico informado, ou seja, o mesmo se encarrega de de criar um “amqp.Message” e mandar a mensagem para a exchange "is" com a routing key informada.

## Sub

### Connect to the broker


Connect to the broker (ou "Conectar ao broker") é o processo de estabelecer uma conexão entre um cliente (dispositivo, serviço ou aplicação) e um broker, que é um intermediário responsável por gerenciar e distribuir mensagens em sistemas de comunicação. Esse conceito é amplamente utilizado em arquiteturas de mensageria, como o MQTT (Message Queuing Telemetry Transport), RabbitMQ, Kafka, entre outros.
O broker atua como o ponto central de um sistema de mensagens, facilitando a comunicação entre diferentes partes (publicadores e assinantes). Ele recebe mensagens de clientes que publicam dados (publishers) e as entrega para clientes que assinam tópicos específicos (subscribers). Além disso, ele pode oferecer funcionalidades como persistência, confiabilidade e ordenação na entrega das mensagens, dependendo da tecnologia utilizada.

```
channel = Channel("amqp://guest:guest@localhost:5672")
```

### Subscribe to the desired topic(s)

"subscribe to the desired topic(s)" é a ação de se inscrever em tópicos específicos em um sistema de mensagens para receber apenas as informações relevantes para o cliente. Essa abordagem é fundamental em arquiteturas publish/subscribe pela sua eficiência e organização.

```
subscription = Subscription(channel)
```
Resumidamente falando, o objeto “subscription” e inicializado com uma função que cria uma fila.
```
subscription.subscribe(topic="MyTopic.SubTopic")
```
Acima, no método "subscribe",  faz-se  o processo de bind da fila com a exchange "is". Desse modo, tudo que for publicado na exchange "is" no tópico “MyTopic.SubTopic”  será encaminhado para essa fila.

### Blocks forever waiting for one message from any subscription

blocks forever waiting for one message from any subscription" descreve o comportamento de um cliente que permanece em espera ativa, sem realizar outras ações, até que receba uma mensagem de um dos tópicos ou assinaturas de interesse. Esse padrão é útil em cenários onde mensagens são críticas para o próximo passo no fluxo de trabalho, mas requer cuidado para evitar bloqueios indesejados ou ineficiência.

```
message = channel.consume()
print(message)
```

## Run the exemple

### Executar um amqp broker localmente com o comando abaixo:
```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

### Executar o publish

```
from is_wire.core import Channel, Message

# Connect to the broker
channel = Channel("amqp://guest:guest@localhost:5672")

message = Message()
message.body = "Hello!".encode('latin1')

while True:
    # Broadcast message to anyone interested (subscribed)
    channel.publish(message, topic="MyTopic.SubTopic")
```

### Executar um sub para consumir as mensagens

```
from __future__ import print_function
from is_wire.core import Channel, Subscription
import time

# Connect to the broker
channel = Channel("amqp://guest:guest@localhost:5672")

# Subscribe to the desired topic(s)
subscription = Subscription(channel)
subscription.subscribe(topic="MyTopic.SubTopic")
# ... subscription.subscribe(topic="Other.Topic")

while True:
    message = channel.consume()
    print(message.body.decode('latin1'))
    time.sleep(1)
```
