import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Empleadata", page_icon="💼")

# Título de la página
st.title("Empleadata 💼")

# Cabecera tabla
st.markdown("### Datos sobre los empleados en una app")

# Cargar datos
data = pd.read_csv("data/employees.csv")

# Mostrar tabla
st.write(data)

# Linea divisoria
st.markdown("---")

# Campos para modificar gráfica
col1, col2, col3 = st.columns(3)
with col1:
  color = st.color_picker("Elige un color para la gráfica", "#00AABF")
with col2:
  show_names = st.checkbox("Mostrar nombres de los empleados", value=True)
with col3:
  show_salary = st.checkbox("Mostrar salario de los empleados junto a la barra", value=True)

# Gráfica
fig, ax = plt.subplots()
sns.barplot(x="salary", y="full name", data=data, palette=[color], ax=ax)
plt.title("Salario de los empleados")
plt.xlabel("Salario (€)")
plt.ylabel("Nombre")

if not show_names:
    ax.set_yticklabels([])
if show_salary:
    for i, row in data.iterrows():
        ax.text(row["salary"], i, f"{row['salary']} €", va="center")
ax.set_xlim(0, data["salary"].max() * 1.3)  # Add padding to the x-axis
st.pyplot(fig)



