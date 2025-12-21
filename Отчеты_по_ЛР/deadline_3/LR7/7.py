class Vector3D:
    __slots__ = ('x', 'y', 'z') 
    
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

v = Vector3D(1.0, 2.0, 3.0)
print(v)

try:
    print(v.__dict__)
except AttributeError as e:
    print(f"нет __dict__: {e}")

try:
    v.color = "red"
except AttributeError as e:
    print(f"нельзя добавить новый атрибут: {e}")