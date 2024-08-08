import sys
import os
import datetime

# Añadir el directorio del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cronjobs.common.queries import QUERY_UPDATE_PORCENTAJE_CUMPLIMIENTO_ACTIVIDADES
from cronjobs.common.service_queries import PostgreSQLManager


def run():
    print('\n===========================================================================')
    print(f'Inicio de la ejecución: {datetime.datetime.now()}')
    print('Actualizando porcentaje de cumplimiento de actividades...')
    db_manager = PostgreSQLManager()
    db_manager.connect()

    try:
        db_manager.execute_query(QUERY_UPDATE_PORCENTAJE_CUMPLIMIENTO_ACTIVIDADES)
        print('Porcentajes de actividades actualizados correctamente')

    except Exception as e:
        print(f'Error actualizando los porcentajes de actividades: {e}')

    finally:
        db_manager.close()
        print('Conexión cerrada')


if __name__ == "__main__":
    run()
