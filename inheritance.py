class vehicle:
    def __init__(self,name,maximum_speed,mileage):
        self.name=name
        self.maximum_speed=maximum_speed
        self.mileage=mileage
class bus(vehicle):
    pass
ob=bus("volvo",180,890)
print(ob.name)
print(ob.maximum_speed)
print(ob.mileage)