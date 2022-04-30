def info(self):
    vehicle = None
    for userVehicle in self.vehicles:  # For each user vehicle
        vehicle = self.connectedcar.Vehicle(userVehicle['vin'], self.access['access_token'])
    return vehicle

def user(self):
    user = None
    for userVehicle in self.vehicles:  # For each user vehicle
        user = self.connectedcar.Vehicle(userVehicle['vin'], self.access['access_token'])
    return user

def action(self):
    vehicleList = []  # Stored list of user vehicles
    for userVehicle in self.vehicles:  # For each user vehicle
        vehicleList.insert(0, userVehicle['vin'])
        break
    return self.connectedcar.Vehicle(
        vehicleList[0], self.access['access_token'])  # Create vehicle object


