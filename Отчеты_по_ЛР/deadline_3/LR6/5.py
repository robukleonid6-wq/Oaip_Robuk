class SmartList(list):
    def __getitem__(self, index):
        if index < 0:
            new_index = -index - 1
            if new_index >= len(self):
                return super().__getitem__(index)
            return super().__getitem__(new_index)
        else:
            return super().__getitem__(index)

sl = SmartList([10, 20, 30])
print(sl[0])   
print(sl[-1]) 
print(sl[-2]) 
print(sl[-3])  
print(sl[-0])  