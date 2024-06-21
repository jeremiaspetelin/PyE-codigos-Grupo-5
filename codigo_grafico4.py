import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
file_path = 'study_performance.csv'
df = pd.read_csv(file_path)

# Create a countplot for test preparation course by gender
plt.figure(figsize=(10, 6))
sns.countplot(x='test_preparation_course', hue='gender', data=df)

# Add a title and labels to the plot
plt.title('Cantidad de Estudiantes que se Prepararon para la Evaluación por Género')
plt.xlabel('Preparación para la Evaluación')
plt.ylabel('Cantidad de Estudiantes')

# Display the plot
plt.show()
