class Promotion:

    all_promotions = []

    def __init__(self, promotion):
        self.promotion = promotion

    #Appends the Promotion object to a class variable all_promotions that is an empty list. 
    def save_promotion(self):
       Promotion.all_promotions.append(self)

    #Clears all the Items from the list
    @classmethod
    def clear_promotions(cls):
       Promotion.all_promotions.clear()

    #Get all the Promotions
    @classmethod
    def get_promotions(cls):

        response = []

        for promotion in cls.all_promotions:
            response.append(promotion)

        return response