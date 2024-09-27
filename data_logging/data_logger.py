import numpy as np


class DataLogger:
    def __init__(self):
        self.timestamps = {}
        self.values = {}
        self.indeces = {}
        self.sizes = {}
        self.post_sizes = {}
        self.triggers = {}
    
    def add_signal(self, name, shape, dtype, pre_size, post_size):
        size = pre_size + post_size
        values_shape = [size,]
        values_shape.extend(shape)
        self.values[name] = np.empty(values_shape, dtype=dtype)
        self.timestamps[name] = np.empty(size, 'datetime64[ns]')
        self.indeces[name] = 0
        self.sizes[name] = size
        self.post_sizes[name] = post_size
        self.triggers[name] = 0

    def put_signal(self, name, timestamp, value):
        index = self.indeces[name]
        self.timestamps[name][index] = timestamp
        self.values[name][index] = value
        size = self.sizes[name]
        self.indeces[name] = (index + 1)  % size
    

    def save(self):
        pass
