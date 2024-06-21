#Distribución de Puntajes de Matemáticas por Nivel de Estudio de los Padres y Género

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('study_performance.csv')

# Crear un gráfico de caja y bigotes con los colores intercambiados para género
plt.figure(figsize=(16, 10))
sns.boxplot(x='parental_level_of_education', y='math_score', hue='gender', data=data, palette={'female': 'orange', 'male': 'lightblue'})
plt.title('Distribución de Puntajes de Matemáticas por Nivel de Estudio de los Padres y Género')
plt.xlabel('Nivel de Estudio de los Padres')
plt.ylabel('Puntaje de Matemáticas')
plt.legend(title='Género')
plt.xticks(rotation=45)
plt.show()
