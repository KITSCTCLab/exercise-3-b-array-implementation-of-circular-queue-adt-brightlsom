class MyCircularQueue:
    def __init__(self, size: int):
        # Write code here
        self.max_size = size
        self.front = self.rear = -1
        self.circular_queue = [None] * size        

    def enqueue(self, value: int) -> bool:
        # Write code here
        if not self.is_full():
            if self.rear == -1 and self.front == -1:
                if len(self.circular_queue) == 0:
                    self.circular_queue = [None] * self.max_size
                self.rear = self.front = 0
                self.circular_queue[self.rear] = value
                return True
            else:
                self.rear = (self.rear + 1) % self.max_size
                self.circular_queue[self.rear] = value
                return True
        else:
            return False        

    def dequeue(self) -> bool:
        # Write code here
        if not self.is_empty():
            if self.rear == self.front:
                self.circular_queue.clear()
                self.rear = self.front = -1
                return True
            else:
                self.circular_queue[self.front] = None
                self.front = (self.front + 1) % self.max_size
                return True
        else:
            return False        

    def get_front(self) -> int:
        # Write code here
        if not self.is_empty():
            return self.circular_queue[self.front]
        else:
            return -1
        
    def get_rear(self):
        # Write code here
        if not self.is_empty():
            return self.circular_queue[self.rear]
        else:
            return -1
        
    def is_empty(self):
        # Write code here
        return True if self.rear == -1 and self.front == -1 else False        

    def is_full(self):
        # Write code here
        return True if ((self.rear + 1) % self.max_size == self.front) else False

# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
print(operations)
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
print(data)
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
