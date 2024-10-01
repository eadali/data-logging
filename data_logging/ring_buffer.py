import numpy as np


class RingBuffer:
    def __init__(self, capacity, data_shape, data_type):
        # Initialize the ring buffer with given capacity, shape, and data type
        self.capacity = capacity
        self.data_shape = data_shape
        self.data_type = data_type
        self.buffer = np.empty([capacity, *data_shape], data_type)
        self.current_index = 0
        self.current_size = 0
    
    def put(self, value):
        # Insert a new value into the buffer at the current index
        self.buffer[self.current_index] = value
        # Update the index to the next position, wrapping around if necessary
        self.current_index = (self.current_index + 1) % self.capacity
        # Increase the size of the buffer if it's not yet full
        if self.current_size < self.capacity:
            self.current_size += 1
        
    def get(self, index):
        # Retrieve a value from the buffer at the given index, adjusted for wrapping
        return self.buffer[(self.current_index + index) % self.capacity]
    
    def is_full(self):
        # Check if the buffer is full
        return self.current_size == self.capacity