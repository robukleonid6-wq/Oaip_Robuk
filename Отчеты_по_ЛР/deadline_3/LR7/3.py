class StringUtils:
    @staticmethod
    def invert(string: str) -> str:
        return string[::-1]
    
    @staticmethod
    def normalize(string: str) -> str:
        return string.strip().lower()

class User:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
    
    def __repr__(self):
        return f"User(name='{self.name}', role='{self.role}')"
    
    @classmethod
    def from_string(cls, data_string: str):
        name, role = data_string.split(";")
        return cls(name, role)

print(StringUtils.invert("Hello"))
print(StringUtils.normalize("  DATA  "))

user = User.from_string("Alice;Admin")
print(user.name)
print(user.role)
print(user)