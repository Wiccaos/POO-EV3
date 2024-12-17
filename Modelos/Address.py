from Modelos.User import User

class Address(User):
    """Direcciones"""
    def __init__(self, street='', suite='', city='', zip_code='', lat='', lng='', userId=0):
        super().__init__(userId)
        self.street = street
        self.suite = suite
        self.city = city
        self.zip_code = zip_code
        self.lat = lat
        self.lng = lng
