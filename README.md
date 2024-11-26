# 🚦 Semáforo Inteligente

Este proyecto simula un sistema de semáforos que toma decisiones basadas en el tráfico y la presencia de peatones utilizando **Python** y **Streamlit**. El objetivo es optimizar el flujo vehicular y garantizar la seguridad de los peatones.

## 🌐 Accede a la Aplicación

Puedes probar la aplicación en el siguiente enlace:  
[Semáforo Inteligente](https://blank-app-zcmd4wzboas.streamlit.app/)

## 🚦 Funcionalidad

1. **Entrada**:
   - Tráfico en la calle principal: `Mucho`, `Moderado`, `Nada`.
   - Tráfico en la calle secundaria: `Mucho`, `Moderado`, `Nada`.
   - Presencia de peatones: `Sí` o `No`.

2. **Salida**:
   - Estado de los semáforos:
     - Calle principal.
     - Calle secundaria.
     - Peatones.
   - Recomendaciones sobre quién tiene prioridad.

## ✨ Ejemplo

**Entrada**:
- Tráfico en la calle principal: Moderado.
- Tráfico en la calle secundaria: Mucho.
- Peatones: No.

**Salida**:
- Calle Principal: Verde.
- Calle Secundaria: Rojo.
- Peatones: Rojo.

**Recomendación**:
Calle Principal tiene prioridad.
