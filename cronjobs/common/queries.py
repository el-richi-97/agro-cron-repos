QUERY_UPDATE_ACTIVIDADES_EN_CURSO = """
    UPDATE actividades
    SET id_estado_actividad = 2
    WHERE fecha_inicio_actividad::DATE <= CURRENT_DATE and fecha_fin_real_actividad IS NULL
"""

QUERY_UPDATE_FECHA_FIN_REAL_ESTADO_CERRADO_ACTIVIDAD = """
    update actividades 
    set fecha_fin_real_actividad = 
    case 
        when id_estado_actividad = 3 then current_timestamp else null 
    end
"""

QUERY_AGRO_UPDATE_ID_ESTADO_ACTIVIDAD = """
update actividades set id_estado_actividad = 3 where fecha_fin_real_actividad is not null
"""

QUERY_UPDATE_CANT_SALIDAS_ACTIVIDAD = """
    -- actualizar salidas
    UPDATE actividades
    SET cantidad_salidas = (
        SELECT 
            COALESCE((SELECT COUNT(*) FROM agro_salidas WHERE id_actividad = actividades.id_actividad), 0) +
            COALESCE((SELECT COUNT(*) FROM agro_salidas_consumos WHERE id_actividad = actividades.id_actividad), 0) +
            COALESCE((SELECT COUNT(*) FROM agro_salidas_personal WHERE id_actividad = actividades.id_actividad), 0) +
            COALESCE((SELECT COUNT(*) FROM agro_salidas_semillas WHERE id_actividad = actividades.id_actividad), 0)
        FROM actividades AS sub
        WHERE sub.id_actividad = actividades.id_actividad
    )
"""

QUERY_UPDATE_PORCENTAJE_CUMPLIMIENTO_ACTIVIDADES = """
    UPDATE actividades
    SET porcentaje_finalizacion =
    CASE
        WHEN current_date <= fecha_inicio_actividad THEN 0
        WHEN current_date >= fecha_fin_tentativa_actividad THEN 100
        ELSE
            ROUND(EXTRACT(EPOCH FROM (current_date - fecha_inicio_actividad)) / EXTRACT(EPOCH FROM (
            actividades.fecha_fin_tentativa_actividad - actividades.fecha_inicio_actividad)) * 100, 2)
    END
"""
