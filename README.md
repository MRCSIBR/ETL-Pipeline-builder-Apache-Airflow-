

# ETL-Pipeline-builder-Apache-Airflow  
Plantilla reutilizable para construir flujos de trabajo ETL utilizando Airflow, incluyendo DAGs para la extracción, transformación y carga de datos en bases de datos o almacenes de datos.
## Requisitos  
- Docker  
- Docker Compose  

## Instalación  

1. Clona el repositorio:  
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd etl_pipeline
   ```

2. Construye y ejecuta los servicios:  
   ```bash
   docker-compose up --build
   ```

3. Accede a la interfaz web de Airflow en [http://localhost:8080](http://localhost:8080). Usa las credenciales:

   - **Usuario:** admin  
   - **Contraseña:** admin  

## Estructura del Pipeline

- **Extract:** Extrae datos de un archivo CSV (ejemplo: URL externa).
- **Transform:** Aplica transformaciones (ejemplo: agrega una nueva columna).
- **Load:** Carga los datos transformados en una base de datos SQLite.

---

## Personalización  

- Modifica `scripts/transform_data.py` para ajustar las funciones de extracción, transformación y carga según tus necesidades.
- Actualiza `dags/etl_pipeline.py` para cambiar el programa de ejecución o agregar más tareas.

---

## Notas

- El pipeline se ejecuta diariamente (`schedule_interval='@daily'`).
- Los datos se almacenan temporalmente en `/tmp` dentro del contenedor.
