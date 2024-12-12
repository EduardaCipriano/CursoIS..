import os
from is_wire.core import Channel, Subscription, Message
from is_msgs.image_pb2 import Image
import numpy as np
import cv2
import time

def to_np(input_image):
    """Converte o objeto Image do is_msgs para um array NumPy"""
    if isinstance(input_image, np.ndarray):
        return input_image
    elif isinstance(input_image, Image):
        buffer = np.frombuffer(input_image.data, dtype=np.uint8)
        return cv2.imdecode(buffer, flags=cv2.IMREAD_COLOR)
    return np.array([], dtype=np.uint8)

def save_image(image, save_path, image_format):
    """Salva a imagem em um arquivo com timestamp"""
    timestamp = int(time.time() * 1000)
    filename = f"image_{timestamp}.{image_format}"
    cv2.imwrite(os.path.join(save_path, filename), image)
    print(f"Image saved as {filename} in {save_path}")


# Configurações de variáveis via ConfigMap e valores padrão
ip = os.environ.get("IP")  # Endereço IP do RabbitMQ
topic = os.environ.get("TOPIC")  # Tópico para assinar
image_format = os.environ.get("IMAGE_FORMAT")  # Formato de imagem
save_path = "/data/images"  # Caminho de salvamento

print('--- Starting image receiver ---')

# Cria o diretório de salvamento se não existir
#if not os.path.exists(save_path):
 #   os.makedirs(save_path)

try:
    # Conexão com o RabbitMQ
    channel = Channel(f"amqp://guest:guest@{ip}")
    subscription = Subscription(channel)
    subscription.subscribe(topic=topic)
    print(f"Connected to RabbitMQ at {ip} and subscribed to topic '{topic}'")

    while True:
        try:
            # Consome a mensagem da fila
            msg = channel.consume(timeout=10.0)  # Timeout para evitar bloqueio infinito
            print("Message received")

            # Descompacta e processa a imagem
            im = msg.unpack(Image)
            frame = to_np(im)
            # Verifica se a imagem não está vazia
            if frame.size > 0:
                save_image(frame, save_path, image_format)
            else:
                print("Received empty frame, skipping save.")

        except Exception as e:
            print(f"Error processing message: {e}")

except Exception as e:
    print(f"Failed to connect to RabbitMQ: {e}")



