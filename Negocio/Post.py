class Post:
    """publicaciones"""
    def __init__(self, userId = 0, id = 0, title = '', body = ''):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body