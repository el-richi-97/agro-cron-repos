import sys
import os
import datetime

# Añadir el directorio del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cronjobs.common.queries import QUERY_UPDATE_CANT_SALIDAS_ACTIVIDAD
from cronjobs.common.service_queries import PostgreSQLManager


def run():
    print('\n===========================================================================')
    print(f'Inicio de la ejecución: {datetime.datetime.now()}')
    print('Actualizando conteo de salidas por actividad...')
    db_manager = PostgreSQLManager()
    db_manager.connect()

    try:
        db_manager.execute_query(QUERY_UPDATE_CANT_SALIDAS_ACTIVIDAD)
        print('Conteo de salidas actualizado correctamente')

    except Exception as e:
        print(f'Error actualizando conteo de salidas para las actividades: {e}')

    finally:
        db_manager.close()
        print('Conexión cerrada')
