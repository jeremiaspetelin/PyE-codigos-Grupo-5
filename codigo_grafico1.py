import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('study_performance.csv')

plt.figure(figsize=(10, 6))
sns.boxplot(x='race_ethnicity', y='math_score', data=data, palette='Set2')
plt.title('Distribución de los Puntajes de Matemáticas por Raza')
plt.xlabel('Raza / Etnicidad')
plt.ylabel('Puntaje de Matemáticas')
plt.show()