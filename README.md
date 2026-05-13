# Portafolio Profesional - César Reverón G.

Portfolio técnico orientado a demostrar capacidades en análisis de datos, automatización de procesos y herramientas de IA aplicadas a entornos técnicos.

## Perfil

**Rol:** Data Analyst en transición profesional

**Especialización:** Automatización de procesos técnicos mediante Python e IA. Background en integración de sistemas UAV/UAS, radioenlaces y telemetría.

**Ubicación:** Torrejón de Ardoz, Madrid

## Estructura del Proyecto

```
portafolio/
├── index.html                    # Sitio web principal
├── proyectos/
│   ├── 01_eda/                  # Análisis Exploratorio de Datos
│   │   ├── data/                # Datasets y resultados
│   │   ├── src/                 # Scripts Python
│   │   └── notebooks/           # Jupyter Notebooks
│   ├── 02_dashboard/            # Dashboard interactivo
│   │   ├── data/                # Métricas en JSON
│   │   └── dashboard.html       # Visualización con Chart.js
│   ├── 03_automacion/           # Automatización con IA
│   │   ├── scripts/             # Scripts de automatización
│   │   └── docs/                # Documentación
│   └── 04_terminal/             # Terminal y CLI
│       └── docs/                # Documentación
├── docs/                        # Documentación técnica
│   └── portfolio_v01.md
└── README.md
```

## Proyectos

### Proyecto 1: EDA (Análisis Exploratorio de Datos)

Procesamiento y visualización de datasets sintéticos.

**Stack:** Python, Pandas, Matplotlib, Jupyter

**Características:**
- Limpieza de datos
- Detección de anomalías
- Estadísticas descriptivas
- Visualizaciones técnicas

[Ver notebook](./proyectos/01_eda/notebooks/analysis.ipynb)

### Proyecto 2: Dashboard de Datos Técnicos

Dashboard interactivo con métricas operativas.

**Stack:** HTML, JavaScript, Chart.js, JSON

**Características:**
- Tendencia temporal
- Distribución por categoría
- Estados del sistema
- KPIs en tiempo real

[Ver dashboard](./proyectos/02_dashboard/dashboard.html)

### Proyecto 3: Automatización con IA

Scripts de automatización mediante APIs de IA.

**Stack:** Python, APIs de IA, Prompt Engineering

**Características:**
- Consumo de APIs de IA
- Generación automática de reportes
- Optimización de prompts

[Ver documentación](./proyectos/03_automacion/docs/README.md)

### Proyecto 4: Terminal y Línea de Comandos

Gestión de entornos técnicos mediante terminal.

**Stack:** Bash, Git, WSL, Python CLI

**Características:**
- Automatización CLI
- Control de versiones
- Flujo de trabajo técnico

[Ver documentación](./proyectos/04_terminal/docs/README.md)

## Stack Tecnológico

| Área | Tecnologías |
|------|-------------|
| Procesamiento de Datos | Python, Pandas, NumPy |
| Bases de Datos | SQL, SQLite |
| Visualización | Matplotlib, Plotly, Chart.js, Power BI |
| Automatización | Python, APIs IA, Bash |
| Entorno Técnico | VS Code, WSL, Git, Jupyter |

## Setup Local

### Requisitos

- Python 3.10+
- Git
- (Opcional) WSL para entorno Linux

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/CesaReveron/portafolio.git
cd portafolio

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows

# Instalar dependencias
pip install -r proyectos/01_eda/requirements.txt
```

### Ejecutar Análisis

```bash
# Generar dataset
python proyectos/01_eda/src/generate_data.py

# Limpiar datos
python proyectos/01_eda/src/data_cleaning.py

# Generar análisis
python proyectos/01_eda/src/analysis.py
```

### Ver Dashboard

Abrir `proyectos/02_dashboard/dashboard.html` en un navegador.

## Despliegue

El sitio está configurado para GitHub Pages. Cada push a `main` activa el despliegue automático.

**URL:** https://cesareveron.github.io/portafolio

## Contacto

- **Email:** reveronprograma@gmail.com
- **Teléfono:** +34 643 518 623
- **GitHub:** [CesaReveron](https://github.com/CesaReveron)
- **LinkedIn:** [César Reverón](https://linkedin.com/in/cesar-reveron)
- **Ubicación:** Torrejón de Ardoz, Madrid

## Roadmap

- [x] Crear estructura de proyectos
- [x] Implementar EDA con Python
- [x] Crear dashboard interactivo
- [x] Documentar automatización IA
- [x] Documentar flujo terminal
- [ ] Implementar más visualizaciones
- [ ] Añadir tests unitarios
- [ ] Configurar CI/CD

---

*Última actualización: Mayo 2026*