# Example Flask ESDL service 

Example Flask ESDL service, that receives an ESDL description via an API and calculates the amount of instances of each ESDL class

## Starting the application

To build the Docker container and run the application:

```shell
make
```

Use your browser and navigate to: http://localhost:4000/api

The endpoint `/esdl_service/count_esdl_objects` expects a Base64 encode ESDL string.

An example output would be:

```json
{
  "AggregatedBuilding": 1,
  "Area": 3,
  "Carriers": 1,
  "EnergyCarrier": 1,
  "EnergySystemInformation": 1,
  "GasHeater": 1,
  "GasNetwork": 1,
  "GenericProducer": 1,
  "HeatCommodity": 1,
  "HeatingDemand": 1,
  "InPort": 3,
  "InfluxDBProfile": 1,
  "Instance": 1,
  "OutPort": 3,
  "Point": 4,
  "QuantityAndUnitType": 1,
  "QuantityAndUnits": 1,
  "SingleValue": 1
}
```

## Stopping the Docker container

To stop and remove the Docker container:
```shell
make stop
```