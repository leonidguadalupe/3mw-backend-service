# 3mw-backend-service

## Introduction
This is the backend service of the application. Documentation needs some work (I could add Sphinx soon)! It does the following functionalities:
* `CRUD` for creating power plants.
This is being catered by django rest framework model viewset and serializer.
* `CREATE` datapoints for the power plants. This is handled through an upsert functionality which is made possible by postgres. However, I tried something faster by using a temporary table, copying all the generated datapoints into a tsv, moving all of it to the temporary table and then detecting conflict through the partial unique constraint uid and datetime generated (which is hourly). I tried this as it sped up the insert significantly. 
* `Periodic task` to get data from monitoring service. This is implemented using celery task and celery beat (with Redis as broker)
* `Generate reports`

## Challenges
As I am not sure how the monitoring app looks like, I have created my own but had issues getting the internal IP of the app within the docker network. 