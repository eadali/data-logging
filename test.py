# from data_logging import SignalLogger
from data_logging import RingBufferManager
import numpy as np
import cv2
from datetime import datetime
from matplotlib import pyplot as plt

frame_shape = (480, 640, 3)
frame_dtype = np.uint8
pre_buffer_size = 8
post_buffer_size = 4

# logger = SignalLogger(frame_shape, frame_dtype,
#                     pre_buffer_size, post_buffer_size)

manager = RingBufferManager(4, 3, frame_shape, frame_dtype)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3
font_color = (255,255,255)
font_thickness = 5
text_position = (50, 200)

for i in range(1000):
    timestamp = np.datetime64(datetime.now())
    frame = np.zeros(frame_shape, dtype=frame_dtype)
    cv2.putText(frame, str(i), text_position, 
                font, font_scale, font_color, font_thickness)
    manager.put(frame)

manager.next_buffer()
arr = manager.get(-1)
print(type(arr))
print(arr.shape)
plt.imshow(arr[0])
plt.savefig('test')




