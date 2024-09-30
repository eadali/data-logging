import numpy as np
from threading import Thread
import time


class DataLogger:
    def __init__(self, shape, dtype, pre_size, post_size):
        self.size = pre_size + post_size
        self.post_size = post_size
        self.num_buffer = 4
        timestamps_shape = [self.num_buffer, self.size]
        frames_shape = [self.num_buffer, self.size, *shape]
        self.timestamps = np.empty(timestamps_shape, 'datetime64[ns]')
        self.frames = np.empty(frames_shape, dtype)
        self.index = 0
        self.buffer_index = 0 
        self.is_triggered = False
        self.is_saving = False

    # def run(self):
    #     if self.counter < self.post_size:
    #         time.sleep(0.01)
    #         return
        
    #     index = self.index
    #     for _ in range(self.size):
    #         index = (index + 1)  % self.size

    #     if self.is_triggered:
    #         if self.counter > self.post_size:
    #             index = self.index
    #             for _ in range(self.size):

    #                 index = index + 1


    def put(self, timestamp, frame):
        self.timestamps[self.buffer_index, self.index] = timestamp
        self.frames[self.buffer_index, self.index] = frame
        self.index = (self.index + 1)  % self.size
        if self.is_triggered:
            self.counter += 1
    
    def save(self, trigger=True):
        if trigger:
            self.counter = 0
            self.is_triggered = True
            self.buffer_index += 1
        
