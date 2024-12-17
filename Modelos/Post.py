from Modelos.User import User

class Post(User):
    """publicaciones"""
    def __init__(self, userId=0, id=0, title='', body=''):
        super().__init__(userId)
        self.id = id
        self.title = title
        self.body = body