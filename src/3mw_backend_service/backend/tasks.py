import requests

from celery import task
from backend.models import Datapoint as DatapointModel, Plant as PlantModel
from datetime import datetime

@task()
def get_all_datapoints_for_plants():
    plants = PlantModel.objects.all()
    date_today = str(datetime.now().date())
    for plant in plants:
        try:
            r = requests.get(f'http://172.21.0.9:5000/', 
                    params= {
                        'plant-id': plant.uid,
                        'from':date_today,
                        'to':date_today
                    },
            )
        except requests.exceptions.RequestException as e: 
            raise e
        
        result = r.json()
        
        def unpack(n):
            return DatapointModel(
                plant=PlantModel.objects.get(uid=plant_id),
                datetime_generated=n["datetime"],
                energy_expected=n["expected"]["energy"],
                energy_observed=n["observed"]["energy"],
                irradiation_expected=n["expected"]["irradiation"],
                irradiation_observed=n["observed"]["irradiation"]
            )
        unpacked_list = list(map(unpack,result["data"]))
        bulk_upsert_datapoints(unpacked_list)