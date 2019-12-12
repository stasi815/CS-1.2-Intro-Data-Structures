class Queue():
    """ Creates the model for queue objects. """

    def __init__(self):
        self.queue = []

    def __str__(self):
        return f'{self.queue}'

    def __iter__(self):
        return self.queue.__iter__()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)