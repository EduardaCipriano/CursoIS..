# Docker

## O que são containers?

Containers são unidades leves e portáteis de software que empacotam uma aplicação e todas as suas dependências, bibliotecas e configurações necessárias para sua execução, tornando-a independente do ambiente em que é executada. Isso permite que a aplicação seja executada de maneira consistente em diferentes sistemas, seja no ambiente de desenvolvimento, produção ou em servidores na nuvem.

Containers são executados sobre um sistema operacional comum, mas utilizam tecnologias como o **Docker** (um dos mais populares) ou **Kubernetes** para gerenciar e orquestrar múltiplos containers. Eles são mais eficientes do que máquinas virtuais, pois não exigem um sistema operacional completo para cada instância, o que reduz o consumo de recursos.

A principal vantagem dos containers é a sua capacidade de **isolamento**, ou seja, cada container opera de forma independente, sem afetar o desempenho ou funcionamento dos outros containers. Isso torna os containers ideais para desenvolvimento, testes, implementação e escalabilidade de aplicações.

## O que são imagens Docker ?

Uma **imagem Docker** é um arquivo de leitura apenas (somente leitura) que contém tudo o que uma aplicação precisa para ser executada em um container. Isso inclui:

- **O sistema operacional base** (como uma versão do Linux ou uma versão minimalista do Linux)
- **Bibliotecas** e **dependências** necessárias
- **Códigos** da aplicação
- **Arquivos de configuração**

As imagens Docker são criadas a partir de um **Dockerfile**, que é um arquivo de texto que contém uma série de instruções que definem como a imagem será construída. Cada linha no Dockerfile especifica uma operação a ser realizada, como instalar pacotes, copiar arquivos ou expor portas de rede.

Uma imagem Docker é a base de um container. Quando você executa um container a partir de uma imagem, o Docker cria uma instância dessa imagem e a coloca em execução. O container é um ambiente isolado onde a aplicação funciona, e pode ser iniciado, pausado ou removido, mas a imagem em si permanece inalterada.

### Características das imagens Docker:
- **Imutabilidade**: As imagens são imutáveis. Uma vez criadas, elas não podem ser alteradas, mas podem ser versionadas e novas imagens podem ser criadas a partir de versões anteriores.
- **Portabilidade**: Como elas contêm todas as dependências necessárias, podem ser executadas em qualquer ambiente Docker compatível, seja localmente ou em nuvens.
- **Camadas**: As imagens são compostas por camadas, onde cada instrução no Dockerfile cria uma camada. Essas camadas são reutilizáveis, o que torna o processo de criação de imagens mais eficiente.

Em resumo, as **imagens Docker** são a "fórmula" ou "modelo" de um container e garantem que a aplicação seja executada de maneira consistente em qualquer ambiente.

## Construção de uma imagem

Depois de criar o Dockerfile, você pode construir a imagem Docker usando o comando docker build. Este comando precisa ser executado no diretório onde o Dockerfile está localizado.

### Image

- Requirements: flask==2.0.1

- Dockerfile:

```
FROM python:3.7-alpine
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

```
- Build the image:

```
docker build --tag=flaskboasvindas .
```
### Containers
- Run the Container

```  
sudo docker run -it --rm --name flaskboasvindasContainer -p 8080:8000 flaskboasvindas python3 serverFlask.py
```

