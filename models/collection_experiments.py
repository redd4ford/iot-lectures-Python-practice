def add_sequence(sequence):
    # this one does not modify the existing sequence, it creates
    # a new sequence
    # if we do sequence *= 2 it will change the existing list though
    sequence = sequence * 2
    print(sequence * 2)
    # will cause an error when trying to add something to tuple
    sequence.append('new string')
    print(sequence)


def add_element_to_tuple(sequence : tuple):
    sequence[0].append(10)


def play_with_slicing():
    my_list = [3, '12', 3.2, 6, (2, 3), 'wow', '4']
    # print everything starting from 2 ending with 5, 3 elements overall
    print('slice 1: ' + str(my_list[2:5]))
    print('slice 2: ' + str(my_list[2:7]))
    print('slice 3: ' + str(my_list[2:7:2]))


if __name__ == '__main__':
    add_sequence([1, 2, 3, 4])
    # will not work because tuple's element is immutable
    # add_element_to_tuple(('first', 'second'))
    test_list = [1, 2, 3, 4]
    # proofs that the original sequence does not change
    # because any method or function uses a copy of your object
    print('before: ' + str(test_list))
    add_sequence(test_list)
    print('after: ' + str(test_list))
    if 2 in test_list:
        print ('I\'m happy')
    new_tuple = ([1, 2], [3, 4])
    print('before: ' + str(new_tuple))
    add_element_to_tuple(new_tuple)
    print('after: ' + str(new_tuple))
    play_with_slicing()