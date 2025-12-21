def filtr_logov(log_lst, keyword):
    for log in log_lst:
        if keyword in log:
            yield log

logi = [
    "info: server started",
    "error: database connection failed",
    "info: user logged in",
    "error: file not found"
]
for oshibka in filtr_logov(logi, "info"):
    print(oshibka)