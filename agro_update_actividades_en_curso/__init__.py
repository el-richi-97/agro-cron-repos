import datetime
import logging
import azure.functions as func


def agro_update_actividades_en_curso(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')
    logging.info('Python timer trigger function agro_update_actividades_en_curso ran at %s', utc_timestamp)
