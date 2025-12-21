def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

@make_bold
def get_text():
    return "Hello, World!"

print(get_text())