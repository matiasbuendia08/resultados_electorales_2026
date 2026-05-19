# Perú vota 2026 · Resultados distritales

Visualizador interactivo de resultados electorales de la primera vuelta 2026 a nivel distrital, con análisis socioeconómico y comparación histórica con 2021.

## Qué hace

- **Resumen**: distribución del voto entre todos los partidos con barra interactiva y tarjetas por candidato. Al seleccionar un departamento, provincia o distrito muestra indicadores socioeconómicos (pobreza, IDH, colegios, viviendas) y gráficos de evolución histórica (IDH, IDE, salud, educación, economía).
- **Todos los candidatos**: tabla ordenable con votos y porcentaje de cada candidato por nivel geográfico.
- **Por distrito**: grilla de tarjetas con el resultado FP vs JP y los indicadores clave de cada distrito.
- **Análisis post-primera vuelta**: sección enfocada exclusivamente en el duelo Fuerza Popular vs. Juntos por el Perú de cara al balotaje. Incluye perfil socioeconómico del voto, cambio territorial respecto a 2021 (Castillo vs. Keiko) y tabla de distritos en disputa (resultado cerrado entre ambas fuerzas).

## Archivos

| Archivo | Descripción |
|---|---|
| `index.html` | Toda la aplicación (HTML + CSS + JS en un solo archivo) |
| `datos.json.gz` | Datos electorales y socioeconómicos comprimidos, generados desde el Excel fuente |
| `convertir.py` | Script para convertir el Excel fuente a `datos.json.gz` |
| `distrital_web.xlsx` | Última versión del Excel publicada (referencia) |

> El archivo Excel fuente con el que trabajo localmente no está en este repositorio. `convertir.py` toma ese archivo y genera `datos.json.gz`, que es lo que carga la app.

## Cómo actualizar los datos

1. Editar el Excel fuente localmente
2. Correr `python convertir.py`
3. Subir el `datos.json.gz` generado a este repositorio

## Fuentes

- Resultados electorales: ONPE
- Pobreza monetaria 2018: INEI – Mapa de Pobreza Provincial y Distrital 2018
- IDH e IDE 2017–2024: PNUD / PNUD-DGSE
- Colegios con servicios básicos: MINEDU
- Infraestructura educativa: INEI (Censo 2017)

## Elaboración

Matias Buendia · [LinkedIn](https://www.linkedin.com/in/matiasbuendia/)
