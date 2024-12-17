class User:
    """Clase de los usuarios"""
    def __init__(self, userId=0, name='', username='', email='', website = '', phone=''):
        self.userId = userId
        self.name = name
        self.username = username
        self.email = email
        self.website = website
        self.phone = phone