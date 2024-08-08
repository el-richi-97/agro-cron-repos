#!/bin/bash

# Obtén el directorio del script actual
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR/.."
CRONJOBS_DIR="$PROJECT_DIR/cronjobs"

# Eliminar todas las entradas del crontab relacionadas con cualquier script en el directorio cronjobs
CRONTAB_TMP=$(mktemp)
crontab -l > $CRONTAB_TMP

for script in $CRONJOBS_DIR/*.py; do
    SCRIPT_PATH="$script"
    grep -v "$SCRIPT_PATH" $CRONTAB_TMP > $CRONTAB_TMP.tmp
    mv $CRONTAB_TMP.tmp $CRONTAB_TMP
done

crontab $CRONTAB_TMP
rm $CRONTAB_TMP

# Eliminar todas las tareas programadas de `at` relacionadas con cualquier script en el directorio cronjobs
for script in $CRONJOBS_DIR/*.py; do
    SCRIPT_PATH="$script"
    for job in $(atq | awk '{print $1}'); do
        if at -c "$job" | grep -q "$SCRIPT_PATH"; then
            atrm "$job"
        fi
    done
done

echo "Todos los cronjobs relacionados con los scripts en $CRONJOBS_DIR han sido eliminados."
