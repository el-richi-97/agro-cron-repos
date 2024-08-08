# Agroptimum Cronjobs

Este proyecto está diseñado para generar cronjobs en Python que se ejecutan de forma nativa en Linux, sin necesidad de
frameworks intermediarios. Estos cronjobs se comunican con la base de datos del proyecto Agroptimum para automatizar
procesos que se reflejan en una aplicación que se alimenta de dicha base de datos.

## Estructura del Proyecto

- `cronjobs/`: Contiene los scripts Python que se ejecutan como cronjobs.
- `scripts/`: Contiene los scripts `.sh` que configuran la recurrencia de ejecución de los cronjobs.
- `logs/`: Directorio donde se almacenan los archivos de logs generados por los cronjobs.
- `tests/`: Pruebas unitarias y de integración para los cronjobs.
- `.env`: Archivo que contiene las variables de entorno necesarias para el proyecto.
- `requirements.txt`: Archivo de dependencias de Python necesarias para el proyecto.
- `venv/`: Entorno virtual de Python.

## Requisitos

- Python 3.8+
- Linux

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd agro-cron-repos
    ```

2. Crea y activa el entorno virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno. Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente
   contenido:
    ```
    DB_HOST=<host_de_la_base_de_datos>
    DB_PORT=<puerto_de_la_base_de_datos>
    DB_USER=<usuario_de_la_base_de_datos>
    DB_PASSWORD=<contraseña_de_la_base_de_datos>
    DB_NAME=<nombre_de_la_base_de_datos>
    ```

## Ejecución de Cronjobs

Para ejecutar los cronjobs, debes configurar los scripts `.sh` proporcionados en el directorio `scripts/`. Cada
script `.sh` corresponde a un cronjob específico y contiene la configuración necesaria para ejecutar el cronjob en
intervalos específicos.

### Importante

Es necesario especificar una fecha mayor a la actual en cada uno de los scripts `.sh` de los cronjobs. Asegúrate de
modificar la línea de configuración de fecha en cada script para reflejar una fecha y hora futuras.

### Ejemplo de Script `.sh`

Supongamos que tienes un script llamado `set_agro_update_id_estado_actividad.sh` con el siguiente contenido:

```sh
#!/bin/bash

# Configuración de cronjob específica para actualizar el estado de actividad
source /path/to/your/project/venv/bin/activate
python /path/to/your/project/cronjobs/set_agro_update_id_estado_actividad.py >> /path/to/your/project/logs/set_agro_update_id_estado_actividad.log 2>&1
