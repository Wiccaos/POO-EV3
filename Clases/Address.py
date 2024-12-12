import Users

class Address(Users):
    def __init__(self, id_addreses, street, suite, city, zip_code, lat, lng, userId):
        self.userId = userId
        self.id_address = id_addreses
        self.street = street
        self.suite = suite
        self.city = city
        self.zip_code = zip_code
        self.lat = lat
        self. lng = lng
