# https://github.com/ianjwhite99/connected-car-python-sdk/blob/07e1c3a04bfb7f6377fd32ed6df0297a909bb3c4/connectedcar/vehicle.py#L6
import connectedcar
from Fordpass.support import info, action

class Fordpass(object):
    def __init__(self, username=None, password=None):
        if username != None and password != None:
            self.connectedcar = connectedcar
            client = self.connectedcar.AuthClient(
                '9fb503e0-715b-47e8-adfd-ad4b7770f73b',
                None,
                None)  # Create client connection
            access = client.get_user_access_token(username, password)  # Fetch client access token
            
            user = self.connectedcar.User(access['access_token'])  # New User Object
            self.vehicles = user.vehicles()  # Fetch list of user vehicles
            self.access = access
            self.usr = user
        else:
            print("Fordpass takes username=<USERNAME> or password=<PASSWORD>")
            exit
    @property
    def user(self):
        return self.usr.info()

    @property
    def status(self):
        return info(self).details()

    @property
    def maintenance_schedule(self):
        return info(self).maintenance_schedule()

    @property
    def recall_status(self):
        return info(self).recall_status()

    @property
    def vin(self):
        return info(self).vin()

    @property
    def fuel(self):
        return info(self).fuel()

    @property
    def oil(self):
        return info(self).oil()

    @property
    def tire_pressure(self):
        return info(self).tire_pressure()

    @property
    def battery(self):
        return info(self).battery()

    @property
    def capability(self):
        return info(self).capability()

    @property
    def location(self):
        return info(self).location()

    @property
    def window_positions(self):
        return info(self).window_positions()

    @property
    def door_status(self):
        return info(self).door_status()

    @property
    def lock_status(self):
        return info(self).lock_status()

    @property
    def alarm_status(self):
        return info(self).alarm_status()

    @property
    def ignition_status(self):
        return info(self).ignition_status()

    @property
    def start(self):
        return action(self).start()

    @property
    def stop(self):
        return action(self).stop()

    @property
    def lock(self):
        return action(self).lock()

    @property
    def unlock(self):
        return action(self).unlock()

# print(Fordpass(username='lando@deepturn.com', password='Progress123').user)
# print(Fordpass().status)
# print(Fordpass().capability)
# print(Fordpass().maintenance_schedule)
# print(Fordpass().stop)




