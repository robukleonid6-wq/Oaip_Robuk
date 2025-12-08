def build_user_profile(user_id: int, **info) -> dict:
    d = {"user_id": user_id}
    for k, v in info.items():
        d[k] = v
    return d

p = build_user_profile(101, name="Заур мен бэк", status="online", email="kvach_umer@gmail.com")
print(p)
