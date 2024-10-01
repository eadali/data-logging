import numpy as np
from .ring_buffer import RingBuffer


class RingBufferManager:
    def __init__(self, num_buffers, buffer_capacity, data_shape, data_type):
        # Initialize multiple ring buffers with the given parameters
        self.num_buffers = num_buffers
        self.buffer_capacity = buffer_capacity
        self.data_shape = data_shape
        self.data_type = data_type
        self.buffers = [RingBuffer(buffer_capacity, data_shape, data_type) for _ in range(num_buffers)]
        self.current_buffer_index = 0

    def put(self, value):
        # Insert a new value into the current buffer
        self.buffers[self.current_buffer_index].put(value)
    
    def get(self, index):
        # Retrieve a value from the buffer at the given index, adjusted for wrapping
        buffer = np.empty([self.buffer_capacity, *self.data_shape], self.data_type)
        for i in range(self.buffer_capacity):
            buffer[i] = self.buffers[(self.current_buffer_index + index) % self.num_buffers].get(i)
        return buffer
    
    def is_full(self):
        # Check if the current buffer is full
        return self.buffers[self.current_buffer_index].is_full()

    def next_buffer(self):
        # Move to the next buffer, wrapping around if necessary
        self.current_buffer_index = (self.current_buffer_index + 1) % self.num_buffers
