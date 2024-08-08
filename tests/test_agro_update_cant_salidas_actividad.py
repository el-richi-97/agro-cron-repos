import unittest
from unittest.mock import patch

from cronjobs.agro_update_cant_salidas_actividad import run
from cronjobs.common.queries import QUERY_UPDATE_CANT_SALIDAS_ACTIVIDAD


class TestAgroUpdateCantSalidasActividad(unittest.TestCase):

    @patch('cronjobs.agro_update_cant_salidas_actividad.PostgreSQLManager')
    def test_successful_update(self, mock_postgre_sql_manager):
        mock_db_manager = mock_postgre_sql_manager.return_value
        mock_db_manager.execute_query.return_value = None

        run()

        mock_db_manager.connect.assert_called_once()
        mock_db_manager.execute_query.assert_called_once_with(QUERY_UPDATE_CANT_SALIDAS_ACTIVIDAD)
        mock_db_manager.close.assert_called_once()

    @patch('cronjobs.agro_update_cant_salidas_actividad.PostgreSQLManager')
    def test_update_with_exception(self, mock_postgre_sql_manager):
        mock_db_manager = mock_postgre_sql_manager.return_value
        mock_db_manager.execute_query.side_effect = Exception("Test exception")

        run()

        mock_db_manager.connect.assert_called_once()
        mock_db_manager.execute_query.assert_called_once_with(QUERY_UPDATE_CANT_SALIDAS_ACTIVIDAD)
        mock_db_manager.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
