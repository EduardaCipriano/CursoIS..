# is-wire 

## Basic Request/Reply

### Create a RPC Server

"Create a RPC Server", ou "Criar um Servidor RPC", refere-se ao processo de configurar um servidor que utiliza o modelo de comunicação Remote Procedure Call (RPC). Esse modelo permite que clientes executem funções ou procedimentos remotamente, como se estivessem sendo chamados localmente.

O servidor RPC é responsável por expor essas funções ou métodos, processar as chamadas recebidas e retornar os resultados aos clientes.

O rpc server terá um método chamado "delegate" que  faz um bind de uma função para um particular topic, para que toda vez que um mensagem é
recebida neste topic a função vai ser chamada.

## Run the example

### Executar um amqp broker localmente com o comando abaixo:

```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

### Executar o RPC server, no qual encontra-se nos arquivos anexados no Curso 4.

```
python3 rpc_server_controle_robot.py
```
Pronto, agora só mandar requests para o rpc. Os exemplos de request encontram-se também no curso 4 .

### Get position

```
python3 get_position.py
```

### Set position

```
python3 set_position.py <position x> <position y>
```
