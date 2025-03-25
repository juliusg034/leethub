class MovingAverage:
    from collections import deque

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        self.queue.append(val)
        avg = 0
        n = len(self.queue)
        
        if n <= self.size:
            sum = 0
            for num in self.queue:
                sum += num
            avg = sum / n
        
        else:
            self.queue.popleft()
            sum = 0
            for num in self.queue:
                sum += num
            avg = sum / self.size
            
        return avg
                
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
    