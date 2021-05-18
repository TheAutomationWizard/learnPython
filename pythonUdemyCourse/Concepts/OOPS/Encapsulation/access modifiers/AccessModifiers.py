class PrivateFields:
    # Public Field
    public_name = 'Aditya Inc.'

    # Protected Field
    _protected_funding = 20
    _another_protected_funding = 50

    # Private Field
    __private_funding = 100

    # Private Methods
    def __add_more_private_funding(self, amount_received):
        self.__private_funding += amount_received

    # Public Methods
    def add_private_funds(self, amount):
        self.__add_more_private_funding(amount)

    # Protected Methods
    def funding_from_known_sources(self, funding):
        self._protected_funding += funding

    # ***********   Encapsulation in Python, Getter & Setters Using property class
    @property
    def another_protected_funding(self):
        return self._another_protected_funding

    @another_protected_funding.setter
    def another_protected_funding(self, value):
        self._another_protected_funding += value


if __name__ == '__main__':
    private_test = PrivateFields()
    # ********************************************************
    #          Public Fields & Methods
    # ********************************************************
    print(f'Public Field : {private_test.public_name}')

    # ********************************************************
    #          Protected Fields & Methods
    # ********************************************************
    # Directly Accessing Protected Variables
    print(f'Protected Field : {private_test._protected_funding}')
    private_test._protected_funding += 20
    print(f'Protected Field : {private_test._protected_funding}')

    # Indirectly Accessing Protected Variables ( Using property class)
    print(f'Protected Field : {private_test.another_protected_funding}')
    private_test.another_protected_funding += 20
    print(f'Protected Field : {private_test.another_protected_funding}')

    # ********************************************************
    #          Nothing in Python is truly Private (Internally)
    # ********************************************************
    try:
        print(f'Public Field {private_test.__private_funding}')
    except Exception:
        print('Failed to access private field.')
    finally:
        print(f'Nothing is really private in Python : {PrivateFields()._PrivateFields__private_funding}')
