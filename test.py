from data_logging import DataLogger
import numpy as np


pre_size = 10
post_size = 5
shape = (128, 256, 3)


logger = DataLogger(pre_size, post_size)
logger.add_signal('frame', shape, dtype=np.uint8)
print(logger.buffer['frame'].shape)


