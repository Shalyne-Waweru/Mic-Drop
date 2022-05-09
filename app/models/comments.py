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