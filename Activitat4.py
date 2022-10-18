import pandas as pd 
df = pd.read_csv("students_grades.csv")

mitjana = df["grades"].mean()
mediana = df["grades"].median()

print("""
Mitjana: %d
Mediana: %d
"""%(mitjana,mediana))
