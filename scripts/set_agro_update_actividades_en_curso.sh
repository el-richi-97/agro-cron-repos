#!/bin/bash

# Obtén el directorio del script actual
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR/.."
CRONJOBS_DIR="$PROJECT_DIR/cronjobs"

# Configuración de cronjob recurrente
CRON_SCHEDULE="* * * * *"  # Cada minuto
SCRIPT_PATH="$CRONJOBS_DIR/agro_update_actividades_en_curso.py"
ENV_PATH="$PROJECT_DIR/venv"
LOG_PATH="$PROJECT_DIR/logs/agro_update_actividades_en_curso.log"

# Crear directorio de logs si no existe
mkdir -p "$(dirname "$LOG_PATH")"

# Fecha y hora de inicio en formato 'YYYY-MM-DD HH:MM' (ajusta la fecha y hora según sea necesario)
START_DATETIME="2024-08-08 07:19"

# Detectar sistema operativo y convertir fecha y hora de inicio a un formato manejable
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    AT_FORMAT=$(date -d "$START_DATETIME" +"%H:%M %m%d%Y")
elif [[ "$OSTYPE" == "darwin"* ]]; then
    AT_FORMAT=$(date -j -f "%Y-%m-%d %H:%M" "$START_DATETIME" +"%H:%M %m%d%Y")
else
    echo "Sistema operativo no soportado"
    exit 1
fi

# Depuración
echo "Formato de fecha y hora para 'at': $AT_FORMAT"

# Crear un comando at para la primera ejecución
echo "export PYTHONPATH=\"$PROJECT_DIR\" && source $ENV_PATH/bin/activate && python $SCRIPT_PATH >> $LOG_PATH 2>&1 && deactivate" | at "$AT_FORMAT"

# Verificar si el comando 'at' fue programado correctamente
if [[ $? -ne 0 ]]; then
    echo "Error al programar el comando 'at'"
    exit 1
fi

# Añadir cronjob recurrente
(crontab -l ; echo "$CRON_SCHEDULE export PYTHONPATH=\"$PROJECT_DIR\" && source $ENV_PATH/bin/activate && python $SCRIPT_PATH >> $LOG_PATH 2>&1 && deactivate") | crontab -

echo "Cronjob recurrente configurado e iniciado inmediatamente."
