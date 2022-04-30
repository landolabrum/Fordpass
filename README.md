# Fordpass

### An unofficial wrapper for Ford Motor Co. - Fordpass Connect
---
## installation
1. Clone the repo: `git clone https://github.com/LandoLabrum/Fordpass.git`
2. Install the dependancies: `pip install -r requirements.txt`
3. Replace the `<USERNAME>` and `<PASSWORD>` in demo.py
4. Run demo.py: `python3 demo.py`
---
## Documentation: 
- [connectedcar](https://ianjwhite99.github.io/connected-car-python-sdk/api.html)
---
## Features
*example: *`Fordpass(username=<USERNAME>, password=<PASSWORD>).status`
| Feature | Description |
|--------|---------------|
|user|Detailed info from User account|
|status|Detailed info from Status of Vehicle|
|maintenance_schedule|Vehicles Maintainence Schedule|
|recall_status|Any applicable recalls of vehicle
|vin|Vehicles Vin number|
|fuel|Vehicles fuel status|
|oil|Vehicles oil status|
|tire_pressure|Vehicles tire pressure status|
|battery|Vehicles battery status|
|capability|Vehicles build capabilities|
|location|Vehicles current location|
|window_positions|Vehicles current window position|
|door_status|Vehicles current door position|
|lock_status|Vehicles current lock status|
|alarm_status|Vehicles current alarm status|
|ignition_status|Vehicles current ignition status|
|start|Start the vehicle|
|stop|Stop the vehicle|
|lock|Lock the vehicle|
|unlock|Unlock the vehicle|



