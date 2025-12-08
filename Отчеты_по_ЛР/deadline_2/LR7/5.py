def format_report(report_title: str, *data, **props) -> None:
    print(f"--- Отчет: {report_title} ---")
    print("Данные:")
    for el in data:
        print(f" - {el}")
    print()
    print("Свойства:")
    for k, v in props.items():
        print(f" - {k}: {v}")
    print("------------------------------")


format_report(
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Заур А.В.",
    date="2077-11-04"
)
