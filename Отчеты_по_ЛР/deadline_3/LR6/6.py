class Frange:
    def __init__(self, start, stop=None, step=1.0):
        if stop is None:
            self.start = 0.0
            self.stop = float(start)
        else:
            self.start = float(start)
            self.stop = float(stop)
        self.step = float(step)
        self.current = self.start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

for x in Frange(1, 10, 0.5):
    print(x)