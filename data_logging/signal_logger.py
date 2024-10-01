import numpy as np
from .ring_buffer_manager import MultiRingBuffer
import time


class SignalLogger:
    def __init__(self, shape, dtype, pre_size, post_size, num_buffers):
        self.shape = shape
        self.dtype = dtype
        self.size = pre_size + post_size
        self.post_size = post_size
        self.num_buffers = num_buffers

        self.timestamps = MultiRingBuffer(num_buffers, self.size, (1,), 'datetime64[ns]')
        self.frames = MultiRingBuffer(num_buffers, self.size, shape, dtype)
        self.counter = 0
        self.is_triggered = False

    def run(self):
        if not self.is_triggered:
            time.sleep(0.01)
            return

        if self.counter < self.post_size:
            time.sleep(0.01)
            return
        
        self.timestamps.next_buffer()
        self.frames.next_buffer()
        for i in range(self.size):
            timestamp = self.timestamps.get(i)
            frame = self.frames.get(i)
            # TODO: save
        
        self.is_triggered = False
        self.counter = 0


    def put(self, timestamp, frame):
        self.timestamps.put(timestamp)
        self.frames.put(frame)
        if self.is_triggered:
            self.counter += 1
            if self.counter > self.size:

    
    def trigger(self, value=True):
        if value:
            if self.timestamps.is_full() and self.frames.is_full():
                self.timestamps.next_buffer()
                self.frames.next_buffer()
            
            
        
