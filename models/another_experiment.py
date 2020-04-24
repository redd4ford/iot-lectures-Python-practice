from multimethod import multimethod
import doctest


class WithStaticAndOverload:
    worker_name = 'some name'

    def __init__(self):
        pass

    @staticmethod
    def do_work():
        """
        >>> WithStaticAndOverload.do_work()
        'some name'
        """
        return WithStaticAndOverload.worker_name

    @staticmethod
    def sing_a_song():
        """
        >>> WithStaticAndOverload.sing_a_song()
        'What do we do with a drunken sailor?'
        """
        return 'What do we do with a drunken sailor?'

    # overloading example -- specifying the variable type is not necessary

    @multimethod
    def print_data(self, first: str, second: str):
        """
        >>> WithStaticAndOverload().print_data('1', '010101')
        '1010101'
        """
        return first + second

    @multimethod
    def print_data(self, first: int, second: int):
        """
        >>> obj.print_data(10, 20)
        30
        """
        return first + second


def print_non_class_data(first: int, second: int):
    """
    returns sum of two integers
    >>> print_non_class_data(10, 20)
    30
    >>> print_non_class_data(-3, 4)
    1
    """
    return first + second


def create_tuple(first: int, second: int):
    """
    returns tuple of two integers
    >>> create_tuple(10, 20)
    (10, 20)
    >>> create_tuple(20, 70)
    (20, 70)
    """
    return (first, second)


if __name__ == '__main__':
    # doctest - checks your documentation and performs operations from it
    doctest.testmod(verbose=True, extraglobs={'obj': WithStaticAndOverload()})
    # command in terminal: python -m doctest -v app/models/another_experiment.py
    my_object = WithStaticAndOverload()
    my_object.sing_a_song()
    my_object.print_data(23, 45)
    my_object.print_data('34', '78')
