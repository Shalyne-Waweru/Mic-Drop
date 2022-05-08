class Pickup:

    all_pickup_lines = []

    def __init__(self,pickupLine):
        self.pickupLine = pickupLine


    #Appends the pickupLine object to a class variable all_pickup_lines that is an empty list. 
    def save_pickup_line(self):
        Pickup.all_pickup_lines.append(self)

    #Clears all the Items from the list
    @classmethod
    def clear_pickup_lines(cls):
        Pickup.all_pickup_lines.clear()

    #Get all the Pickup Lines
    @classmethod
    def get_pickup_lines(cls):

        response = []

        for pLine in cls.all_pickup_lines:
            response.append(pLine)

        return response