import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
file_path = 'study_performance.csv'
df = pd.read_csv(file_path)

# Calcular la mediana de los puntajes de matemáticas, lectura y escritura por tipo de almuerzo
median_scores = df.groupby('lunch')[['math_score', 'reading_score', 'writing_score']].median().reset_index()

# Transformar el DataFrame a formato largo para facilitar la creación del gráfico con seaborn
median_scores_melted = median_scores.melt(id_vars='lunch', var_name='Subject', value_name='Median Score')

# Crear un gráfico de barras para la mediana de los puntajes por tipo de almuerzo
plt.figure(figsize=(12, 8))
sns.barplot(x='lunch', y='Median Score', hue='Subject', data=median_scores_melted)

# Añadir título y etiquetas a los ejes
plt.title('Mediana de Puntajes por Tipo de Almuerzo')
plt.xlabel('Tipo de Almuerzo')
plt.ylabel('Mediana de Puntaje')

# Mostrar el gráfico
plt.show()