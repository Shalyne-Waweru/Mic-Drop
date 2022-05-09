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

class Interview:

    all_interviews = []

    def __init__(self,interview):
        self.interview = interview


    #Appends the interview object to a class variable all_interviews that is an empty list. 
    def save_interview(self):
        Interview.all_interviews.append(self)

    #Clears all the Items from the list
    @classmethod
    def clear_interviews(cls):
        Interview.all_interviews.clear()

    #Get all the Interviews
    @classmethod
    def get_interviews(cls):

        response = []

        for interview in cls.all_interviews:
            response.append(interview)

        return response

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

class Comments:

    all_comments = []

    def __init__(self,comment):
        self.comment = comment


    #Appends the comment object to a class variable all_comments that is an empty list. 
    def save_comment(self):
        Comments.all_comments.append(self)

    #Clears all the Items from the list
    @classmethod
    def clear_comments(cls):
        Comments.all_comments.clear()

    #Get all the Comments
    @classmethod
    def get_comments(cls):

        response = []

        for comment in cls.all_comments:
            response.append(comment)

        return response