from Modelos.User import User

class Company(User):
    """Empresas"""
    def __init__(self, name_company='', catch_phrase='', bs='', userId=0):
        super().__init__(userId)  # Corrected line
        self.name_company = name_company
        self.catch_phrase = catch_phrase
        self.bs = bs
