import numpy as np


class DataLogger:
    def __init__(self, pre_size, post_size):
        self.pre_size = pre_size
        self.post_size = post_size
        self.values = {}
        size = self.pre_size+self.post_size
        self.timestamps = np.zeros(size, np.datatime64)
        self.index = 0
    
    def add_signal(self, name, shape, dtype):
        size = self.pre_size + self.post_size
        buffer_shape = [size,]
        buffer_shape.extend(shape)
        self.buffer[name] = np.empty(buffer_shape, dtype=dtype)
    
    def update(self, timestamp):
        self.timestamps[self.index] = timestamp
        size = self.pre_size + self.post_size
        self.index = (self.index + 1) % size

    def put_signal(self, name, value):
        self.values[]