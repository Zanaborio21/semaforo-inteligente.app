import streamlit as st

# Título
st.title("Semáforo Inteligente con Decisiones Complejas")

# Entradas del sistema
trafico_principal = st.radio("¿Tráfico en la calle principal?", ["Mucho", "Moderado", "Nada"])
trafico_secundaria = st.radio("¿Tráfico en la calle secundaria?", ["Mucho", "Moderado", "Nada"])
peatones = st.radio("¿Hay peatones esperando?", ["Sí", "No"])

# Convertir entradas a valores booleanos
sensor_principal_mucho = trafico_principal == "Mucho"
sensor_principal_moderado = trafico_principal == "Moderado"
sensor_secundaria_mucho = trafico_secundaria == "Mucho"
sensor_secundaria_moderado = trafico_secundaria == "Moderado"
sensor_peatones = peatones == "Sí"

# Lógica del semáforo
luz_principal = sensor_principal_mucho or (sensor_principal_moderado and not sensor_peatones)
luz_secundaria = not sensor_principal_mucho and sensor_secundaria_moderado
luz_peatones = sensor_peatones or (sensor_principal_moderado and sensor_secundaria_moderado)

# Mostrar estados de los semáforos
st.subheader("Estado de los Semáforos:")

# Calle Principal
if luz_principal:
    st.write("**Calle Principal:**")
    st.success("Verde")
else:
    st.write("**Calle Principal:**")
    st.error("Rojo")

# Calle Secundaria
if luz_secundaria:
    st.write("**Calle Secundaria:**")
    st.success("Verde")
else:
    st.write("**Calle Secundaria:**")
    st.error("Rojo")

# Peatones
if luz_peatones:
    st.write("**Peatones:**")
    st.success("Verde")
else:
    st.write("**Peatones:**")
    st.error("Rojo")

# Recomendación Final
st.subheader("Recomendación:")
if luz_peatones:
    st.info("¡Peatones tienen prioridad para cruzar!")
elif luz_principal:
    st.info("Calle Principal tiene prioridad.")
elif luz_secundaria:
    st.info("Calle Secundaria tiene prioridad.")
else:
    st.warning("Todos los semáforos están en rojo. No cruce.")
