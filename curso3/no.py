from is_msgs.camera_pb2 import CameraSettings
from is_msgs.camera_pb2 import CameraSetting

brightness = CameraSetting()
saturation = CameraSetting()
zoom = CameraSetting()

brightness.automatic = False
saturation.automatic = False
zoom.automatic = False

brightness.ratio = 0.2
saturation.ratio = 0.7
zoom.ratio = 0.8

camera = CameraSettings(
    brightness=brightness,
    saturation=saturation,
    zoom=zoom
    )

print(camera)
print(camera.brightness)
print(camera.saturation.automatic)
