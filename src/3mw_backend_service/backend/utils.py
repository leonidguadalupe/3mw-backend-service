from io import StringIO

from contextlib import contextmanager
from typing import List, Iterable

from django.db.backends.utils import CursorWrapper
from django.db import connection
from backend.models import Datapoint as DatapointModel

@contextmanager
def create_destroy_datapoint_table(cursor: CursorWrapper):
    """Context manager for creating and dropping temp tables"""
    cursor.execute(
        '''
        DROP TABLE IF EXISTS temp_datapoint;

        CREATE TEMPORARY TABLE temp_datapoint AS
        SELECT * FROM backend_datapoint LIMIT 0;
        '''
    )
    try:
        yield
    finally:
        cursor.execute(
            '''
            DROP TABLE IF EXISTS temp_datapoint;
            '''
        )

def create_tsv_file(rows: Iterable) -> StringIO:
    file = StringIO()
    for row in rows:
        print(row)
        file.write('\t'.join(str(value) for value in row) + '\n')

    file.seek(0)
    return file

def populate_temp_table(cursor: CursorWrapper, datapoints: List[DatapointModel]):
    def generate_rows_from_datapoints():
        for datapoint in datapoints:
            yield (str(datapoint.plant_id), datapoint.datetime_generated,
                datapoint.energy_expected, datapoint.energy_observed,
                datapoint.irradiation_expected, datapoint.irradiation_observed
            )

    tsv_file = create_tsv_file(generate_rows_from_datapoints())
    cursor.copy_from(
        tsv_file,
        'temp_datapoint',
        columns=('plant_id', 'datetime_generated', 'energy_expected', 'energy_observed',
            'irradiation_expected', 'irradiation_observed'
        )
    )

def copy_from_temp_table(cursor: CursorWrapper):
    cursor.execute(
        '''
        INSERT INTO backend_datapoint(plant_id, datetime_generated, energy_expected,
        energy_observed, irradiation_expected, irradiation_observed)
        SELECT td.plant_id, td.datetime_generated, td.energy_expected, td.energy_observed,
        td.irradiation_expected, td.irradiation_observed
        FROM temp_datapoint td
        ON CONFLICT(plant_id, datetime_generated) DO UPDATE SET
            energy_expected = EXCLUDED.energy_expected, energy_observed = EXCLUDED.energy_observed,
            irradiation_expected = EXCLUDED.irradiation_observed
        '''
    )
def bulk_upsert_datapoints(datapoints: List[DatapointModel]):
    with connection.cursor() as cursor:
        with create_destroy_datapoint_table(cursor):
            populate_temp_table(cursor, datapoints)
            copy_from_temp_table(cursor)