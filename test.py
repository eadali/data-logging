from data_logging import DataLogger
import numpy as np
import cv2
from datetime import datetime




color_shape = (480, 640, 3)
depth_shape = (480, 640)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3
font_color = (255,255,255)
thickness = 5
pos = (50, 200)

logger = DataLogger()
logger.add_signal('color', color_shape, np.uint8, 8, 4)
logger.add_signal('depth', depth_shape, np.uint16, 10, 5)

for i in range(1000):
    timestamp = np.datetime64(datetime.now())
    color = np.zeros(color_shape, dtype=np.uint8)
    cv2.putText(color, str(i), pos, font, font_scale, font_color, thickness)
    depth = np.zeros(depth_shape, dtype=np.uint16)
    cv2.putText(color, str(i), pos, font, font_scale, font_color, thickness)

    logger.put_signal('color', timestamp, color)
    logger.put_signal('depth', timestamp, depth)
    




