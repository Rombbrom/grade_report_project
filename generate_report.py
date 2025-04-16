
import pandas as pd

# Чтение Excel-файла
df = pd.read_excel("grades.xlsx")

# Фильтрация по факультету "ФИЗ"
filtered_df = df[df["Факультет"] == "ЭМФ"]

# Расчет средней оценки по каждому студенту
report_df = filtered_df.groupby("ФИО").agg({"Оценка": "mean"}).reset_index()
report_df.columns = ["ФИО", "Средняя оценка"]

# Сохранение в Excel
report_df.to_excel("отчет_по_оценкам.xlsx", index=False)
print("Отчет успешно создан: отчет_по_оценкам.xlsx")
