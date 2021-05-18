# *******************************************************************
#  Inheritance - Super Invoking in constructor ( Multiple Inheritance )
# *******************************************************************


class Family:
    lastName = 'Test'

    def __init__(self):
        print('Executing : __init__ of Family Class.')
        print('Finished : __init__ of Family Class.')

    # Inherited Method
    def my_family_name(self):
        return 'Family name : {}'.format(self.lastName)


class Father(Family):
    baapKaNaam = 'baap'
    def __init__(self):
        print('Executing : __init__ of Father Class.')
        print('Finished : __init__ of Father Class.')

    def set_occupation(self, occupation):
        return self.baapKaNaam


class Mother(Family):
    MaaKaNaam = 'Maa'
    def __init__(self):
        print('Executing : __init__ of Mother Class.')
        print('Finished : __init__ of Mother Class.')

    def set_hobbie(self, hobbie=''):
        return self.MaaKaNaam

class Son(Father, Mother):
    def __init__(self):
        print('Executing : __init__ of Son Class.')
        print('Finished : __init__ of Son Class.')

    def mother_class_info(self):
        return super(Son, self).set_hobbie()

beta = Son()
print(beta.mother_class_info())