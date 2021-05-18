# *******************************************************************
#  Inheritance - Super Invoking in constructor ( Multiple Inheritance )
# *******************************************************************


class Family:
    def __init__(self, lastName, address, *args, **kwargs):
        print('Executing : __init__ of Family Class.')
        self.lastName = lastName
        print('*' * 60)
        print('Finished : __init__ of Family Class.')

    # Inherited Method
    def my_family_name(self):
        return 'Family name : {}'.format(self.lastName)


class Father(Family):
    def __init__(self, Father_name, Father_age, *args, **kwargs):
        print('Executing : __init__ of Father Class.')
        super(Father, self).__init__(*args, **kwargs)

        self.f_name = Father_name
        self.f_age = Father_age
        print('Finished : __init__ of Father Class.')

    def __set_occupation(self, occupation):
        self.occupation = occupation


class Mother(Family):
    def __init__(self, Mother_name, Mother_age, *args, **kwargs):
        print('Executing : __init__ of Mother Class.')
        super(Mother, self).__init__(*args, **kwargs)

        self.m_name = Mother_name
        self.m_age = Mother_age
        print('Finished : __init__ of Mother Class.')

    def __set_hobbie(self, hobbie):
        self.hobbie = hobbie


class Son(Father, Mother):
    def __init__(self, name, age, *args, **kwargs):
        print('Executing : __init__ of Son Class.')
        super(Son, self).__init__(*args, **kwargs)

        self.name = name
        self.age = age
        print('Finished : __init__ of Son Class.')

    def mother_class_info(self):
        return f"Name : {super().f_name}"

    def __str__(self):
        return f"\n\nSon's Name : {self.name} {self.lastName} | Age : {self.age}" \
               f"\nFather's Name : {self.f_name} {self.lastName} | Age : {self.f_age}" \
               f"\nMother's Name : {self.m_name} {self.lastName} | Age : {self.m_age}\n\n"


beta = Son(name='Aditya', age=26, lastName='Tiwary', Father_name='Alok', Father_age=61, Mother_name='Sanju',
           Mother_age=48, address='#143, ABC, India', occupation='Businessman', hobbie='Modesty')
print(beta)
