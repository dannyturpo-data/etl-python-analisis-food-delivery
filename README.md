# 🍽️ ETL y Business Intelligence para una Plataforma de Food Delivery

## 📖 Descripción

Este proyecto desarrolla un proceso ETL (Extract, Transform, Load) utilizando Python, Pandas y SQLite para integrar, limpiar y analizar información de restaurantes y menús de una plataforma de Food Delivery.

El objetivo principal es transformar datos provenientes de múltiples archivos CSV en una base de datos estructurada, permitiendo responder preguntas estratégicas de negocio mediante consultas SQL y visualizaciones orientadas a la toma de decisiones.


## 🎯 Objetivos del proyecto

Construir un pipeline ETL completo.
Integrar información de restaurantes y menús.
Aplicar procesos de limpieza y transformación de datos.
Optimizar la calidad de la información.
Almacenar los datos en una base SQLite.
Realizar análisis exploratorios mediante SQL.
Generar visualizaciones enfocadas en Business Intelligence.


## 🛠 Tecnologías utilizadas

Herramienta	Uso
Python	Desarrollo del pipeline ETL
Pandas	Limpieza y transformación de datos
SQLite	Base de datos local
SQLAlchemy	Conexión entre Python y SQLite
SQL	Consultas analíticas
Matplotlib	Visualización de datos
Google Colab	Desarrollo del proyecto
Git	Control de versiones
GitHub	Gestión del repositorio


## 📂 Estructura del Proyecto

etl-python-analisis-food-delivery/

│
├── data/
│   ├── raw/
│   │   └── restaurant-menus.csv
│   │   └── restaurants.csv
│   ├── processed/
│   │   └── df_master.csv
│   └── base_datos/
│       └── delivery_insights.db
│
├── notebooks/
│   ├── 01_EXPLORATORIO_FOOD_DELIBERY.ipynb
│   ├── 02_Limpieza_FOOD_DELIVERY_TRANSFORM.ipynb
│   └── 03_CARGA_BASE_DATOS_LOAD.ipynb
│   └── 04_BUSINESS_INTELLIGENCE_DELIVEY_INSIGHT.ipynb
│
├── src/
│   ├── exploracion_df.py
│   ├── limpieza_restaurantes.py
│   └── limpieza_menus.py
│
├── README.md
│
└── TPI_Python_ETL.pdf


## ⚙️ Flujo ETL
Extracción
──────────

Restaurants.csv
Restaurant_Menus.csv (10 archivos)

        │
        ▼

Transformación
──────────────

✔ Limpieza de datos
✔ Tratamiento de valores nulos
✔ Conversión de tipos de datos
✔ División de direcciones
✔ Normalización de texto
✔ Conversión de rangos de precios
✔ Filtrado de registros
✔ Integración de información

        │
        ▼

Carga
─────

SQLite
delivery_insights.db

Tabla:

master_food_data

        │
        ▼

Business Intelligence

SQL
+
Visualizaciones
+
Insights de negocio


## 🧹 Transformaciones

### Restaurantes

- Limpieza de valores nulos.
- División de la dirección completa.
- Conversión del rango de precios.
- Normalización de categorías.
- Eliminación de registros inválidos.

### Menús

- Conversión del precio a formato numérico.
- Eliminación de precios nulos o iguales a cero.
- Estandarización de texto.
- Tratamiento de descripciones faltantes.


## Carga de Datos Load

Los datos transformados fueron almacenados en una base de datos SQLite denominada:

delivery_insights.db

Tabla principal:

master_food_data


## 📊 Business Intelligence

Se desarrollaron consultas SQL para responder preguntas estratégicas del negocio.

1. Penetración geográfica
Top 5 ciudades con mayor cantidad de restaurantes consolidados.
2. Distribución por rango de precios
Participación de restaurantes según su categoría de precios.
3. Estrategia de menú
Precio promedio de los platos en las ciudades con mayor presencia.
4. Correlación precio-calidad
Relación entre el rango de precios y la satisfacción del usuario.
5. Ciudades con mayor satisfacción
Ranking de ciudades según el puntaje promedio de sus restaurantes.


## 📈 Principales hallazgos
La mayor concentración de restaurantes se encuentra en un reducido grupo de ciudades.
Los restaurantes económicos presentan niveles de satisfacción comparables con categorías de mayor precio.
No se encontró evidencia de que un mayor precio garantice una mejor experiencia para el usuario.
Existen categorías gastronómicas altamente representadas que concentran una parte importante del mercado.
La integración de datos permitió construir una base consolidada lista para futuros análisis.


## 👨‍💻 Autor

Danny Turpo Condori

Ingeniero Electrónico | Data Analytics | Python | SQL | Power BI