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