import sys
import os
import datetime

# Añadir el directorio del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cronjobs.common.queries import QUERY_AGRO_UPDATE_ID_ESTADO_ACTIVIDAD
from cronjobs.common.service_queries import PostgreSQLManager


def run():
    print('\n===========================================================================')
    print(f'Inicio de la ejecución: {datetime.datetime.now()}')
    print('Actualizando id de actividades...')
    db_manager = PostgreSQLManager()
    db_manager.connect()

    try:
        db_manager.execute_query(QUERY_AGRO_UPDATE_ID_ESTADO_ACTIVIDAD)
        print('IDs de actividades actualizados correctamente')

    except Exception as e:
        print(f'Error actualizando los ID de actividades: {e}')

    finally:
        db_manager.close()
        print('Conexión cerrada')


if __name__ == "__main__":
    run()
