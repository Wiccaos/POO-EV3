class Address():
    """Direcciones"""
    def __init__(self, street, suite, city, zip_code, lat, lng, userId):
        self.userId = userId
        self.street = street
        self.suite = suite
        self.city = city
        self.zip_code = zip_code
        self.lat = lat
        self.lng = lng
