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

5. Otorga permisos de ejecución a los scripts `.sh`:
    ```sh
    chmod +x scripts/*.sh
    ```

6. Instala el comando `at` (si no está instalado):

   ### En Ubuntu/Debian:
    ```sh
    sudo apt-get update
    sudo apt-get install at
    ```

   ### En CentOS/RHEL:
    ```sh
    sudo yum install at
    ```

   ### En Fedora:
    ```sh
    sudo dnf install at
    ```

   ### En Arch Linux:
    ```sh
    sudo pacman -S at
    ```

## Ejecución de Cronjobs

Para ejecutar los cronjobs, debes configurar y ejecutar los scripts `.sh` proporcionados en el directorio `scripts/`.
Cada script `.sh` corresponde a un cronjob específico y contiene la configuración necesaria para ejecutar el cronjob en
intervalos específicos. El comando para la ejecución de un cronjob es el siguiente: `/bin/sh/ <NOMBRE_DEL_SCRIPT>.sh`.

```sh

### Ejemplo de Script `.sh`

Supongamos que tienes un script llamado `set_agro_update_id_estado_actividad.sh` con el siguiente contenido:

```sh
#!/bin/bash

# Obtén el directorio del script actual
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR/.."
CRONJOBS_DIR="$PROJECT_DIR/cronjobs"

# Configuración de cronjob recurrente
CRON_SCHEDULE="* * * * *"  # Cada minuto
SCRIPT_PATH="$CRONJOBS_DIR/agro_update_id_estado_actividad.py"
ENV_PATH="$PROJECT_DIR/venv"
LOG_PATH="$PROJECT_DIR/logs/agro_update_id_estado_actividad.log"

# Crear directorio de logs si no existe
mkdir -p "$(dirname "$LOG_PATH")"

# Ejecutar el script inmediatamente
export PYTHONPATH="$PROJECT_DIR"
source $ENV_PATH/bin/activate
python $SCRIPT_PATH >> $LOG_PATH 2>&1
deactivate

# Añadir cronjob recurrente
(crontab -l ; echo "$CRON_SCHEDULE export PYTHONPATH=\"$PROJECT_DIR\" && source $ENV_PATH/bin/activate && python $SCRIPT_PATH >> $LOG_PATH 2>&1 && deactivate") | crontab -

echo "Cronjob recurrente configurado e iniciado inmediatamente."
