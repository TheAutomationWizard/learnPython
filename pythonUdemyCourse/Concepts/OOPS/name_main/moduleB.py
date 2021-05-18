from moduleA import first_method


def second_method():
    print('I am in module B.')
    print('Here, __name__ : ',__name__)


if __name__ == '__main__':
    second_method()
    first_method()
