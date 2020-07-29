if __name__ == '__main__':
    my_dict = {'first': 2, (23) : 'second', 2 : 23, frozenset({23, 45}) : 'vasian'}
    print(my_dict)
    another_dict = dict(first=2, second='second', third=23, fourth='vasian')
    print(another_dict)
    third_approach = dict([('first', 2), ((23,), 'second')])
    print(third_approach)
    fourth_dict = dict({'first' : 2, (23,) : 'second', 2 : 23, frozenset({23, 45}) : 'vasa'})
    fifth_dict = {}

    print('element by key first: ' + str(my_dict['first']))
    print('element by key nine: ' + str(my_dict.get('nine')))
    my_dict['nine'] = 2334
    my_dict.pop('first')
    del my_dict[2]
    print(my_dict)
    my_dict.clear()
    print(my_dict)

    for x in iter(my_dict.keys()):
        print(x)

    valueable_dict = {x: x*x*x for x in range(10)}
    print(valueable_dict)

    # work with strings
    input_string = 'hello'
    hello = '-'.join(input_string)
    print(hello)

    print('Hi! How are you? I\'m fine'.split('.'))
    string_to_center = 'start data processing'
    print(string_to_center.center(50, '-'))

    print(string_to_center.ljust(50, '-'))
    print(string_to_center.zfill(25))

    # format strings
    print("Hello dear %s! I'm glad to see you at %s exam! Your current score is: %5.2f" % ("Vasyl", "Programming", 95.567))

    print("Hello dear {student}! I'm glad to see you at {subject} exam! Your current score is: {score:5.2f}".format(student='Vasyl', subject='Programming', score=95.567))

    print("Hello dear {0:s}! I'm glad to see you at {1:s} exam! Your current score is: {2:5.2f}".format("Vasyl", "Programming", 95.567))