# logs

Logs são ferramentas essenciais para compreender o comportamento de sistemas e aplicações, ajudando a manter a confiabilidade, a segurança e o desempenho. Eles são uma peça-chave na administração de sistemas modernos.

O [log](https://www.youtube.com/watch?v=tZ2iJ5H99fg&t=2641s&ab_channel=EduardoMendes) é um meio de rastrear eventos que acontecem quando algum software é executado. Eles fornecem uma explicação simples de algum evento no sistema separando em níveis diferentes certos tipos de mensagens.

Os [logs no espaço inteligente](https://github.com/labviros/is-wire-py/blob/master/src/is_wire/core/logger.py) são configurados através da classe Logger (from is_wire.core import Logger). 

## Logger

Logger é um componente ou ferramenta utilizada em sistemas e aplicações para criar, formatar e gerenciar logs. Ele é responsável por registrar informações sobre o comportamento de um programa, como mensagens de erro, eventos importantes, status de execução e outros dados úteis para monitoramento, depuração e análise de desempenho.

O Logger faz parte do processo de logging e é frequentemente integrado em frameworks e bibliotecas de desenvolvimento para facilitar o registro e a organização das mensagens de log.

```
from is_wire.core import Logger

log = Logger(name = "Teste")

log.debug("Um debug")

log.info("olá :)")

log.warn("cuidado")

log.error("Ops")

#### Esse Logger encerra o programa

log.critical("erro crítico")

print("Não será exibido")
```

![Resultado](https://github.com/matheusdutra0207/logs/blob/main/M%C3%ADdia/log1.JPG "result")

# Status

Status refere-se ao estado atual de algo em um determinado momento. Ele é utilizado para descrever a condição, o funcionamento ou a situação de um sistema, processo, objeto, dispositivo, ou qualquer outro elemento que pode ser monitorado ou avaliado. O status é geralmente representado por uma informação objetiva que ajuda a entender o comportamento ou desempenho de algo, sendo fundamental em diversas áreas, como tecnologia, negócios, saúde, e administração.

[Status suportados pelo IS](https://github.com/labviros/is-wire-py/blob/master/src/is_wire/core/wire/status.py)

## Exemplo de aplicação de Status em uma função

```
from is_wire.core import StatusCode, Status
from google.protobuf.struct_pb2 import Struct
from is_wire.core import Logger

log = Logger(name = "root")

def increment(struct):
    if struct.fields["value"].number_value < 0:
        return Status(StatusCode.INVALID_ARGUMENT, "Number must be positive")

    struct.fields["value"].number_value += 1.0
    return struct

#Observem os resultados 
struct_1 = Struct()
struct_2 = Struct()

struct_1.fields["value"].number_value = 1.0
struct_2.fields["value"].number_value = -1.0


print(increment(struct_1))
print(increment(struct_1).fields["value"].number_value)


print(increment(struct_2))
print(increment(struct_2).code)

```
