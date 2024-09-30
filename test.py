from data_logging import DataLogger
import numpy as np
import cv2
from datetime import datetime

frame_shape = (480, 640, 3)
frame_dtype = np.uint8
pre_buffer_size = 8
post_buffer_size = 4

logger = DataLogger(frame_shape, frame_dtype,
                    pre_buffer_size, post_buffer_size)

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
    logger.put(timestamp, frame)
    




