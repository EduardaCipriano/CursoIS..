from is_wire.core import Channel, Subscription, Message
from is_msgs.image_pb2 import Image
import numpy as np
import cv2
import json
import time


def to_np(input_image):
    if isinstance(input_image, np.ndarray):
        output_image = input_image
    elif isinstance(input_image, Image):
        buffer = np.frombuffer(input_image.data, dtype=np.uint8)
        output_image = cv2.imdecode(buffer, flags=cv2.IMREAD_COLOR)
    else:
        output_image = np.array([], dtype=np.uint8)
    return output_image

if __name__ == '__main__':
    print('--- Saving the image ---')
    
    channel = Channel("amqp://guest:guest@10.10.0.91:5672")
    subscription = Subscription(channel)
    subscription.subscribe(topic='Frame.Joab')


    msg = channel.consume()
    img_unpack = msg.unpack(Image)
    imgNP = to_np(img_unpack)

    filename = 'image_rcvd.jpeg'
    file_path= f'./img_RCV/{filename}'


    cv2.imwrite(file_path, imgNP)
    print('Image saved')
      
