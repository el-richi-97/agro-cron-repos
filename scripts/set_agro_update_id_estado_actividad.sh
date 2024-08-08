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
source "$ENV_PATH"/bin/activate
python "$SCRIPT_PATH" >> "$LOG_PATH" 2>&1
deactivate

# Añadir cronjob recurrente
(crontab -l ; echo "$CRON_SCHEDULE export PYTHONPATH=\"$PROJECT_DIR\" && source $ENV_PATH/bin/activate && python $SCRIPT_PATH >> $LOG_PATH 2>&1 && deactivate") | crontab -

echo "Cronjob recurrente configurado e iniciado inmediatamente."
