from abc import ABC, abstractmethod


class AbstractParent(ABC):
    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError

    @abstractmethod
    def cook_dinner(self):
        raise NotImplementedError

    @abstractmethod
    def fix_the_tv(self):
        raise NotImplementedError


class Mother(AbstractParent):
    def __init__(self, age=0):
        self.age = age
        print('mother constructor')

    def __del__(self):
        print('Goodbye mother')

    def do_work(self):
        print('i\'m working')

    def cook_dinner(self):
        print('i\'m cooking')

    def fix_the_tv(self):
        print('my husband is a useless beer drinker')

    def do_housework(self):
        print('listening to music')

    def hello_friend(self):
        print('hello darkness')


class Father(AbstractParent):
    def __init__(self):
        print('father constructor')

    def __del__(self):
        print('Goodbye father')

    def play_guitar(self):
        print('i\'m playing the guitar')

    def cook_dinner(self):
        print('galya, zhrat\'!')

    def fix_the_tv(self):
        print('i\'m fixing the tv')

    def do_housework(self):
        print('sitting on the sofa and drinking beer')

    def hello_friend(self):
        print('all of my beer cans are my friends')


class Daughter(Mother, Father):
    def __init__(self, age=0):
        Mother.__init__(self)
        Father.__init__(self)

    def __del__(self):
        print('I\'m all alone')

    def do_work(self):
        print('i\'m working like a horse')

    def hello_friend(self):
        print('hello friend')


class Friend:
    pass


def greet_mother(mother: Mother):
    print('hello mother')
    mother.do_work()
    mother.cook_dinner()
    mother.fix_the_tv()
    mother.do_housework()
    mother.hello_friend()


def greet_father(father: Father):
    print('time for beer!')
    father.play_guitar()
    father.cook_dinner()


if __name__ == '__main__':
    daughter = Daughter()
    # mother.do_work()
    # daughter.__class__ = Friend
    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    mother = Mother()
    mother.fix_the_tv()
    father = Father()
    father.fix_the_tv()

    for x in [daughter]:
        x.do_housework()

    # tuple
    vasian = ('11 years', 12, 3.14, daughter)
    # set -- unique objects
    my_set = {23, 11, 10, 10, 'call'}
    print(my_set)
    # list -- for lab
    povtorka_list = ['mathan_2', 'programming_2', 'superprise']
    print(povtorka_list)
    # frozen set -- objects can't be removed (=> immutable)
    another_set = frozenset(['let', 'it', 'go'])
    print(another_set)
    # dictionary - key-word pairs, any type, anything you want, a tuple as a key, enjoy your stay here in Python
    my_dict = {1: "first", "2": 123, (1, 2, 3): "tuple_as_a_key"}
    print(my_dict)
